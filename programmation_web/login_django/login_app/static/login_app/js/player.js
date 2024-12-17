class Player {
    constructor(maze) {
        this.maze = maze;
        this.x = 21 * this.maze.tileSize + this.maze.tileSize / 2;
        this.y = 23 * this.maze.tileSize + this.maze.tileSize / 2;
        this.radius = maze.tileSize / 1.8; // Augmenter le rayon pour correspondre à la moitié d'une tuile
        this.speed = 2;
        this.direction = 'RIGHT';
        this.nextDirection = 'RIGHT';
        this.mouthOpen = true;
        this.score = 0;
        this.tunnelY = 14 * this.maze.tileSize + this.maze.tileSize / 2; // Position Y du tunnel
    }

    setDirection(direction) {
        this.nextDirection = direction;
        if (!this.direction) {
            this.direction = direction;
        }
    }

    update() {
        const oldX = this.x;
        const oldY = this.y;

        if (this.canMove(this.direction)) {
            switch (this.direction) {
                case 'RIGHT':
                    this.x += this.speed;
                    // Téléportation droite vers gauche
                    if (this.x > this.maze.width && Math.abs(this.y - this.tunnelY) < this.maze.tileSize) {
                        this.x = 0;
                    }
                    break;
                case 'LEFT':
                    this.x -= this.speed;
                    // Téléportation gauche vers droite
                    if (this.x < 0 && Math.abs(this.y - this.tunnelY) < this.maze.tileSize) {
                        this.x = this.maze.width;
                    }
                    break;
                case 'UP': this.y -= this.speed; break;
                case 'DOWN': this.y += this.speed; break;
            }
        }

        if (this.nextDirection && this.nextDirection !== this.direction && this.canMove(this.nextDirection)) {
            this.direction = this.nextDirection;
        }

        if (oldX !== this.x || oldY !== this.y) {
            this.mouthOpen = !this.mouthOpen;
        }
    }

    draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);

        let rotation = 0;
        switch (this.direction) {
            case 'LEFT': rotation = Math.PI; break;
            case 'UP': rotation = -Math.PI / 2; break;
            case 'DOWN': rotation = Math.PI / 2; break;
        }
        ctx.rotate(rotation);

        ctx.beginPath();
        ctx.fillStyle = 'yellow';
        const mouthAngle = this.mouthOpen ? 0.2 : 0;
        ctx.arc(0, 0, this.radius, mouthAngle, Math.PI * 2 - mouthAngle);
        ctx.lineTo(0, 0);
        ctx.fill();
        ctx.restore();
    }

    canMove(direction) {
        let nextX = this.x;
        let nextY = this.y;

        if (Math.abs(this.y - this.tunnelY) < this.maze.tileSize) {
            if ((direction === 'LEFT' && this.x < this.maze.tileSize) ||
                (direction === 'RIGHT' && this.x > this.maze.width - this.maze.tileSize)) {
                return true;
            }
        }
        switch (direction) {
            case 'RIGHT': nextX += this.speed; break;
            case 'LEFT': nextX -= this.speed; break;
            case 'UP': nextY -= this.speed; break;
            case 'DOWN': nextY += this.speed; break;
        }

        const canMove = !this.maze.checkCollision(nextX, nextY);
        return canMove;
    }

    reset() {
        // Position initiale
        this.x = 21 * this.maze.tileSize + this.maze.tileSize / 2;
        this.y = 23 * this.maze.tileSize + this.maze.tileSize / 2;
        this.direction = 'RIGHT';
        this.nextDirection = 'RIGHT';
    }
}