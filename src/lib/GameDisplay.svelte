<script lang="ts">
    import type { Game } from "./GameLogic.svelte";
    export let game: Game;
    export let categories: (keyof Game)[] = [];
    export let correctGame: Game | undefined = undefined;
</script>

<div class="row" title="{game.description || "No description available."}">
    {#each categories as category}
        <div
            class="cell {correctGame ? (game[category] == correctGame[category]
                ? 'correct'
                : 'incorrect') : ''}"
        >
            {game[category] === -1 ? "∞" : game[category]}
        </div>
    {/each}
</div>
