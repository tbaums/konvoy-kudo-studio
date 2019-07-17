<style>
    #actor_status {
        grid-column: 2 / 2;
        grid-row: 2;
        overflow: hidden;
        padding: 0;
        margin: 0;
    }

    #actor_status ul {
        /* Remove indentation for list items */
        padding: 0;
    }

    #actor_list {
        padding: 0;
        margin-top: 0;
    }

    .actor_list__item {
        /* width: 100%; */
        display: block;
        list-style-type: none;
        margin-bottom: .5em;
        /* margin-top: .5em; */
        text-align: left;
        border: 1px solid #aaa;
        border-radius: 2px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        padding-bottom: 0em;
        /* padding-top: 1em; */
        padding-left: 1em;
        
    }

    .actor_list__actor_name {
        font-weight: bold;
        display: block;
        padding-top: .5em;
        padding-bottom: .5em;
    }

    hr {
        /* border: none; */
        border-top: 3px #333;
        color: #333;
        overflow: hidden;
        margin-top: 0;
        /* text-align: center; */
        /* height: 5px; */

    }

    /* hr:after {
        background: #fff;
        padding: 0 4px;
        position: relative;
        top: -13px;
    } */

    .actor_list__actor_details * {
        padding-top: .5em;
        padding-bottom: .5em;
    }
    .actor_list__actor_coordinates {
        /* padding-top: .5em;
        padding-bottom: .5em; */
        margin-right: auto;
    }

    .actor_list__actor_status {
        /* display: inline; */
        margin-right: .5em;
    }
</style>

<script>
    import { actors, map } from '../routes/stores.js'

    $map.set('actor1', { 'x': 12, 'y': 15 })
    $map.set('actor2', { 'x': 42, 'y': 45 })
    $actors.push('actor1')
    $actors.push('actor2')
</script>

<div id="actor_status">
    <ul id="actor_list">
        {#each $actors as actor}
            <li class="actor_list__item">
                <span class="actor_list__actor_name">
                    {actor} 
                </span>
                <hr />
                <div class="actor_list__actor_details" style="display: flex;">
                    <span class="actor_list__actor_coordinates">
                        x: {$map.get(actor)['x']}, y: {$map.get(actor)['y']}
                    </span>
                    <span class="actor_list__actor_status">
                        Status: <span style="color: green;">OK</span>
                    </span>
                </div>
            </li>
        {/each}
    </ul>
</div>