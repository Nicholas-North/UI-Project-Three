<script>
    import { onMount } from 'svelte';
    import { getContext } from 'svelte';
    import carModels from '../data/Car_Models.json';

    let makes = [];
    let models = [];
    let years = [];
    let selectedMake = '';
    let selectedModel = '';
    let selectedModels = [];
    let selectedYear = '';
    let selectedYears = [];
    let vehicleID = '';

    const getMakes = getContext('getMakes');
    const getModels = getContext('getModels');
    const getYears = getContext('getYears');

    onMount(() => {
        makes = getMakes();
        models = getModels();
        years = getYears();
    });

    function filterModelsByMake(make) {
        return carModels.filter(car => car.Company === make);
    }

    function filterYearsByMakeAndModel(make, model) {
        return carModels.filter(car => car.Company === make && car.Model === model);
    }

    function getVehicleID(make, model, year) {
        const vehicle = carModels.find(car => car.Company === make && car.Model === model && car.Year === year);
        return vehicle ? vehicle.VehicleID : '';
    }

    $: if (selectedMake) {
        selectedModels = Array.from(new Set(filterModelsByMake(selectedMake)));
    }

    $: if (selectedMake && selectedModel) {
        selectedYears = Array.from(new Set(filterYearsByMakeAndModel(selectedMake, selectedModel)));
    }

    $: if (selectedMake && selectedModel && selectedYear) {
        vehicleID = getVehicleID(selectedMake, selectedModel, selectedYear);
    }
</script>

<main>
    <label for="make">Make:</label>
    <select id="make" bind:value={selectedMake}>
        <option value="">Select a make</option>
        {#each makes as make}
            <option value={make}>{make}</option>
        {/each}
    </select>

    {#if selectedMake}
        <label for="model">Model:</label>
        <select id="model" bind:value={selectedModel}>
            <option value="">Select a model</option>
            {#each filterModelsByMake(selectedMake) as model}
                <option value={model.Model}>{model.Model}</option>
            {/each}
        </select>
    {/if}

    {#if selectedMake && selectedModel}
        <label for="year">Year:</label>
        <select id="year" bind:value={selectedYear}>
            <option value="">Select a year</option>
            {#each filterYearsByMakeAndModel(selectedMake, selectedModel) as year}
                <option value={year.Year}>{year.Year}</option>
            {/each}
        </select>
    {/if}

    {#if selectedMake && selectedModel && selectedYear}
        <p>Vehicle ID: {vehicleID}</p>
    {/if}
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    label {
        margin-top: 1rem;
    }
</style>