<script lang="ts">
  import type { Games, Game } from "./GameLogic.svelte";
  import { getGames, getCorrectGame, getCategories } from "./GameLogic.svelte";
  import Select from "./Select.svelte";
  import GameDisplay from "./GameDisplay.svelte";

  const choices: Games = getGames();
  const categories: (keyof Game)[] = getCategories();
  const correctGame: Game = getCorrectGame();
  let attempts: Game[] = [];

  const formatCategoryName = (category: string): string => {
    return category
      .replace(/([a-z])([A-Z])/g, "$1 $2") // Add space between camelCase words
      .replace(/^./, (str) => str.toUpperCase()); // Capitalize the first letter
  };
</script>

<main>
  
    <div class="row header-row">
      {#each categories as category}
        <div class="cell header-cell">
          {formatCategoryName(category)}
        </div>
      {/each}
    </div>
  <Select
    items={Object.fromEntries(
      Object.entries(choices).filter(([_, game]) => !attempts.includes(game)),
    )}
    callback={(selected) => (attempts = [selected, ...attempts])}
    {categories}
  />

  <div class="attempts-container">
    {#each attempts as attempt}
      <div class="row">
        <a
          class="display-link"
          href={attempt.website}
          target="_blank"
          rel="noreferrer"
        >
          <GameDisplay game={attempt} {categories} {correctGame} />
        </a>
      </div>
    {/each}
  </div>
</main>

<style>
  main {
    padding: 1rem;
    font-family: sans-serif;
    width: 100%;
  }

  .header-row {
    font-weight: bold;
    margin-top: 1rem;
  }

  .header-cell {
    background-color: #f0f0f0;
    color: #333;
  }

  .display-link {
    width: 100%;
  }
</style>
