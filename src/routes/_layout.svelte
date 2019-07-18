<style>
	main {
		position: relative;
		max-width: 56em;
		background-color: white;
		color: rgba(83,86,90,1);
		padding: 2em;
		margin: 0 auto;
		box-sizing: border-box;
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 1em;
	}

	/* .header  {
		grid-column: 1 / -1;
		grid-row: 1;
	}

	main .header h1 {
        font-size: 2.8em;
        text-transform: uppercase;
        font-weight: 700;
        margin: 0 0 0.5em 0;
        text-align: center;
        color: rgba(51,0,114,1)
    } */
</style>


<script>
	import Nav from '../components/Nav.svelte';
	export let segment;
</script>


<Nav {segment} />




<main>
	<slot></slot>
</main>