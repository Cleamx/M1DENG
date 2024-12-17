const DIRECTIONS = {
    RIGHT: 0,
    UP: 1,
    LEFT: 2,
    DOWN: 3
};

function checkCollision(x1, y1, x2, y2, radius) {
    const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    return distance < radius * 2;
}

function isValidMove(x, y, maze) {
    const gridX = Math.floor(x / maze.tileSize);
    const gridY = Math.floor(y / maze.tileSize);
    return maze.grid[gridY][gridX] !== 1;
}