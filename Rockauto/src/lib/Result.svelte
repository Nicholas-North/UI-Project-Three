<script>
    import { getContext } from 'svelte';
  
    const addToCart = getContext('addToCart');
    const isInCart = getContext('isInCart');
  
    // Declare variables
    export let filteredParts = [];
  
  </script>
  
  <main>
    <h1 class="head">&nbsp; Results</h1>
      <div class="scroll">
          {#each filteredParts as part}
              <div class="part-item">
                <p class="bigText">{part.Name} Price: ${part.Price}</p>
                <button class="cartButton" on:click={() => {addToCart(part);}}>Add to Cart</button>
              </div>
              
          {/each}
      </div>
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
    .cartButton{
      font-size: 18px;
      float:right;
    }
  </style>