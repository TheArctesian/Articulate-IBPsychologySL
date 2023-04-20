<script>
  import "../../app.css";
</script>

<div class="wrapper">
  <h1 class="font-bold text-2xl">Articulate Game-rules</h1>
  <br>
  <div class="text-left">
    <p>Setup: Set up 2-4 teams of two, pick a playing piece</p>
    <p>
      Starting position: Pick a tile as the starting tile, place pieces on that
      tile
    </p>
    <p>
      Winning condition: you make a full loop to return to the starting tile
    </p>
  </div>
  <br>
  <div class="text-left">
    <p>How a round goes down:</p>
    <li>
      The team whose round it is press the button corresponding to the tile
      they&rsquo;re on
    </li>
    <li>
      Like Heads-Up, one team member is given a prompt and must help the other
      team member guess what it is without using any nouns, verbs, or adjectives
      from the prompt.
    </li>
    <li>
      Who gets the prompt and who guesses alternates each time. The team has 1
      minute to guess as many prompts as possible.
    </li>
    <li>Skipping prompts is permitted.</li>
    <li>
      &ldquo;ERQ Question&rdquo; prompts do not need to be guessed
      word-for-word.
    </li>
    <li>
      Move the piece by the number of tiles equivalent to the number of prompts
      guessed correctly.
    </li>
    <br>
    <p class="text-center">Next team goes</p>
  </div>
  <div class="back">
    <a href="/" class="colors">Back to app</a>
  </div>
</div>

<style>
  .back {
    margin: auto;
    border-radius: 0.2rem;
    font-weight: bold;
    padding: 0.5rem;
    width: fit-content;
    transition: all ease-in-out 100ms;
  }
  .back:hover {
    color: var(--purple) !important;
    transition: all ease-in-out 100ms;
  }
  .donate {
    width: fit-content;
    padding: 1rem;
    background-color: var(--purple);
    color: white;
    inline-size: 80vw;
    overflow: auto;
    border-radius: 0.2rem;
  }
  a {
    color: var(--comment);
    transition: all ease-in-out 200ms;
  }
  .link {
    font-style: italic;
  }
  .link:hover {
    transition: all ease-in-out 200ms;
    font-style: normal;
  }
  @media (max-width: 750px) {
    a {
      font-size: 3.8vw;
    }
  }

  .projects {
    margin: auto;
    text-decoration: none;
    font-size: 5vw;
    transition: all ease-in-out 400ms;
    color: var(--purple);
  }

  :global(body) {
    background-color: var(--bg);
    font-family: "Fira Code", monospace;
    letter-spacing: 0.1em; /* Adjust as needed */
  }
  .wrapper {
    margin-left: 5vw;
    margin-right: 5vw;
    margin-top: 5vh;
    margin-bottom: 5vh;
    font-size: small;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    border-radius: 0.2rem;
    background-color: var(--fg);
  }
  .content {
    margin: 1rem;
    display: flex;
    justify-content: center;
    border-radius: 2rem;
  }
  .element {
    margin: 1rem;
    border-radius: 0.2rem;
    padding: 1rem;
    border: 0.2rem solid var(--fg);
  }
  .element:hover {
    border: 0.2rem solid var(--purple);
  }

  @media (max-width: 750px) {
    .element {
      margin: 0.6rem;
      border-radius: 0rem;
      padding: 0rem;

      border: 0.2rem solid var(--fg);
    }
  }
  .text {
    background-color: var(--fg);
    padding: 1rem;
    border-radius: 1rem;
  }
  img {
    transition: all ease-in-out 200ms;
    width: 7.5vw;
  }
  .s {
    padding: 1rem;
    margin: auto;
    width: 30vw;
  }
  .colors {
    color: var(--selection);
  }
</style>
