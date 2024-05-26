#!/usr/bin/node

const request = require('request-promise');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

const GetMovie = async (url) => {
    try {
        const body = await request(url);
        const Data = JSON.parse(body);
        const charactersUrl = Data.characters;
        
        for (let i = 0; i < charactersUrl.length; i++) {
            const urlChar = charactersUrl[i];
            try {
                const charBody = await request(urlChar);
                const charsData = JSON.parse(charBody);
                console.log(charsData.name);
            } catch (err) {
                console.error('Error in chars:', err);
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

GetMovie(url);

