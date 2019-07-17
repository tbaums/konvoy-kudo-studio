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
        display: block;
        list-style-type: none;
        margin-bottom: .5em;
        text-align: left;
        border: 1px solid #aaa;
        border-radius: 2px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        padding-bottom: 0em;
        padding-left: 1em;
        
    }

    .actor_list__actor_name {
        font-weight: bold;
        display: block;
        padding-top: .5em;
        padding-bottom: .5em;
    }

    hr {
        border-top: 3px #333;
        color: #333;
        overflow: hidden;
        margin-top: 0;
    }

    .actor_list__actor_details * {
        padding-top: .5em;
        padding-bottom: .5em;
    }
    .actor_list__actor_coordinates {
        margin-right: auto;
    }

    .actor_list__actor_status {
        margin-right: .5em;
    }
</style>

<script>
    import { actors, map } from '../routes/stores.js'
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