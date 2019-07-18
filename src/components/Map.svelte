<style>
    .actor {
        color: rgba(158, 36, 123, 1);
        position: absolute;
    }

    #map {
        grid-column: 1;
        grid-row: 2;
        width: 100%;
        /* VH of 72 seems to align well with 7 actors */
        height: 72vh;
        position: relative;
        border: 1px solid #aaa;
		border-radius: 2px;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }

    #map>p {
        margin: 0;
        border: 0;
        padding: 0;
        line-height: 0;
    }

    button {
        grid-row: 3;
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



<script>
    import { actors, map } from '../routes/stores.js'
    let x, y
    $: actor_list = gen_actor_list()



    let messages = ''
    let data = []

    let prev_messages = ''
    let new_messages = ''

    let current_host;


    // Prevennts an error when Svelte does SSR.
    if (process.browser) {
        let xhr = new XMLHttpRequest()
        current_host = window.location.host.toString();
        console.log('current host is: ', current_host)
    }

    //need to create an array of actors because Svelte can't iterate over Map objects
    function gen_actor_list() {
        // let arr = [];
        $actors = []
        for (let item of $map.keys()) {
            $actors.push(item)
        }
        return $actors
    }

    function process_map_data(data_point_array) {
        let data_point;
        //handle multiple data points sent in a single update
        if (data_point_array[data_point_array.length - 1].length > 1) {
            data_point_array = data.slice(-1)
            //console.log("data_point_array is: ")
            //console.log(data_point_array)
            data_point_array.forEach(function (item, index) {
                item.forEach(function (sub_item, index) {
                    //console.log(sub_item, index);
                    process_data_point(sub_item)
                })
            })

            //console.log('data_point_array - if')
            //console.log(data_point_array)
        } else {
            data_point_array = data.slice(-1)
            process_data_point(data_point_array)
            //console.log('data_point_array - else')
            //console.log(data_point_array)
        }

        function process_data_point(data_point) {
            // let data_point = data_point_array[data_point_array.length - 1]
            //console.log('data_point: ')
            //console.log(data_point)
            try {
                data_point = JSON.parse(data_point)
            }
            catch (error) {
                //console.error(error)
                return
            }

            //console.log("parsed data_point")
            //console.log(data_point)

            let actor = data_point.actor
            if (data_point.x <= 0) {
                x = 0
            } else if (data_point.x >= 90) {
                x = 90
            } else {
                x = data_point.x
            }

            if (data_point.y <= 5) {
                y = 5
            } else if (data_point.y >= 95) {
                y = 95
            } else {
                y = data_point.y
            }
            //console.log(x)
            //console.log(y)
            //console.log(actor)

            $map.set(actor, { 'x': x, 'y': y })
        }
    }



    async function fetch_map(event) {
        let xhr = new XMLHttpRequest()
        xhr.responseType = 'text';
        let url = 'https://' + current_host + '/kafka-client-api/read?topic=actors'
        console.log("url is: ", url)
        xhr.open("GET", url)
        xhr.timeout = Infinity;
        xhr.onloadstart = function () {
            //console.log("Download underway");
        };
        xhr.onprogress = function (event) {
            let response = xhr.response
            // trim the last message's trailing '::::' and split on '::::'
            new_messages = response.slice(prev_messages.length, response.length - 4).split('::::')
            prev_messages = response
            //console.log('new_msgs')
            //console.log(new_messages)
            data.push(new_messages)
            // set data = data to trigger view update, keeping only last 100 messages in order to prevent browser from getting bogged down.
            if (data.length >= 100) {
                data = data.splice(-100, data.length)
            } else {
                data = data
            }
            // set x and y coords
            //console.log('data.slice(-1)')
            //console.log(data.slice(-1))

            process_map_data(data.slice(-1))
            // let data_point_array = data.slice(-1)
            //call gen_actor_list to update list of actors
            //TODO: confirm if this step is necessary, given it's defined as reactive above-- $: actor_list = gen_actor_list()
            actor_list = gen_actor_list()
        };
        xhr.send()
        xhr.onload = function () {
            //TODO: reconnect on completion
            //console.log(xhr.response)
        }
    }

</script>


<div id="map">
    {#each actor_list as actor}
        <p class='actor' id={actor} style="left: {$map.get(actor)['x']}%; bottom: {$map.get(actor)['y']}%;">🤖{actor}</p>
    {/each}

</div>

<button on:click={fetch_map}>
        Click me to start fetch
</button>