<script context="module" lang="ts">
    import games from '../games.json';
    export type Game = {
     "name": string;
     "website": string;
     "releaseYear": string;
     "maxAttempts": number;
     "category": string;
     "userInput": string;
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
     "userInput",
     "difficultyLevel",
   ];

   const allGames: Games = games as Games;
  
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

  export const getDayId = (): Number => {
    return daysSince1970;
  }
 </script>