const container = document.querySelector('.scrolling-picture')
const carousel = document.querySelector('.carousel-wrapper')
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


    paths.forEach(image => {
        let wrapper = document.createElement('div')
        wrapper.classList.add('wrapper')
        let img = document.createElement('img')
        img.src=image
        wrapper.appendChild(img)
        container.appendChild(wrapper)
    })
}

document.addEventListener('DOMContentLoaded', photoScroller)