<style>
    #actor_status {
        grid-column: 2 / 2;
        grid-row: 2;
    }

    li .actor_status {
        width: 100%;
        /* TODO: create nice cards for these */
    }


</style>

<script>
    import { actors, map } from '../routes/stores.js'
</script>

<div id="actor_status">
    <p>Actor Status:</p>
    <ul>
        {#each $actors as actor}
            <li class="actor_status">{actor} - x: {$map.get(actor)['x']}, y: {$map.get(actor)['y']}</li>
        {/each}
    </ul>
</div>