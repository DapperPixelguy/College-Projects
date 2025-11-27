const container = document.querySelector('.scrolling-picture')
let cooldown

function getScrollAmount() {
    const wrapper=container.querySelector('.wrapper')
    return wrapper.getBoundingClientRect().width
}

function scrollRight() {
    if (cooldown) return

    container.scrollBy({left: getScrollAmount(), behavior: "smooth"})

    cooldown = true
    setTimeout(()=> cooldown=false, 600)
}

function scrollLeftBtn() {
    if (cooldown) return

    container.scrollBy({left: -getScrollAmount(), behavior: "smooth"})
    cooldown = true
    setTimeout(()=> cooldown=false, 800)
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

photoScroller()