const logo = document.querySelector('.logo')
const nav = document.getElementById('nav')
const reducedMotion = window.matchMedia(`(prefers-reduced-motion: reduce)`).matches === true
let logoCooldown

// Click on the logo to go to the home page
logo.addEventListener('click', () => {
        window.location.href = '/'
})

// Make the logo accessible to keyboard navigation
logo.addEventListener('keypress', (event)=>{
    if (event.key === 'Enter') {
        window.location.href = '/'
    }
})

//
function highlightNavSelection() {
    let currentPage = document.title.split(' ')[0].toLowerCase()
    nav.querySelector('ul').querySelectorAll('li').forEach( li => {
        if (li.id === currentPage) {
            li.classList.add('selected')
        }
    })
}
window.addEventListener('DOMContentLoaded', highlightNavSelection)

// Disable the chance for the logo to spin if the user prefers reduced motion

if (!reducedMotion){
    $('.logo').mouseover(logoSpin)
}
async function logoSpin() {
    const duration = 600
    if (!logoCooldown && (Math.random()*100 < 3)){

        logoCooldown = true
        console.log('Spin')
        const animation = [
            {transform: "rotate(0) scale(1)"},
            {transform: "rotate(180deg) scale(0.5)", filter: 'blur(2px)'},
            {transform: "rotate(365deg) scale(1)"}
        ]
        logo.animate(animation, {
            easing: 'ease-in-out',
            duration: duration
        } )
        setTimeout(()=>logoCooldown=false, 10000)

    }
}

new IntersectionObserver(
  ([e]) => nav.classList.toggle('stuck', e.intersectionRatio < 1),
  { threshold: 1, rootMargin: '-0.05px 100px 100px 100px' }
).observe(nav);