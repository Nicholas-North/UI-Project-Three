<script>
    import { getContext } from 'svelte';
  
    import NavBar from "../components/NavBar.svelte";
  
    const setActiveModule = getContext('setActiveModule');
    const setSelectedBook = getContext('setSelectedBook');
    
  
    const links = [
        { name: 'home', label: 'Home' },
        { name: 'search', label: 'Search' },
        { name: 'browse', label: 'Browse' },
        { name: 'catalog', label: 'Catalog' },
        { name: 'cart', label: 'Cart' }
    ];
  
    // Declare variables
    export let filteredParts = [];
  
    function handleBookClick(book) {
          setSelectedBook(book);
          setActiveModule('book');
    }
  </script>
  
  <main>
    <h1 class="head">&nbsp; Results</h1>
      <div class="scroll">
          {#each filteredParts as part}
              <div class="book-item">
                <p class="bigText">{part.name}</p>
                <p class="bigText">Price: {part.price}</p>
                <p class="bigText">Add to Cart</p>
                  <div class="book-details">

                  </div>
              </div>
          {/each}
      </div>
  </main>
  
  <style>
    .book-item {
        display: flex;
        align-items: center;
        padding: 2px;
        border: 1px solid black;
        border-radius: 8px;
    }
    .book-details {
        flex: 1;
        color: #6C584C;
        font-size: 22px;
    }
    .bigText{
      font-size: 20px;
    }
    .head{
      color: #6C584C;
      font-size: 30px;
    }
  </style>