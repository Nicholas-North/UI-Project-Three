<script>
    import {onMount, afterUpdate} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import Splash from '../modules/Splash.svelte';
    import VehicleParts from '../modules/VehicleParts.svelte';

    // let ActiveContext = {section: 'Catalog', context: 'splash'};
    // let ActiveContext = {section: 'Catalog', context: 'VehicleParts'};
    let ActiveContext = {}
    let selectedVechicle = 0;

    function setSelectedVehicle(vehicleID){
        selectedVechicle = parseInt(vehicleID);
        ActiveContext = {section: 'Catalog', context: 'VehicleParts'};
    }

    const getActiveContext = getContext('getActiveContext');

    afterUpdate(() => {
        ActiveContext = getActiveContext();
        console.log('ActiveContext:', ActiveContext.section);
    });

    setContext('setSelectedVehicle', setSelectedVehicle);
</script>

<main>
    {#if ActiveContext.context === 'splash'}
        <Splash />
    {/if}
    {#if ActiveContext.context === 'VehicleParts'}
        <VehicleParts VehicleID={selectedVechicle} />
    {/if}

</main>

<style>

</style>