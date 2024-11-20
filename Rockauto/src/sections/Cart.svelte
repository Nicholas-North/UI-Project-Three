<script>
    import {getContext} from 'svelte';
    import App from '../App.svelte';

    const setActiveContext = getContext('setActiveContext');
    const removeFromCart = getContext('removeFromCart');

    export let cart = [];

</script>

<main>
    <h1 class="head">&nbsp; Cart</h1>
    <div class="scroll">
        {#each cart as part, i}
            <div class="container" id={part.Name + i} style="display:flex;">
                <div class="part-item">
                <p class="bigText">{part.Name} Price: ${part.Price}</p>
                <button class='X' on:click={() => {document.getElementById(part.Name + i).style.display="none"; removeFromCart(part);}}>&#x2718</button>
                </div>
            </div>
        {/each}
    </div>
    <button class="bigText" on:click={() => {
        for(let i=cart.length; i>0; i--){
            removeFromCart(cart[i]);
        }
        setActiveContext('Catalog', 'splash');
    }}>Purchase</button>
    <button class="bigText" on:click={() => {
        let j = 0;
        for(let i=cart.length-1; i>=0; i--){
            console.log(typeof(cart[i]));
            console.log(cart[i]['Name']);
            document.getElementById(cart[i]['Name']+j).style.display='none';
            removeFromCart(cart[i]);
            j++;
        }
    }}>Clear Cart</button>

</main>

<style>
    .part-item {
        display: flex;
        align-items: center;
        padding: 2px;
        border: 1px solid black;
        border-radius: 8px;
    }
    .bigText{
      font-size: 20px;
    }
    .head{
      color: #6C584C;
      font-size: 30px;
    }
    .X{
        font-size:20px;
        color:red;
    }
</style>