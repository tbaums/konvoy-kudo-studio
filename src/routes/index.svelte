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

	figure {
		margin: 0 0 1em 0;
	}

	img {
		width: 100%;
		max-width: 400px;
		margin: 0 0 1em 0;
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
	let messages = '';

	// Prevennts an error when Svelte does SSR.
	if (process.browser) {
		let xhr = new XMLHttpRequest()
	}
	
	async function handleClick(event) {
		let xhr = new XMLHttpRequest()
		xhr.responseType = 'text';
		console.log('got here - 1')
		console.log('got here - 2')
		// Change this to ENV variable with const x = process.env.X;
		xhr.open("GET", 'https://aa5075ebba40811e9a7850aec40aad68-946518783.us-west-2.elb.amazonaws.com/kafka-client-api/read?topic=topic56')
		console.log('got here - 3')
		xhr.timeout = Infinity;
		console.log('got here - 4')
		xhr.onloadstart = function () {
			console.log("Download underway");
			console.log(xhr.response)
		};
		console.log("passed onloadstart")
		xhr.onprogress = function (event) { // triggers periodically
			// event.loaded - how many bytes downloaded
			// event.lengthComputable = true if the server sent Content-Length header
			// event.total - total number of bytes (if lengthComputable)
			// console.log(`Received ${event.loaded} of ${event.total}`);
			console.log('inside onprogress')
			console.log(event)
			console.log(event.loaded)
			console.log(xhr.response)
			messages = xhr.response
		};
		console.log('got here - 5')
		xhr.send()
		console.log('got here - 6')
		xhr.onload = function () {
			console.log(xhr.response)
		}
	}

</script>

<button on:click={handleClick}>
	Click me to start fetch
</button>

<div id="hero">
	<div id="map" width=40%>
		{messages}
	</div>
</div>

{ @debug }