<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import carModels from '../data/Car_Models.json';

    import SectionHandler from './SectionHandler.svelte';
    export let parts = [];

    let ActiveContext = {section: 'Catalog', context: 'splash'};
    const makes = Array.from(new Set(carModels.map(car => car.Company)));
    const models = Array.from(new Set(carModels.map(car => car.Model)));
    const years = Array.from(new Set(carModels.map(car => car.Year)));

    function setActiveContext(section, context) {
        ActiveContext = {section, context};
    }
    function getActiveContext() {
        return ActiveContext;
    }

    function getMakes() {
        return makes;
    }

    function getModels() {
        return models;
    }

    function getYears() {
        return years;
    }

    setContext('getMakes', getMakes);
    setContext('getModels', getModels);
    setContext('getYears', getYears);

    setContext('setActiveContext', setActiveContext);
    setContext('getActiveContext', getActiveContext);
</script>

<main>
    <SectionHandler parts={parts} context={ActiveContext}/>
</main>

<style>

</style>