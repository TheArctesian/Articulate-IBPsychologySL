<script lang="ts">
  import questions from "./cog.json";
  import Typewriter from "svelte-typewriter";
  import "../../../app.css";

  let askedQuestion: string[] = [];
  let questionLength: number;
  let question: string = "Press the button to get a questions";
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
  <div class="c flex flex-col justifty-between">
    <div class="cc">
      <h1 class="text-center m-auto text-2xl">
        <b class="text-3xl">Cognitive Question: </b><br />
      </h1>
    </div>
    <div class="cc green">
      <Typewriter interval="5">
        <h1>{question}</h1>
      </Typewriter>
    </div>
    <div class="cc">
      <button class="but" on:click={genRandomQuestion}
        >Get a new question</button
      >
    </div>
    <div class="cc">
      <a href="/" class="colors">Back to app</a>
    </div>
  </div>
</div>

<style>
.green{
    background-color: var(--red);
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
