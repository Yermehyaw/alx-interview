#!/usr/bin/node
/**
 * StarWars API - Making requests to the API and receiving
 * handling responses asynchronously
 */
const request = require('request');

/* Get arg frm shell */
const arg = process.argv[2];
if (!arg) {
  process.exit(1);
}

function getJSONFromAPI (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Failed: ', error);
        return reject(error);
      }
      if (response.statusCode === 200) {
        try {
          const data = JSON.parse(body);
          const characterEndpoints = data.characters;
          resolve(characterEndpoints);
        } catch (parseError) {
          reject(parseError);
        }
      } else {
        reject(new Error(`Request failed with: ${response.statusCode}`));
      }
    });
  });
}

function getCharacterNames (characters) {
  const allRequests = characters.map(endpoint => {
    return new Promise((resolve, reject) => {
      request(endpoint, (error, response, body) => {
        if (error) {
          return reject(error);
        }
        if (response.statusCode === 200) {
          try {
            const data = JSON.parse(body);
            const characterName = data.name;
            resolve(characterName);
          } catch (parseError) {
            reject(parseError);
          }
        }
      });
    });
  });
  return Promise.all(allRequests);
}

const apiURL = `https://swapi-api.alx-tools.com/api/films/${arg}`;
getJSONFromAPI(apiURL)
  .then(films => {
    return getCharacterNames(films);
  })
  .then(characters => {
    for (const character of characters) { console.log(character); }
  })
  .catch(error => {
    console.error(error);
  });
