<style>
    main {
        position: relative;
        max-width: 56em;
        background-color: white;
        color: rgba(83, 86, 90, 1);
        padding: 2em;
        margin: 0 auto;
        box-sizing: border-box;
        display: grid;
        grid-template-columns: 1fr 1fr;
        /* grid-template-rows: repeat(4, min-content); */
        grid-gap: 1em;
    }
    
    button,
    button:link,
    button:visited {
        text-transform: uppercase;
        text-decoration: none;
        padding: 1.5rem 1.5rem;
        /* display: inline-block; */
        border-radius: 3rem;
        -webkit-transition: all 0.2s;
        transition: all 0.2s;
        position: relative;
        font-size: 150%;
        border: 1px solid rgba(51, 0, 114, 1);
        cursor: pointer;
        margin: auto;
        color: rgba(51, 0, 114, 1);
    }
    
    button:hover,
    button:link:hover,
    button:visited:hover {
        -webkit-transform: translateY(-3px);
        transform: translateY(-3px);
        -webkit-box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.2);
        box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.2)
    }
    
    button:hover::after,
    button:link:hover::after,
    button:visited:hover::after {
        -webkit-transform: scaleX(1.4) scaleY(1.6);
        transform: scaleX(1.4) scaleY(1.6);
        opacity: 0
    }
    
    button:active,
    button:focus,
    button:link:active,
    button:link:focus,
    button:visited:active,
    button:visited:focus {
        outline: none;
        -webkit-transform: translateY(-1px);
        transform: translateY(-1px);
        -webkit-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2)
    }
    
    button::after {
        content: "";
        display: inline-block;
        height: 100%;
        width: 100%;
        border-radius: 10rem;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -1;
        -webkit-transition: all 0.4s;
        transition: all 0.4s
    }
</style>


<script>
    import Nav from '../components/Nav.svelte';
    export let segment;
</script>


<Nav {segment} />




<main>
    <slot></slot>
</main>