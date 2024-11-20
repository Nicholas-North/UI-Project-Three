<script>
    import {onMount} from 'svelte';
    import {getContext} from 'svelte';
    import {setContext} from 'svelte';

    import logo from '../data/RockAuto.png';

    import Catalog from '../sections/Catalog.svelte';
    import Cart from '../sections/Cart.svelte';
    import PartSearch from '../sections/PartSearch.svelte';
    import ToolsAndParts from '../sections/ToolsAndParts.svelte';
    import Result from "../lib/Result.svelte";

    import NavBar from '../components/NavBar.svelte';

    export let parts = [];
    export let context = {};


    let links = [
        {name: 'Catalog', label: 'Part Catalog'},
        {name: 'PartSearch', label: 'Part Number Search'},
        {name: 'Cart', label: 'Cart'}
    ];

    let filteredParts = [];
    function setFilteredParts(part) {
        filteredParts = part;
    }
    // onMount(() => {
    //     setContext('setFilteredParts', setFilteredParts);
    // });

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
  
    setContext('addToCart', addToCart);
    setContext('removeFromCart', removeFromCart);
    setContext('isInCart', isInCart);
    setContext('setFilteredParts', setFilteredParts);
</script>

<main>
    <div class="banner">
        <img src={logo} alt="Logo" />
        <h2>ALL THE PARTS YOUR CAR WILL EVER NEED</h2>
    </div>
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
    .banner {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #3b3f8c; /* Purplish dark blue */
        padding: 20px;
        text-align: center;
        position: relative;
    }
    .banner img {
        max-width: 100px;
        position: absolute;
        left: 20px;
    }
    .banner h2 {
        font-size: 20px; /* Smaller font size */
        color: #fff; /* White text for better contrast */
        margin: 0 auto;
    }
    .content {
        border: 1px solid #ccc; /* Border color */
        border-radius: 10px; /* Rounded corners */
        padding: 20px; /* Padding inside the border */
        margin: 0 20px 20px 20px; /* Remove top margin, keep other margins */
        background-color: #f0f0f0; /* Slightly gray background color */
    }
</style>