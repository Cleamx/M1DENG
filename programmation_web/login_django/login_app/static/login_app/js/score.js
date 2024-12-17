class Score {
    constructor() {
        this.points = 0;
        this.level = 1;
        this.lives = 3;
    }

    addPoints(value) {
        this.points += value;
    }

    draw(ctx) {
        ctx.fillStyle = 'white';
        ctx.font = '20px Arial';
        ctx.textAlign = 'left';
        ctx.fillText(`Score: ${this.points}`, 10, 20);
        ctx.fillText(`Level: ${this.level}`, 10, 45);
        ctx.fillText(`Lives: ${this.lives}`, 10, 70);
    }
}