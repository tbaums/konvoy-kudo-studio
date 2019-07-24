<style>
    .header {
        grid-column: 1 / -1;
        height: 40vh;
        margin-top: 5em;
    }
    
    .header h1 {
        font-size: 2.8em;
        text-transform: uppercase;
        font-weight: 700;
        margin: 0 0 0.5em 0;
        text-align: center;
        color: rgba(51, 0, 114, 1)
    }
    
    .header h2 {
        font-size: 1.4em;
        font-weight: 300;
        margin: 0 0 0.5em 0;
        text-align: center;
    }
    
    .cta {
        display: flex;
        grid-column: 1 / -1;
        grid-row: 2;
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
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
        -webkit-transform: rotateX(90deg);
        transform: rotateX(90deg);
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
    import {
        goto
    } from '@sapper/app';

    function handle_get_started_click(e) {
        goto(`iot`)
    }
</script>

<svelte:head>
    <title>Dashboard</title>
</svelte:head>

<div class="header">
    <h1>
        Konvoy + Kudo Studio
    </h1>
    <h2>
        Applied examples of stateful data services on Konvoy
    </h2>
</div>

<div class="cta">
    <button class="cta__button" on:click={handle_get_started_click}>
			Get Started
	</button>
</div>


<!-- <div class="text">
	<h3>Much benefits!</h3>
	<p>
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
		aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
		sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
	</p>
</div>

<div class="text">
	<h3>Such features!</h3>
	<p>
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
		aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
		sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
	</p>
</div> -->