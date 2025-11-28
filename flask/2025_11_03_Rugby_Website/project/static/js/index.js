const container = document.querySelector('.scrolling-picture')
const carousel = document.querySelector('.carousel-wrapper')
const blur = document.querySelector('.blur')
const blownUp = document.querySelector('.blow-up')
let cooldown

function getScrollAmount() {
    const wrapper=container.querySelector('.wrapper')
    return wrapper.getBoundingClientRect().width
}

function scrollRight() {
    if (cooldown) return

    if (container.scrollLeft + container.clientWidth >= container.scrollWidth){
        container.scrollTo({left: 0, behavior:'smooth'})
    } else {
        container.scrollBy({left: getScrollAmount(), behavior: "smooth"})
    }

    cooldown = true
    setTimeout(()=> cooldown=false, 600)
}

function scrollLeftBtn() {
    if (cooldown) return

    if (container.scrollLeft === 0){
        container.scrollTo({left: container.scrollWidth, behavior:'smooth'})
    } else {

        container.scrollBy({left: -getScrollAmount(), behavior: "smooth"})
    }
    cooldown = true
    setTimeout(()=> cooldown=false, 600)
}

async function photoScroller() {
    let response = await fetch('/photo-fetch')
    let paths = await response.json()
    let placeholder = 'static/Placeholder_view_vector.svg'


    paths.forEach(image => {
        let wrapper = document.createElement('div')
        wrapper.classList.add('wrapper')
        let img = document.createElement('img')
        img.src=placeholder

        // Have photos change from placeholders once loaded
        let real = new Image()
        real.src = image
        real.onload = () => {
            img.src=image
        }

        wrapper.appendChild(img)
        container.appendChild(wrapper)

        img.addEventListener('click', function () {
            blowUp(this)
        })
    })
}

function blowUp(elem) {

    function closeHandler(e) {
        if (e.target === blur) {
            blur.style.display = 'none'
            blownUp.style.display = 'none'
            blownUp.classList.remove('no-doc-scroll')
            document.removeEventListener('click', closeHandler)
        }
    }

    blownUp.src = elem.src
    console.log(elem.src)

    blur.style.display = 'block'
    blownUp.style.display = 'block'
    blownUp.classList.add('no-doc-scroll')

    document.addEventListener('click', closeHandler)
}

document.addEventListener('DOMContentLoaded', photoScroller)