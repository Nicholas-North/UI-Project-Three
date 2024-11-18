<script>
    import {getContext} from 'svelte';
    export let links = [];

    let currentSection = '';

    const setActiveContext = getContext('setActiveContext');
    const getActiveContext = getContext('getActiveContext');

    $: currentSection = getActiveContext().section;
</script>

<nav>
    <ul>
        {#each links as link}
            <li><a href={`#${link.name}`} on:click={() => setActiveContext(link.name, 'splash')}>{link.label}</a></li>
        {/each}
    </ul>
  </nav>
  
  <style>
    nav {
      position: relative;
      top: 0;
      width: 93.9%;
      background-color: #6C584C;
      color: #f0ead2;
      padding: 1rem;
      font-size: 22px;
    }
  
    ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: flex-start;
    }
  
    li {
      display: inline;
    }
  
    a {
      color: #f0ead2;
      text-decoration: none;
      padding: 0.5rem 1rem;
    }
  
    a:hover {
      background-color: #352100;
    }
  </style>