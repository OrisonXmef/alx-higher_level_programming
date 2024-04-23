#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

const fetchCharacterNames = async (characterUrls) => {
  const characterNames = [];
  for (const characterUrl of characterUrls) {
    try {
      const response = await axios.get(characterUrl, { httpsAgent: new (require('https').Agent)({ rejectUnauthorized: false }) });
      characterNames.push(response.data.name);
    } catch (error) {
      console.error('Error fetching character:', error.message);
      process.exit(1);
    }
  }
  return characterNames;
};

axios.get(apiUrl)
  .then(response => {
    const characters = response.data.characters;
    return fetchCharacterNames(characters);
  })
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Failed to fetch movie details:', error.message);
    process.exit(1);
  });
