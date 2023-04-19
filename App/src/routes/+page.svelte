<script lang="ts">
  import Typewriter from "svelte-typewriter";
  import questions from "./questionbank.json";
  let pickedTopic: boolean = false;
  let Topics: string[] = ["Cog", "Bio", "Soc", "Abn", "Abn", "EMT", "ERQ"];
  let askedQuestion: string[] = [];
  let questionLength: number;
  let Topic: string = []
  let question: string = "Press the button to get a questions";
  function setTopic(){
    pickedTopic = true
  }
  function genRandomQuestion() {
    questionLength = questions.length;
    try {
      let num = Math.floor(Math.random() * questionLength);
      question = questions[num].Question;
      questions.splice(num, 1);
    } catch (error) {
      question = "you have exhausted all the questions, refresh the tab";
    }
    // delete question[num];
  }
</script>

<div class="card margin-auto text-center flex-col">
  {#if pickedTopic == false}
    <div class="c flex flex-col justifty-between">
      <div class="cc">
        <h1 class="text-center m-auto text-2xl">
          <b class="text-3xl">Question: </b><br />
        </h1>
      </div>
      <div class="cc">
        {#each Topics as t }
           <button class="flex-row m-5" on:click={setTopic}>
            {t}
           </button> 
        {/each}
      </div>
      <div class="cc">
        <button class="but" on:click={genRandomQuestion}>Skip</button>
      </div>
      <div class="cc">
        <a href="/about" class="text-l underline a">About this website</a>
      </div>
    </div>
  {:else}
    <div class="c flex flex-col justifty-between">
      <div class="cc">
        <h1 class="text-center m-auto text-2xl">
          <b class="text-3xl">Question: </b><br />
        </h1>
      </div>
      <h1 class="text-center m-auto text-2xl">
        <b class="text-3xl">Time Remaining </b><br />
      </h1>
    </div>
  {/if}
</div>

<style>
    .but{
        background-color: var(--red);
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
