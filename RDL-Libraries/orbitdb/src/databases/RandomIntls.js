import Database from '../database.js'

const fs = require('fs');

function randomInterleave(events, visitedPaths) {
    const n = events.length;

    while (visitedPaths.size < factorial(n)) {
        const shuffledEvents = shuffleArray([...events]);
        const path = shuffledEvents.join(',');

        if (!visitedPaths.has(path)) {
            visitedPaths.add(path);
            console.log(shuffledEvents.join(','));
        }
    }
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function readEventsFromFile(filename) {
    return fs.readFileSync(filename, 'utf-8').trim().split('\n');
}

const events = readEventsFromFile('events.facts');
const visitedPaths = new Set();
randomInterleave(events, visitedPaths);
