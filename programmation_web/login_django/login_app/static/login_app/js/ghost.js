class Ghost {
    constructor(name, color, maze) {
        this.maze = maze;
        this.name = name;
        this.color = color;
        this.size = maze.tileSize / 1.8;
        this.releaseTimer = this.getReleaseTime();

        // Positions initiales dans la "maison"
        const positions = {
            'blinky': { x: 13, y: 11, released: true },
            'pinky': { x: 14, y: 11, releaseDelay: 1000 },
            'inky': { x: 13, y: 14, releaseDelay: 3000 },
            'clyde': { x: 14, y: 14, releaseDelay: 5000 }
        };

        this.x = positions[name].x * maze.tileSize + maze.tileSize / 2;
        this.y = positions[name].y * maze.tileSize + maze.tileSize / 2;
        this.released = positions[name].released || false;
        this.releaseDelay = positions[name].releaseDelay || 0;

        this.speed = 1.5;
        this.direction = 'UP';
        this.nextDirection = 'UP';
    }

    getReleaseTime() {
        const delays = {
            'blinky': 0,
            'pinky': 1000,
            'inky': 3000,
            'clyde': 5000
        };
        return delays[this.name] || 0;
    }

    update() {
        if (!this.released) {
            this.releaseTimer -= 16; 
            if (this.releaseTimer <= 0) {
                this.released = true;
                this.direction = 'UP';
            }
            return;
        }

        if (this.canMove(this.direction)) {
            switch (this.direction) {
                case 'RIGHT': this.x += this.speed; break;
                case 'LEFT': this.x -= this.speed; break;
                case 'UP': this.y -= this.speed; break;
                case 'DOWN': this.y += this.speed; break;
            }
        } else {
            this.chooseNewDirection();
        }
    }

    canMove(direction) {
        let nextX = this.x;
        let nextY = this.y;

        switch (direction) {
            case 'RIGHT': nextX += this.speed; break;
            case 'LEFT': nextX -= this.speed; break;
            case 'UP': nextY -= this.speed; break;
            case 'DOWN': nextY += this.speed; break;
        }

        return !this.maze.checkCollision(nextX, nextY);
    }

    chooseNewDirection() {
        const possibleDirections = ['UP', 'DOWN', 'LEFT', 'RIGHT']
            .filter(dir => dir !== this.getOppositeDirection(this.direction))
            .filter(dir => this.canMove(dir));

        if (possibleDirections.length > 0) {
            const randomIndex = Math.floor(Math.random() * possibleDirections.length);
            this.direction = possibleDirections[randomIndex];
        }
    }

    getOppositeDirection(dir) {
        const opposites = {
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT',
            'UP': 'DOWN',
            'DOWN': 'UP'
        };
        return opposites[dir];
    }

    draw(ctx) {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }

    reset() {
        const positions = {
            'blinky': { x: 13, y: 11 },
            'pinky': { x: 14, y: 11 },
            'inky': { x: 13, y: 14 },
            'clyde': { x: 14, y: 14 }
        };
        this.x = positions[this.name].x * this.maze.tileSize + this.maze.tileSize / 2;
        this.y = positions[this.name].y * this.maze.tileSize + this.maze.tileSize / 2;
        this.direction = 'LEFT';
    }
}