<script lang="ts">
    import type { Game } from "./GameLogic.svelte";
    export let game: Game;
    export let categories: (keyof Game)[] = [];
    export let correctGame: Game | undefined = undefined;
    console.log(game);
</script>

<div class="row">
    {#each categories as category}
        <div
            class="cell {correctGame ? (game[category] == correctGame[category]
                ? 'correct'
                : 'incorrect') : ''}"
        >
            {game[category]}
        </div>
    {/each}
</div>

<style>
    .correct {
        background-color: green;
        color: white;
    }

    .incorrect {
        background-color: black;
        color: white;
    }
</style>
