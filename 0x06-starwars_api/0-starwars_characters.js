#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

const GetMovie = (url) => {
    request(url, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        const Data = JSON.parse(body);
        const charactersUrl = Data.characters;
        charactersUrl.forEach((urlChar) => {
            request(urlChar, (err, res, body) => {
                if (err) {
                    console.error('Error in chars:', err);
                    return;
                }
                const charsData = JSON.parse(body);
                console.log(charsData.name);
            });
        });
    });
}

GetMovie(url);

