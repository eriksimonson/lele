<script lang="ts">
  import type { Games, Game } from "./GameLogic.svelte";
  import { getGames, getCorrectGame, getCategories, getDayId } from "./GameLogic.svelte";
  import Select from "./Select.svelte";
  import GameDisplay from "./GameDisplay.svelte";
  import Modal from './Modal.svelte';

  const maxAttempts = 10;
  const choices: Games = getGames();
  const categories: (keyof Game)[] = getCategories();
  const correctGame: Game = getCorrectGame();
  const dayId: Number = getDayId();
  const localStorageId = `attemptsDay${dayId}`;
  const savedAttempts = JSON.parse(localStorage.getItem(localStorageId) || '[]');
  let attempts: Game[] = [...savedAttempts];

  let hasWon = false;
  $: hasWon = JSON.stringify(attempts.at(0)) === JSON.stringify(correctGame);
  let gameOver = false;
  $: gameOver = hasWon || attempts.length >= maxAttempts;

  const formatCategoryName = (category: string): string => {
    return category
      .replace(/([a-z])([A-Z])/g, "$1 $2") // Add space between camelCase words
      .replace(/^./, (str) => str.toUpperCase()); // Capitalize the first letter
  };
</script>

<main>
    <p>{attempts.length} of {maxAttempts}</p>
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
    callback={(selected) => {
      attempts = [selected, ...attempts];
      localStorage.setItem(localStorageId, JSON.stringify(attempts));
    }}
    {categories}
    disabled={gameOver}
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
  <Modal showModal={gameOver} {attempts} {correctGame} {categories} isWin={hasWon} />
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
