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
    }
    
    img {
        width: 100%;
    }
    
    h2 {
        text-align: center;
    }
</style>

<div>
    <h2>Observe user's cursor in real-time</h2>
    <img {src} alt="Mesosphere homepage">
    <ul>{#each $dots as dot}
        <li>{dot}</li>
        { /each }
    </ul>

</div>