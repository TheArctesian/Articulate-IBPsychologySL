<script lang="ts">
  import Typewriter from "svelte-typewriter";
</script>

<div class="card margin-auto text-center flex-col">
  <div class="c flex flex-col justifty-between">
    <div class="cc">
      <h1 class="text-center m-auto text-2xl">
        <b class="text-3xl">Question: </b><br />
      </h1>
    </div>
    <div class="cc pee">
      <a class="but" href="/topics/bio">Biological</a>
      <a class="but" href="/topics/cog">Cognitive</a>
      <a class="but" href="/topics/soc">Sociocultural</a>
      <a class="but" href="/topics/abn">Abnormal</a>
      <a class="but" href="/topics/emt">Ethics, Methods and Techniques</a>
      <a class="but" href="/topics/erq">Random ERQ Question</a>
      <a class="but" href="/topics/rand">Random Question</a>
    </div>
    <div class="cc">
      <a href="/rules" class="text-l underline a">Rules</a>
    </div>
    <div class="cc">
      <a href="/about" class="text-l underline a">About this website</a>
    </div>
  </div>
</div>

<style>
  .pee {
    margin: 1rem;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    flex-direction: column;
    padding: 1rem;
    background-color: var(--purple);
    border: 1rem;
    border-radius: 0.2rem;
  }
  .but {
    margin: 0.2rem !important;
    padding: 1rem;
  }
  .a {
    color: var(--selection);
  }
  .cc {
    margin: 1rem;
  }
  .c {
    margin: auto;
    justify-content: space-between;
    background-color: var(--fg);
    padding: 1rem;
    border-radius: 0.2rem;
  }
  .but {
    margin: auto;
    padding: 1rem;
    border-radius: 0.2rem;
    color: white;
    background-color: var(--bg);
    transition: all ease-in-out 200ms;
  }
  .but:hover {
    transition: all ease-in-out 200ms;
  }
  .card {
    display: flex;
    height: 96vh;
    margin: 1rem;
    padding: 1rem;
    border-radius: 1rem;
  }
</style>
