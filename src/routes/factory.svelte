<script>
    import Map from '../components/Map.svelte';
    import ActorStatus from '../components/ActorStatus.svelte';
</script>

<style>
    #header {
        color: darkblue;
        grid-column: 1 / -1;
        grid-row: 1;
        text-align: center;
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
        border: 1px solid darkblue;
        position: relative;
    }
</style>

<div id="header">
    <h1>Factory Status</h1>
</div>
<Map />
<ActorStatus />