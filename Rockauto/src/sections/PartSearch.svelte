<script>
    import { getContext } from 'svelte';
  
    import NavBar from "../components/NavBar.svelte";
  
    const setActiveContext = getContext('setActiveContext');
    const setFilteredParts = getContext('setFilteredParts');
  
    // Declare variables
    export let parts = [];
  
    let filteredParts = [];
  
  function Searching(parts) 
    {
      let input = document.getElementById('mySearch').value;
      console.log(input);
      for (let i = 0; i < parts.length; i++){
        if (parts[i]['PartID'] == input) {
          filteredParts.push(parts[i]);
          console.log('FOUND');
        }
      }
      /*
      let filter = input.toUpperCase();
      for (let i = 0; i < parts.length; i++){
        if (parts[i].name.toUpperCase().indexOf(filter) > -1) {
          filteredParts.push(parts[i]);
        }
      }
        */
      console.log(filteredParts);
      setFilteredParts(filteredParts);
      setActiveContext('Result', 'splash');
    }
  </script>
  
  <main>
    <h1 class="text">Search</h1>
      <input type="text" id="mySearch" placeholder="Search.." title="Type in a category">
      <button class="submit-button" id="SearchBtn" on:click={() => Searching(parts)}>Search</button>
  </main>
  
  <style>
    .text {
        color: #6C584C;
        font-size: 30px;
    }
    #mySearch{
      margin-left: 10px;
      width: 50%;
      font-size: 22px;
      padding: 11px;
      border: 1px solid #ddd;
    }
    .submit-button{
      background-color: gray;
      color: #f0ead2;
      margin-top: 5px;
      font-size: 22px;
      padding: 7px;
      border-radius: 10px;
    }
  </style>