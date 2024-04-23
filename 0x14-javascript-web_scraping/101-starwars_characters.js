#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Bypass SSL verification
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details.');
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character details.');
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
