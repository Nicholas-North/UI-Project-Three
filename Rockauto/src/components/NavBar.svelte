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
        width: 100%;
        background-color: #fff; /* White background */
        color: #6C584C;
        padding: 1rem 1rem 0 1rem; /* Remove bottom padding */
        font-size: 22px;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: flex;
        flex-wrap: wrap;
    }

    li {
        margin-right: 10px; /* Spacing between each button */
    }

    a {
        display: block;
        padding: 10px 15px;
        background-color: #f0f0f0; /* Slightly gray background */
        color: #6C584C;
        text-decoration: none;
        border-radius: 10px 10px 0 0; /* Rounded corners at the top */
        transition: background-color 0.3s;
    }

    a:hover {
        background-color: #d4d4d4; /* Slightly darker gray background on hover */
    }
</style>