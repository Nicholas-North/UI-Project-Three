<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import Splash from '../modules/Splash.svelte';

    let ActiveContext = {section: 'Catalog', context: 'splash'};

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

</main>

<style>

</style>