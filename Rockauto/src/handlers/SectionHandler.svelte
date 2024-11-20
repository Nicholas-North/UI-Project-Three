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

    let cartItems = [];
    function addToCart(part) {
        cartItems.push(part);
        console.log(part)
    }
    function removeFromCart(part) {
        cartItems.splice(cartItems.indexOf(part),1);
    }
    function isInCart(part) {
        return cartItems.indexOf(part) > -1;
    }

    setContext('setFilteredParts', setFilteredParts);
    setContext('addToCart', addToCart);
    setContext('removeFromCart', removeFromCart);
    setContext('isInCart', isInCart);
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
            <Cart cart={cartItems}/>
        {/if}
        {#if context.section === 'Result'}
            <Result filteredParts={filteredParts}/>
        {/if}
    </div>
</main>

<style>

</style>