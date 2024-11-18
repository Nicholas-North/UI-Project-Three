<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import Catalog from '../sections/Catalog.svelte';
    import Cart from '../sections/Cart.svelte';
    import PartSearch from '../sections/PartSearch.svelte';
    import ToolsAndParts from '../sections/ToolsAndParts.svelte';
    import Result from "../lib/Result.svelte";

    import NavBar from '../components/NavBar.svelte';

    export let parts = [];
    export let context = {};


    let links = [
        {name: 'Catalog', label: 'Catalog'},
        {name: 'PartSearch', label: 'Part # Search'},
        {name: 'ToolsAndMisc', label: 'Tools & Misc.'},
        {name: 'Cart', label: 'Cart'}
    ];

    let filteredParts = [];
    function setFilteredParts(part) {
        filteredParts = part;
    }

    setContext('setFilteredParts', setFilteredParts);
</script>

<main>
    <div class="header">
        <NavBar links={links} />
    </div>
    <div class="content">
        {#if context.section === 'Catalog'}
            <Catalog />
        {/if}
        {#if context.section === 'PartSearch'}
            <PartSearch parts={parts}/>
        {/if}
        {#if context.section === 'ToolsAndParts'}
            <ToolsAndParts />
        {/if}
        {#if context.section === 'Cart'}
            <Cart />
        {/if}
        {#if context.section === 'Result'}
            <Result filteredParts={filteredParts}/>
        {/if}
    </div>
</main>

<style>

</style>