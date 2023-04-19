<script>
    import "../../app.css";
</script>

<div class="wrapper">
    <h1 class="text-center ">
        Hello I made this website for psyc class you can find out who I am at my
        website <a href="https://www.danielokita.com" class="underline link"
            >danielokita.com</a
        >
        or find me on these places:
    </h1>
    <div class="text-center ">
        <div class="content">
            <div class="element">
                <a href="https://www.linkedin.com/in/stephen-okita-a9427b1b2/">
                    <img src="https://simpleicons.org/icons/linkedin.svg" />
                </a>
            </div>
            <div class="element">
                <a href="https://mastodon.world/@thearctesian">
                    <img src="https://simpleicons.org/icons/mastodon.svg" />
                </a>
            </div>
            <div class="element">
                <a href="https://github.com/TheArctesian">
                    <img src="https://simpleicons.org/icons/github.svg" />
                </a>
            </div>
            <div class="element">
                <a href="https://discord.com/users/682753580943278083">
                    <img src="https://simpleicons.org/icons/discord.svg" />
                </a>
            </div>
        </div>
        <h1>
            the source code for this website can be found<a
                class="s"
                href="https://github.com/TheArctesian/TableQuestions.net"
            >here</a>
        </h1>
        <h1>
            If you would like to donate to me you can find my eth links bellow
        </h1>
        <br />
        <div class="donate flex flex-col">
            <h1><b>Eth: </b>`0xc7AfE4114E3b78cB22Ec7EbDA11AD40199a9Cb96`</h1>
            <h1>
                <b
                    >Cardano:
                </b>`addr1q85kef4y4zx4lyxyuq3wgec3nddn53wv6nmydrc6eyx5l47jdatz0hja95dudtxclcjp8ejkthl6hl5xjfregk9lllrs8um6c0`
            </h1>
        </div>
        <div>
            <a href="https://ko-fi.com/N4N5ILAUX" target="_blank"
                ><img
                    class="flex w-full s"
                    src="https://storage.ko-fi.com/cdn/kofi3.png?v=3"
                    alt="Buy Me a Coffee at ko-fi.com"
                /></a
            >
        </div>
        <div class="back">
            <a href="/" class="colors">Back to app</a>
        </div>
    </div>
</div>

<style>
    
    .back{
        margin:auto;
        border-radius: 0.2rem;
        font-weight: bold;
        padding: .5rem;
        width: fit-content;
        transition: all ease-in-out 100ms;
    }
    .back:hover{
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
        height: 90vh;
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
.colors{
        color: var(--selection);
    }
</style>
