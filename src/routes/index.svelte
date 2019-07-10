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
	// import fetch from '@sapper/server'
	// async function handleClick(event) {
	// 	if (process.browser) {
	// 		// fetch('https://aed1ccf59a30411e9bf1c0aff5ab231b-1169908847.us-west-2.elb.amazonaws.com/svelte/blog')
	// 		await fetch('https://aed1ccf59a30411e9bf1c0aff5ab231b-1169908847.us-west-2.elb.amazonaws.com/kafka-client-api/read?topic=topic56')
	// 			.then(res => {
	// 				console.log(res.text())
	// 			})
	// 			.catch(error => console.error(error));
	// 	}
	// 	return "Fetching"
	// }

	let xhr = new XMLHttpRequest()
	xhr.responseType = 'text';
	$: data = xhr.response;

	async function handleClick(event) {
		console.log('got here - 1')
		let xhr = new XMLHttpRequest()
		console.log('got here - 2')
		xhr.open("GET", 'https://aed1ccf59a30411e9bf1c0aff5ab231b-1169908847.us-west-2.elb.amazonaws.com/kafka-client-api/read?topic=topic56')
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

{ @debug }