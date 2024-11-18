<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import SectionHandler from './SectionHandler.svelte';
    export let parts = [];

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
    <SectionHandler parts={parts} context={ActiveContext}/>
</main>

<style>

</style>