<script>
    import { onMount, afterUpdate} from 'svelte';
    import partsData from '../data/Parts.json'; // Assuming the JSON file is in the same directory

    export let VehicleID;

    let parts = [];
    let filteredParts = [];
    let categories = [];
    let selectedCategories = new Set();
    let priceFilter = 'all';

    function updateParts() {
        let vehicleIDInt = parseInt(VehicleID);
        parts = partsData.filter(part => part.VehicleID === vehicleIDInt);
        filteredParts = parts;
        categories = Array.from(new Set(parts.map(part => part.Category)));
    }

    onMount(() => {
        updateParts();
    });

    afterUpdate(() => {
        updateParts();
        filterParts();
    });

    function filterParts() {
        console.log('Selected categories:', selectedCategories);
        console.log('Price filter:', priceFilter);

        const priceLimits = {
            '<50': 50,
            '<100': 100,
            '<200': 200,
            '<300': 300,
            '<400': 400,
            '<500': 500
        };

        filteredParts = parts.filter(part => {
            const matchesCategory = selectedCategories.size === 0 || selectedCategories.has(part.Category);
            const partPrice = parseFloat(part.Price);
            const matchesPrice = priceFilter === 'all' || partPrice < priceLimits[priceFilter];
            
            
            return matchesCategory && matchesPrice;
        });
    }

    function toggleCategory(category) {
        if (selectedCategories.has(category)) {
            selectedCategories.delete(category);
        } else {
            selectedCategories.add(category);
        }
        filterParts();
    }

    // $: filterParts(); // Re-run filterParts whenever reactive variables change

    // $: {
    //     console.log('Price filter changed:', priceFilter);
    //     filterParts();
    // }
</script>

<main>
    <div class="container">
        <div class="filter-bar">
            <h3>Filter by Price</h3>
            <div>
                <input type="radio" id="all" name="price" value="all" bind:group={priceFilter}>
                <label for="all">All</label>
            </div>
            <div>
                <input type="radio" id="lt50" name="price" value="<50" bind:group={priceFilter}>
                <label for="lt50">Less than $50</label>
            </div>
            <div>
                <input type="radio" id="lt100" name="price" value="<100" bind:group={priceFilter}>
                <label for="lt100">Less than $100</label>
            </div>
            <div>
                <input type="radio" id="lt200" name="price" value="<200" bind:group={priceFilter}>
                <label for="lt200">Less than $200</label>
            </div>
            <div>
                <input type="radio" id="lt300" name="price" value="<300" bind:group={priceFilter}>
                <label for="lt300">Less than $300</label>
            </div>
            <div>
                <input type="radio" id="lt400" name="price" value="<400" bind:group={priceFilter}>
                <label for="lt400">Less than $400</label>
            </div>
            <div>
                <input type="radio" id="lt500" name="price" value="<500" bind:group={priceFilter}>
                <label for="lt500">Less than $500</label>
            </div>
    
            <h3>Filter by Category</h3>
            {#each categories as category}
                <div>
                    <input type="checkbox" id={category} value={category} on:change={() => toggleCategory(category)}>
                    <label for={category}>{category}</label>
                </div>
            {/each}
        </div>
    
        <div class="parts-list">
            <h3>Parts List</h3>
            <ul>
                {#each filteredParts as part}
                    <li>
                        <strong>{part.Name}</strong> - {part.Description} (${part.Price})
                    </li>
                {/each}
            </ul>
        </div>
    </div>
</main>

<style>
    .container {
        display: flex;
    }
    .filter-bar {
        width: 200px;
        padding: 10px;
        border-right: 1px solid #ccc;
    }
    .parts-list {
        flex: 1;
        padding: 10px;
    }
</style>