<script context="module" lang="ts">
  import games from "../games.json";
  export type Game = {
    name: string;
    website: string;
    releaseYear: string;
    maxAttempts: number;
    category: string;
    userInput: string;
    TLD?: string;
    userInputConfidence?: number;
    tags?: string[];
    description?: string;
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
    "TLD"
  ];

  const allGames: Games = addTLDsToGames(games as Games);

  const timezoneOffset = new Date().getTimezoneOffset();
  const localTime = Date.now() - timezoneOffset * 60 * 1000;
  const daysSince1970 = Math.floor(localTime / (1000 * 60 * 60 * 24));

  function addTLD(game: Game): Game {
    try {
      const url = new URL(game.website);
      const hostnameParts = url.hostname.split(".");
      const TLD = "." + hostnameParts[hostnameParts.length - 1];

      return { ...game, TLD };
    } catch (e) {
      console.error("Invalid URL in game.website:", game.website);
      return game;
    }
  }

  function addTLDsToGames(games: Games): Games {
    return Object.fromEntries(
      Object.entries(games).map(([key, game]) => [key, addTLD(game)]),
    );
  }

  export const getGames = (): Games => {
    const leleGame: Game = addTLD({
      name: "LeLe",
      website: "https://lele.bread.red/",
      releaseYear: "2025",
      maxAttempts: 10,
      category: "Miscellaneous",
      userInput: "Word",
      userInputConfidence: 1.0,
      tags: ["word", "guess"],
      description: "A game where you guess daily guessing games.",
    });
    return { ...allGames, leleGame};
  };

  export const getCorrectGame = (): Game => {
    const gameNames: (keyof Games)[] = Object.keys(allGames);
    return allGames[gameNames[daysSince1970 % gameNames.length]];
  };

  export const getCategories = (): (keyof Game)[] => {
    return categories;
  };

  export const getDayId = (): Number => {
    return daysSince1970;
  };
</script>
