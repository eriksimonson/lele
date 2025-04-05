<script lang="ts">
    import type { Games, Game } from "./GameLogic.svelte";
    import GameDisplay from "./GameDisplay.svelte";

    export let items: Games;
    export let categories: (keyof Game)[];
    export let callback: (item: Game) => void;
    export let disabled: boolean = false;

    let searchText: string = "";

    let filteredItems: string[] = Object.keys(items);
    $: filteredItems = Object.keys(items).filter((item) =>
        item.toLowerCase().startsWith(searchText.toLowerCase()),
    );

    function selectItem(item: string) {
        searchText = item;
        callback(items[item]);
        searchText = "";
    }

    function handleEnterKey(event: KeyboardEvent) {
        if (event.key === "Enter" && filteredItems.length > 0 && searchText) {
            selectItem(filteredItems[0]);
        }
    }
</script>

<div class="dropdown">
    <input
        type="text"
        bind:value={searchText}
        placeholder="Search games..."
        aria-label="Search games"
        on:keydown={handleEnterKey}
        disabled={disabled}
    />

    {#if filteredItems.length > 0 && searchText && searchText != filteredItems.at(0)}
        <div class="dropdown-list">
            {#each filteredItems as item}
            <div class="dropdown-item" on:click={() => selectItem(item)}>
                <GameDisplay game={items[item]} {categories}/>
            </div>
            {/each}
        </div>
    {/if}
</div>

<style>
    .dropdown {
        position: relative;
        width: 100%;
    }

    .dropdown input {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
    }

    .dropdown-list {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        max-height: 250px;
        overflow-y: auto;
        border: 1px solid #ccc;
        background-color: #345;
        z-index: 10;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
    }

    .dropdown-item {
        cursor: pointer;
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    .dropdown-item:hover {
        background-color: #234;
    }
</style>
