<style>
	h1,
	figure,
	p {
		text-align: center;
		margin: 0 auto;
	}

	h1 {
		font-size: 2.8em;
		text-transform: uppercase;
		font-weight: 700;
		margin: 0 0 0.5em 0;
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
		border: 1px solid darkblue;
		position: relative;
	}

	#map > p {
		margin: 0;
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
	let messages = ''
	let data = []
	let prev_messages = ''
	let new_messages = ''
	let x = 0
	let y = 0

	// Prevennts an error when Svelte does SSR.
	if (process.browser) {
		let xhr = new XMLHttpRequest()
	}

	async function handleClick(event) {
		let xhr = new XMLHttpRequest()
		xhr.responseType = 'text';
		// Change this to ENV variable with const x = process.env.X;
		xhr.open("GET", 'https://ad51b5465a4a011e987c20aaf9c2019a-392664409.us-west-2.elb.amazonaws.com/kafka-client-api/read?topic=topic2-2')
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
			if (data_point_array[data_point_array.length -1].length > 1) {
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

			x = data_point.x
			y = data_point.y
			console.log(x)
			console.log(y)
		};
		xhr.send()
		xhr.onload = function () {
			console.log(xhr.response)
		}
	}

</script>



<div id="header">
	<h1>Factory Status</h1>
</div>


<div id="hero">
	<div id="map">
		<p class='actor' style="left: {x}%; bottom: {y}%;">A</p>
	</div>
</div>


<button on:click={handleClick}>
	Click me to start fetch
</button>

<p>{data}</p>