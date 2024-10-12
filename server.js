// server.js
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const csv = require('csv-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Endpoint for signup
app.post('/signup', (req, res) => {
    const { username } = req.body;

    // Read the CSV file and check for the taken username
    const takenUsernames = [];

    fs.createReadStream('users.csv')
        .pipe(csv())
        .on('data', (row) => {
            takenUsernames.push(row.username);
        })
        .on('end', () => {
            if (takenUsernames.includes(username)) {
                // If the username is taken, respond with an error
                return res.status(409).json({ message: 'Username is already taken. Please choose a different one.' });
            }

            // If username is available, respond with success
            return res.status(200).json({ message: 'Username is available.' });
        });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
