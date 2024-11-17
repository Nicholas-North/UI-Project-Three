<script>
  import PageHandler from "./handlers/PageHandler.svelte";
</script>

<main>
  <PageHandler />
</main>

<style>
  .header {
    background-color: #DDE5B6;
    border-color: black;
    border-style: solid;
    text-align: center;
    padding: 20px;
    font-size: 22px;
  }

  .row {
    display: flex;
    height: 100vh;
  }
  .column {
    float: left;
    width: 33%;
    font-size: 22px;
    background-color: #DDE5B6;
    border-color: black;
    border-style: solid;
    overflow-y: scroll;
  }
</style>