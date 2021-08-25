let overview = document.querySelector('#Overview-btn')
let map = document.querySelector('#Map-btn')

overview.addEventListener('click', overview_redirect)
map.addEventListener('click', map_redirect)

function overview_redirect() {
    window.location.replace('/overview')
}

function map_redirect() {
    window.location.replace('/map')
}