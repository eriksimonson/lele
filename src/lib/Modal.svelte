<script lang="ts">
    import type { Game } from "./GameLogic.svelte";
    export let showModal;
    export let attempts: Game[];
    export let correctGame: Game;
    export let categories: (keyof Game)[];
    export let isWin: boolean = false;
</script>

{#if showModal}
    <div class="modal-overlay">
        <div class="modal-content">
            <h3>{isWin ? "You Won" : "You Lost"}</h3>
            <p>After {attempts.length} guesses.</p>
            {#each attempts as attempt}
                {#each categories as category}
                    <span>
                        {attempt[category] == correctGame[category]
                            ? "🟩"
                            : "⬛️"}
                    </span>
                {/each}
                <br />
            {/each}
            <p>
                Today's answer was: <a
                    href={correctGame.website}
                    target="_blank"
                    rel="noreferrer">{correctGame.name}</a
                >
            </p>
        </div>
    </div>
{/if}

<style>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal-content {
        padding: 20px;
        border-radius: 10px;
        min-width: 300px;
        text-align: center;
        background-color: var(--bg-color);
    }
</style>
