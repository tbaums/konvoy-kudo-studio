<style>
	main {
		position: relative;
		max-width: 56em;
		background-color: white;
		padding: 2em;
		margin: 0 auto;
		box-sizing: border-box;
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 1em;
	}

	#header {
		color: darkblue;
		grid-column: 1 / -1;
		grid-row: 1;
		text-align: center;
	}

	#actor_status {
		grid-column: 2;
		grid-row: 2;
	}

	#map {
		grid-column: 1;
		grid-row: 2;
		width: 100%;
		height: 30em;
		border: 1px solid darkblue;
		position: relative;
	}
</style>


<script>
	import Nav from '../components/Nav.svelte';
	import Map from '../components/Map.svelte';
	import ActorStatus from '../components/ActorStatus.svelte';

	export let segment;
</script>


<Nav {segment} />




<main>
	<div id="header">
		<h1>Factory Status</h1>
	</div>
	<Map />
	<ActorStatus />
	<slot></slot>
</main>