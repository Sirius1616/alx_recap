#!/usr/bin/env node

class Point {
    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    static displayName = 'point';
    static distance(a, b){
        const dx = a.x - b.x;
        const dy = a.y - b.y;

        return Math.hypot(dx, dy);
    }
}

const p1 = new Point(4, 6);
const p2 =  new Point(6, 3);

console.log(Point.displayName)
console.log(Point.distance(p1, p2))