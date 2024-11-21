<script>
  import { getContext } from 'svelte';
  import carModels from '../data/Car_Models.json';

  const addToCart = getContext('addToCart');
  const isInCart = getContext('isInCart');
  const numInCart = getContext('numInCart');
  const removeFromCart = getContext('removeFromCart');

  // Declare variables
  export let filteredParts = [];

  function numParts(part, id){
        document.getElementById(id).innerHTML = numInCart(part);
    }

</script>

<main>
  <h1 class="head">&nbsp; Results</h1>
  <div class="scroll">
      <table>
          <thead>
              <tr>
                  <th>Name</th>
                  <th>Price</th>
                  <th>Add to Cart</th>
              </tr>
          </thead>
          <tbody>
              {#each filteredParts as part}
                  <tr class="part-item">
                      <td class="bigText">{part.Name}</td>
                      <td class="bigText">${part.Price}</td>
                      <td style="display:flex">
                        <button class="cart-button" style="margin-right:5px;" on:click={() => {addToCart(part); numParts(part, part.PartID);}}>
                            +
                        </button>
                        <p id={part.PartID}>{numInCart(part)}</p>
                        <button class="cart-button" style="margin-left:5px;" on:click={() => {if(numInCart(part)>0){removeFromCart(part);} numParts(part, part.PartID);}}>
                            -
                        </button>
                      </td>
                  </tr>
              {/each}
          </tbody>
      </table>
  </div>
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
  .cartButton {
      padding: 5px 10px;
      border: none;
      background-color: #007bff;
      color: white;
      border-radius: 5px;
      cursor: pointer;
  }
  .cartButton:hover {
      background-color: #0056b3;
  }
</style>