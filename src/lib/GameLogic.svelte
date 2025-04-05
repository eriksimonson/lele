<script context="module" lang="ts">
    export type Game = {
     "name": string;
     "website": string;
     "releaseYear": string;
     "maxAttempts": number;
     "category": string;
     "guessType": string;
     "difficultyLevel": string;
   };
   export type Games = {
     [key: string]: Game;
   };
   const categories: (keyof Game)[] = [
    "name",
     "releaseYear",
     "maxAttempts",
     "category",
     "guessType",
     "difficultyLevel",
   ];
 
   const allGames: Games = {
     Wordle: {
       "name": "Wordle",
       "website": "https://www.nytimes.com/games/wordle/index.html", 
       "releaseYear": "2021",
       "maxAttempts": 6,
       "category": "Word-based",
       "guessType": "Word",
       "difficultyLevel": "Medium",
     },
    Quordle: {
      "name": "Quordle",
      "website": "https://www.quordle.com/",
      "releaseYear": "2022",
      "maxAttempts": 9,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Hard",
    },
    Absurdle: {
      "name": "Absurdle",
      "website": "https://qntm.org/files/absurdle/absurdle.html",
      "releaseYear": "2020",
      "maxAttempts": 6,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Hard",
    },
    Nerdle: {
      "name": "Nerdle",
      "website": "https://nerdlegame.com/",
      "releaseYear": "2021",
      "maxAttempts": 6,
      "category": "Math-based",
      "guessType": "Equation",
      "difficultyLevel": "Medium",
    },
    Worldle: {
      "name": "Worldle",
      "website": "https://worldle.teuteuf.fr/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Geography-based",
      "guessType": "Country",
      "difficultyLevel": "Medium",
    },
    Heardle: {
      "name": "Heardle",
      "website": "https://www.spotify.com/heardle/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Music-based",
      "guessType": "Song",
      "difficultyLevel": "Medium",
    },
    Framed: {
      "name": "Framed",
      "website": "https://framed.wtf/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Movie-based",
      "guessType": "Movie",
      "difficultyLevel": "Medium",
    },
    Globle: {
      "name": "Globle",
      "website": "https://globle-game.com/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Geography-based",
      "guessType": "Country",
      "difficultyLevel": "Medium",
    },
    Waffle: {
      "name": "Waffle",
      "website": "https://wafflegame.net/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Medium",
    },
    Letterle: {
      "name": "Letterle",
      "website": "https://edjefferson.com/letterle/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Word-based",
      "guessType": "Letter",
      "difficultyLevel": "Easy",
    },
    Octordle: {
      "name": "Octordle",
      "website": "https://octordle.com/",
      "releaseYear": "2022",
      "maxAttempts": 13,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Hard",
    },
    Dordle: {
      "name": "Dordle",
      "website": "https://www.dordlegame.com/",
      "releaseYear": "2022",
      "maxAttempts": 7,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Medium",
    },
    Squabble: {
      "name": "Squabble",
      "website": "https://squabble.me/",
      "releaseYear": "2022",
      "maxAttempts": 6,
      "category": "Word-based",
      "guessType": "Word",
      "difficultyLevel": "Medium",
    },
   };
   const timezoneOffset = new Date().getTimezoneOffset();
   const localTime = Date.now() - timezoneOffset * 60 * 1000;
   const daysSince1970 = Math.floor(localTime / (1000 * 60 * 60 * 24));

   export const getGames = (): Games => {
    return allGames;
   }

   export const getCorrectGame = (): Game => {
    const gameNames: (keyof Games)[] = Object.keys(allGames);
    return allGames[gameNames[daysSince1970 % gameNames.length]];
   }

   export const getCategories = (): (keyof Game)[] => {
    return categories;
   }
 
 </script>