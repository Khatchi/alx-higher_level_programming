#!/usr/bin/node

const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf-8', (error, content) => {
	if (error) {
		console.log(error);
	} else {
		console.log(content);
	}
});
