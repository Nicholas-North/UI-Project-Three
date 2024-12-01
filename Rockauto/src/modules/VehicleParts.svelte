<script>
    import { onMount, afterUpdate, getContext} from 'svelte';
    import partsData from '../data/Parts.json'; // Assuming the JSON file is in the same directory
    import carModels from '../data/Car_Models.json';

    export let VehicleID;

    let parts = [];
    let filteredParts = [];
    let categories = [];
    let selectedCategories = new Set();
    let priceFilter = 'all';
    let sortColumn = '';
    let sortDirection = 'asc';
    let car = carModels.find(car => car.VehicleID === parseInt(VehicleID));

    const addToCart = getContext('addToCart');
    const removeFromCart = getContext('removeFromCart');
    const isInCart = getContext('isInCart');
    const numInCart = getContext('numInCart');

    const cart = getContext('cart');

    function numParts(part, id){
        document.getElementById(id).innerHTML = numInCart(part);
    }

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

    function toggleCart(part) {
        if (isInCart(part)) {
            removeFromCart(part);
        } else {
            addToCart(part);
        }

    }

    function sortParts(column) {
        if (sortColumn === column) {
            sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
            sortColumn = column;
            sortDirection = 'asc';
        }

        filteredParts = [...filteredParts].sort((a, b) => {
            if (a[column] < b[column]) return sortDirection === 'asc' ? -1 : 1;
            if (a[column] > b[column]) return sortDirection === 'asc' ? 1 : -1;
            return 0;
        });
    }
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
            <h1>Showing results for: {car.Company + ' ' + car.Model + ' ' + car.Year}</h1>
            <h3>Parts List</h3>
            <table>
                <thead>
                    <tr>
                        <th on:click={() => sortParts('Name')}>Name</th>
                        <th on:click={() => sortParts('Category')}>Category</th>
                        <th on:click={() => sortParts('Description')}>Description</th>
                        <th on:click={() => sortParts('Price')}>Price</th>
                        <th>Add to Cart?</th>
                    </tr>
                </thead>
                <tbody>
                    {#each filteredParts as part, index}
                        <tr class={index % 2 === 0 ? 'even' : 'odd'}>
                            <td>{part.Name}</td>
                            <td>{part.Category}</td>
                            <td>{part.Description}</td>
                            <td>${part.Price}</td>
                            <td style="display:flex">
                                <button class="cart-button" style="margin-right:5px;" on:click={() => {addToCart(part); numParts(part, part.PartID);}}>
                                    +
                                </button>
                                <p id={part.PartID}>{numInCart(part)}</p>
                                <button class="cart-button" style="margin-left:5px;" on:click={() => {if(numInCart(part)>0){removeFromCart(part);} numParts(part, part.PartID);}}>
                                    -
                                </button>
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>
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
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        padding: 10px;
        border: 1px solid #ccc;
        text-align: left;
    }
    th{
        cursor: pointer;
    }
    .even {
        background-color: #f9f9f9;
    }
    .odd {
        background-color: #fff;
    }
    .cart-button {
        padding: 5px 10px;
    }
</style>