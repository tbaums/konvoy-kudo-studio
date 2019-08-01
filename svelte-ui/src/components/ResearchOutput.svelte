<script>
    let src = 'homepage.png'
    import {
        dots
    } from '../routes/stores.js'

    // const obj = [{
    //     "x": "165",
    //     "y": "406"
    // }, {
    //     "x": "195",
    //     "y": "415"
    // }, {
    //     "x": "208",
    //     "y": "416"
    // }, {
    //     "x": "210",
    //     "y": "416"
    // }]
    // dots.set(obj)
</script>

<style>
    div {
        width: 100%;
        height: 100%;
        display: grid;
        /* grid-template-columns: 1fr 1fr; */
        grid-template-rows: repeat(2, min-content);
        grid-gap: 1em;
    }
    
    img {
        width: 100%;
    }
    
    h2 {
        text-align: center;
        grid-row: 2;
    }
    
    .dot {
        background-color: rgba(0, 0, 0, .9);
        color: rgba(255, 255, 255, 0);
        clip-path: circle(30%);
        position: absolute;
        z-index: 1;
        font-size: 1.2em;
    }
</style>
<div style="position: relative;">
    <h2>Observe user's cursor in real-time</h2>
    <span style="background-image: url({src})"></span>
    <!-- <img {src} alt="Mesosphere homepage"> -->
    <span class="dot" id={dot} style="top: {dot.y}px; left: {dot.x}px;">-</span> { /each }

</div>