<script>
  import { getContext } from 'svelte';
  import carModels from '../data/Car_Models.json';

  const addToCart = getContext('addToCart');
  const isInCart = getContext('isInCart');

  // Declare variables
  export let filteredParts = [];

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
                      <td>
                          <button class="cartButton" on:click={() => {addToCart(part);}}>
                              {isInCart(part) ? 'Remove from Cart' : 'Add to Cart'}
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