<style>
    div {
        width: 100%;
        height: 100%;
    }
    
    img {
        width: 100%;
        box-shadow: .5rem .5rem .75rem -.5rem rgba(0, 0, 0, 0.2)
    }
    
    h2 {
        text-align: center;
    }
    
    .input_container {
        display: grid;
        grid-template-rows: repeat(3, min-content);
        grid-gap: 1em;
        position: relative;
    }
    
    #input_image {
        /* implemented as an id rather than class because there will only be one on the page */
        grid-row: 2;
    }
</style>

<script>
    let src = 'homepage.png'
    let m = {
        x: 0,
        y: 0
    };

    let current_host;

    // Prevennts an error when Svelte does SSR.
    if (process.browser) {
        let xhr = new XMLHttpRequest()
        current_host = window.location.host.toString();
        console.log('current host is: ', current_host)
    }

    function handleMousemove(event) {
        m.x = event.clientX;
        m.y = event.clientY;
        post_cursor_coordinates()
    }

    // post_cursor_coordinates remains synchronous in order to preserve the order of POST requests to
    // the kafka-client-api
    function post_cursor_coordinates() {
        let xhr = new XMLHttpRequest()
        let url = 'https://' + current_host + '/kafka-client-api/write?topic=research&payload={"x":"' +
            m.x +
            '","y":"' +
            m.y +
            '"}&repetitions=1'
            // console.log("url is: ", url)
        xhr.open("POST", url)
        xhr.send()
    }
</script>


<div class="input_container">
    <h2>Move mouse around page</h2>
    <div id="input_image" on:mousemove={handleMousemove}>
        <img {src} alt="Mesosphere homepage">
    </div>
    <div>The mouse position is {m.x} x {m.y}</div>
</div>