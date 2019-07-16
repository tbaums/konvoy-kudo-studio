<!-- TODO: Move all this to separate component -->
<style>
	/* TODO: Implement CSS grid */

	h1 {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 700;
		margin: 0 0 0.5em 0;
		text-align: center;
	}

	.actor {
		color: red;
		position: absolute;
	}

	#header {
		color: darkblue;
	}

	#map {
		width: 60%;
		height: 30em;
		border: 3px solid darkblue;
		position: relative;
	}

	#map>p {
		margin: 0;
		border: 0;
		padding: 0;
		line-height: 0;
	}

	p {
		margin: 1em auto;
	}

	@media (min-width: 480px) {
		h1 {
			font-size: 4em;
		}
	}
</style>

<svelte:head>
	<title>Sapper project template</title>
</svelte:head>


<script>
	import { actors, map } from './stores.js'
	let x, y
	$: actor_list = gen_actor_list()


	let messages = ''
	let data = []

	let prev_messages = ''
	let new_messages = ''


	// Prevennts an error when Svelte does SSR.
	if (process.browser) {
		let xhr = new XMLHttpRequest()
	}

	//need to create an array of actors because Svelte can't iterate over Map objects 
	function gen_actor_list() {
		let arr = [];
		for (let item of $map.keys()) {
			arr.push(item)
		}
		return arr
	}



	async function fetch_map(event) {
		let xhr = new XMLHttpRequest()
		xhr.responseType = 'text';
		// Change this to ENV variable with const x = process.env.X;
		xhr.open("GET", 'https://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/read?topic=actors')
		xhr.timeout = Infinity;
		xhr.onloadstart = function () {
			console.log("Download underway");
		};
		xhr.onprogress = function (event) {
			let response = xhr.response
			// trim the last message's trailing '::::' and split on '::::'
			new_messages = response.slice(prev_messages.length, response.length - 4).split('::::')
			prev_messages = response
			console.log('new_msgs')
			console.log(new_messages)
			data.push(new_messages)
			// set data = data to trigger view update
			data = data
			// set x and y coords
			console.log('data.slice(-1)')
			console.log(data.slice(-1))

			let data_point_array = data.slice(-1)

			//handle multiple data points sent in a single update
			if (data_point_array[data_point_array.length - 1].length > 1) {
				data_point_array = data.slice(-1).pop()
				console.log('data_point_array')
				console.log(data_point_array)
			} else {
				data_point_array = data.slice(-1)
			}

			let data_point = data_point_array[data_point_array.length - 1]
			console.log('data_point: ')
			console.log(data_point)
			data_point = JSON.parse(data_point)

			console.log(data_point)

			let actor = data_point.actor 
			x = data_point.x
			y = data_point.y
			console.log(x)
			console.log(y)
			console.log(actor)

			$map.set(actor, { 'x': x, 'y': y })

			//call gen_actor_list to update list of actors
			//TODO: confirm if this step is necessary
			actor_list = gen_actor_list()
			console.log(actor_list)
			console.log(gen_actor_list())
			console.log($map.get(actor))

		};
		xhr.send()
		xhr.onload = function () {
			//TODO: reconnect on completion
			console.log(xhr.response)
			
		}
	}

</script>



<div id="header">
	<h1>Factory Status</h1>
</div>


<div id="hero">
	<div id="map">
		{#each actor_list as actor}
			<p class='actor' id={actor} style="left: {$map.get(actor)['x']}%; bottom: {$map.get(actor)['y']}%;">{actor}</p>
		{/each}
	</div>
</div>


<button on:click={fetch_map}>
	Click me to start fetch
</button>