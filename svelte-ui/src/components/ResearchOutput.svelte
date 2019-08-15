<script>
    let src = 'homepage.png'
    import {
        dots
    } from '../routes/stores.js'
</script>

<style>
    div {
        width: 100%;
        height: 100%;
        /* grid-template-columns: 1fr 1fr; */
    }
    
    img {
        width: 100%;
        box-shadow: .5rem .5rem .75rem -.5rem rgba(0, 0, 0, 0.2)
    }
    
    h2 {
        text-align: center;
        grid-row: 1;
    }
    
    .output_container {
        display: grid;
        grid-template-rows: repeat(2, min-content);
        grid-gap: 1em;
        position: relative;
    }
    
    #output_image {
        /* implemented as an id rather than class because there will only be one on the page */
        grid-row: 2;
    }
    
    .dot {
        background-color: rgba(0, 0, 0, .6);
        color: rgba(255, 255, 255, 0);
        clip-path: circle(30%);
        position: absolute;
        z-index: 1;
        font-size: 1.2em;
    }
</style>
<div class="output_container">
    <h2>Observe user's cursor in real-time</h2>
    <div id="output_image">
        <img {src} alt="Mesosphere homepage"> {#each $dots as dot}
        <span class="dot" style="left: {dot.x}px; top: {dot.y}px;">-</span> { /each }
    </div>


</div>