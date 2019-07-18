<script>
    import Map from '../components/Map.svelte';
    import ActorStatus from '../components/ActorStatus.svelte';
</script>

<style>
    .header {
        grid-column: 1 / -1;
    }
    
    h1 {
        font-size: 2.8em;
        text-transform: uppercase;
        font-weight: 700;
        margin: 0 0 0.5em 0;
        text-align: center;
        color: rgba(51, 0, 114, 1)
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
        position: relative;
    }
</style>

<div class="header">
    <h1>Factory Status</h1>
</div>
<Map />
<ActorStatus />