import Database from '../database.js'
const fs = require('fs');

function dfs(path, remainingEvents, visitedPaths) {
    if (remainingEvents.length === 0) {
        console.log(path.join(','));
        return;
    }

    for (let i = 0; i < remainingEvents.length; i++) {
        const newPath = [...path, remainingEvents[i]];
        const newRemaining = remainingEvents.filter((_, index) => index !== i);
        const newPathString = newPath.join(',');

        if (!visitedPaths.has(newPathString)) {
            visitedPaths.add(newPathString);
            dfs(newPath, newRemaining, visitedPaths);
        }
    }
}

function readEventsFromFile(filename) {
    return fs.readFileSync(filename, 'utf-8').trim().split('\n');
}

const events = readEventsFromFile('InitRun/events.facts');
dfs([], events, new Set());
