class Game {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.canvas.width = 600;  
        this.canvas.height = 660; 
        this.ctx = this.canvas.getContext('2d');
        this.setupClickHandler();

        document.getElementById('game-container').appendChild(this.canvas);

        this.maze = new Maze();
        this.player = new Player(this.maze);
        this.ghosts = [
            new Ghost('blinky', 'red', this.maze),
            new Ghost('pinky', 'pink', this.maze),
            new Ghost('inky', 'cyan', this.maze),
            new Ghost('clyde', 'orange', this.maze)
        ];
        this.score = 0;
        this.dots = this.initializeDots();
        this.gameOver = false;
        this.lives = 3;
        this.level = 1;
        this.isInvulnerable = false;
        this.invulnerableTime = 2000;

        this.setupControls();

        this.init();
    }

    initializeDots() {
        const dots = [];
        for (let y = 0; y < this.maze.grid.length; y++) {
            for (let x = 0; x < this.maze.grid[y].length; x++) {
                if (this.maze.grid[y][x] === 0) {
                    dots.push({
                        x: x * this.maze.tileSize + this.maze.tileSize / 2,
                        y: y * this.maze.tileSize + this.maze.tileSize / 2,
                        eaten: false
                    });
                }
            }
        }
        return dots;
    }

    setupControls() {
        document.addEventListener('keydown', (event) => {
            switch (event.key) {
                case 'ArrowLeft':
                    event.preventDefault();
                    this.player.nextDirection = 'LEFT';
                    break;
                case 'ArrowRight':
                    event.preventDefault();
                    this.player.nextDirection = 'RIGHT';
                    break;
                case 'ArrowUp':
                    event.preventDefault();
                    this.player.nextDirection = 'UP';
                    break;
                case 'ArrowDown':
                    event.preventDefault();
                    this.player.nextDirection = 'DOWN';
                    break;
            }
        });
    }

    setupClickHandler() {
        this.canvas.addEventListener('click', () => {
            if (this.gameOver) {
                this.resetGame();
            }
        });
    }

    resetGame() {
        this.score = 0;
        this.lives = 3;
        this.gameOver = false;
        this.dots = this.initializeDots();
        this.player.reset();
        this.ghosts.forEach(ghost => ghost.reset());
    }

    init() {
        this.lastTime = 0;
        this.gameLoop();
    }

    gameLoop() {
        this.update();
        this.draw();
        requestAnimationFrame(() => this.gameLoop());
    }

    update() {
        if (this.gameOver) return;

        this.player.update();
        this.ghosts.forEach(ghost => ghost.update());
        this.checkDotCollision();
        this.checkGhostCollision();
    }

    checkDotCollision() {
        let remainingDots = 0;
        this.dots.forEach(dot => {
            if (!dot.eaten) {
                remainingDots++;
                const distance = Math.hypot(this.player.x - dot.x, this.player.y - dot.y);
                if (distance < this.player.radius) {
                    dot.eaten = true;
                    this.score += 10;
                }
            }
        });

        if (remainingDots === 0) {
            this.levelUp();
        }
    }

    checkGhostCollision() {
        if (!this.isInvulnerable) {
            this.ghosts.forEach(ghost => {
                const distance = Math.hypot(this.player.x - ghost.x, this.player.y - ghost.y);
                if (distance < this.player.radius + ghost.size) {
                    this.handleGhostCollision();
                }
            });
        }
    }

    levelUp() {
        this.level++;
        this.dots = this.initializeDots();
        this.ghosts.forEach(ghost => {
            ghost.speed += 0.1;
        });
    }

    handleGhostCollision() {
        if (!this.isInvulnerable) {
            this.lives--;
            if (this.lives <= 0) {
                this.gameOver = true;

                fetch('save-score/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        "score": this.score
                    })
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'error') {
                            console.error('Error saving score:', data.message);
                        }
                    })
                    .catch(error => console.error('Error:', error));

            } else {
                this.resetPositions();
                this.makePlayerInvulnerable();
            }
        }
    }

    resetPositions() {
        this.player.reset();
        this.ghosts.forEach(ghost => ghost.reset());
    }

    makePlayerInvulnerable() {
        this.isInvulnerable = true;
        setTimeout(() => {
            this.isInvulnerable = false;
        }, this.invulnerableTime);
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.save();
        this.ctx.translate(
            (this.canvas.width - this.maze.width) / 2,
            (this.canvas.height - this.maze.height) / 2
        );

        this.maze.draw(this.ctx);

        this.dots.forEach(dot => {
            if (!dot.eaten) {
                this.ctx.beginPath();
                this.ctx.fillStyle = 'white';
                this.ctx.arc(dot.x, dot.y, 3, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });

        this.player.draw(this.ctx);
        this.ghosts.forEach(ghost => ghost.draw(this.ctx));
        this.ctx.restore();

        this.ctx.fillStyle = 'white';
        this.ctx.font = '20px Arial'; 
        this.ctx.fillText(`Score: ${this.score}`, 20, 20);
        this.ctx.fillText(`Lives: ${this.lives}`, 20, 40);
        this.ctx.fillText(`Level: ${this.level}`, 20, 60);

        if (this.gameOver) {
            this.ctx.fillStyle = 'red';
            this.ctx.font = '48px Arial';
            this.ctx.fillText('GAME OVER', this.canvas.width / 2 - 100, this.canvas.height / 2);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, creating game...');
    window.game = new Game();
});