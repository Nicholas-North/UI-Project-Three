<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import Splash from '../modules/Splash.svelte';
    import VehicleParts from '../modules/VehicleParts.svelte';

    // let ActiveContext = {section: 'Catalog', context: 'splash'};
    let ActiveContext = {section: 'Catalog', context: 'VehicleParts'};

    function setActiveContext(section, context) {
        ActiveContext = {section, context};
    }
    function getActiveContext() {
        return ActiveContext;
    }

    setContext('setActiveContext', setActiveContext);
    setContext('getActiveContext', getActiveContext);
</script>

<main>
    {#if ActiveContext.context === 'splash'}
        <Splash />
    {/if}
    {#if ActiveContext.context === 'VehicleParts'}
        <VehicleParts VehicleID=1 />
    {/if}

</main>

<style>

</style>