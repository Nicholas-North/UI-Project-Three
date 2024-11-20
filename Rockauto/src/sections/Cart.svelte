<script>
    import {getContext} from 'svelte';
    import App from '../App.svelte';

    const setActiveContext = getContext('setActiveContext');
    const removeFromCart = getContext('removeFromCart');

    export let cart = [];

    function clearCart() {
        // Create a copy of the cart array to avoid modifying it while iterating
        const cartCopy = [...cart];
        cartCopy.forEach((part, index) => {
            document.getElementById(part.Name + index).style.display = 'none';
            removeFromCart(part);
        });
    }

</script>

<main>
    <h1 class="head">Cart</h1>
    <div class="scroll">
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Remove?</th>
                </tr>
            </thead>
            <tbody>
                {#each cart as part, i}
                    <tr id={part.Name + i}>
                        <td>{part.Name}</td>
                        <td>${part.Price}</td>
                        <td>
                            <button class='X' on:click={() => {document.getElementById(part.Name + i).style.display="none"; removeFromCart(part);}}>&#x2718</button>
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
    <button class="bigText" on:click={() => {
        for(let i=cart.length - 1; i >= 0; i--){
            removeFromCart(cart[i]);
        }
        setActiveContext('Catalog', 'splash');
    }}>Purchase</button>
    <button class="bigText" on:click={clearCart}>Clear Cart</button>
</main>

<style>
    .scroll {
        overflow-x: auto;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        padding: 10px;
        border: 1px solid black;
        text-align: left;
    }
    th {
        background-color: #f0f0f0;
    }
    .bigText {
        font-size: 20px;
    }
    .head {
        color: #6C584C;
        font-size: 30px;
    }
    .X {
        font-size: 20px;
        color: red;
        border: none;
        background: none;
        cursor: pointer;
    }
</style>