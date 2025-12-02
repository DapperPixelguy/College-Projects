let accessLevel = window.ACCESS_LEVEL
const blur = document.querySelector('.blur')
const popup = document.querySelector('.score-enter-wrapper')
let score_debounce
const submitbutton = document.getElementById('submit')
let isAuthenticated = window.IS_AUTHENTICATED

// Function to validate, and submit scores to createResult

function submit_scores(elem){
    let team1_input = popup.querySelector('#team1').value
    let team2_input = popup.querySelector('#team2').value

    popup.querySelector('#team1').value = ''
    popup.querySelector('#team2').value = ''

    if (parseInt(team1_input) >= 0 && parseInt(team2_input) >= 0) {
        elem.removeEventListener('click', elem.score_toggle_handler)

        score_toggle()
        createResult(elem, team1_input, team2_input)
    }
}

// Function to check if an outside click is detected, so score enter can be closed

function outsideClickHandler(event) {
    if (popup.contains(event.target)) return

    score_toggle()
}

// Function to toggle the score entry box

function score_toggle(elem) {
    if (accessLevel < 2) {
        return
    }

    if (elem) {
        submitbutton.onclick = () => submit_scores(elem)
    }
    if (score_debounce){
        return
    }

    score_debounce = true
    setTimeout(()=>{
        score_debounce = false
    }, 300)

    const visible = getComputedStyle(popup).display !== 'none'

    const keyframes = visible
    ? [{opacity: 1}, {opacity: 0}]
    : [{opacity: 0}, {opacity: 1}]

    console.log(elem)
    popup.animate(keyframes, {duration: 200})
    blur.animate(keyframes, {duration: 200})

    if (!visible){
        popup.classList.add('no-doc-scroll')
        blur.style.display = 'block'
        popup.style.display = 'block'

        document.getElementById('team1-label').textContent=
            `${elem.querySelector('.team1').querySelector('h4').textContent}`

        document.getElementById('team2-label').textContent=
            `${elem.querySelector('.team2').querySelector('h4').textContent}`

        if (elem.classList.contains('result')){
            let scores = elem.querySelector('.middle').textContent.split('-')
            let score1 = parseInt(scores[0])
            let score2 = parseInt(scores[1])

            document.getElementById('team1').value=score1
            document.getElementById('team2').value=score2
        }

        window.addEventListener('click', outsideClickHandler)
    }

    if (visible) {
        popup.classList.remove('no-doc-scroll')
        setTimeout(()=>{
            popup.style.display = 'none'
            blur.style.display = 'none'
        }, 200)
        window.removeEventListener('click',outsideClickHandler)
    }
}

async function createResult(elem, team1_score, team2_score) {

    if (!isAuthenticated) {
        return
    }

    if (parseInt(accessLevel) < 2) {
    return;
    }

    const id = elem.dataset.fixtureId
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

    const res = await fetch('/fixtures/create-result', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken},
        body: JSON.stringify({
            'id': id,
            'team1_score': team1_score,
            'team2_score': team2_score
        })
    })

    f = await res.json()

    console.log(f)

    let info = elem.querySelector('.fixture-info')
    let fixture = elem.querySelector('.fixture')
    info.innerHTML = `
            <p style="justify-self: end">${f.date}</p>
            <p>Concluded</p>
            <p>${f.venue}</p>
            `;

            fixture.innerHTML =
            `<div class="team1">
                <h4 class="barlow-condensed">${f.team1.name}</h4>
                <img class="team1-logo" src="static/Placeholder_view_vector.svg">
            </div>

            <p class="middle barlow-condensed" style="justify-self: center">${f.team1.score} - ${f.team2.score}</p>

            <div class="team2">
                <img class="team2-logo" src="static/Placeholder_view_vector.svg">
                <h4 class="barlow-condensed" style="justify-self: end">${f.team2.name}</h4>
            </div>`

    data = await res
    console.log(data)

    loadLogo(f.team1.logo, fixture.querySelector('.team1-logo'))
    loadLogo(f.team2.logo, fixture.querySelector('.team2-logo'))

    elem.classList.add('result')
}
function loadLogo(url, element) {
        let img = new Image()
        img.src=url
        img.onload = () => {
            element.src = url
        }
}

async function buildFixtures() {
    const animKey = 'animationLastPlayed'
    const cooldown = 5 * 60 * 1000
    const lastPlayed = parseInt(localStorage.getItem(animKey)) || 0
    const now = Date.now()
    let playAnim

    if (now - lastPlayed < cooldown) {
        playAnim = false
    } else {
        playAnim = true
        localStorage.setItem(animKey, now)
    }
    const response = await fetch('/fixtures/fetch')
    const fixtures = await response.json()
    const container = document.querySelector('.fixture-container')
    const reducedMotion = window.matchMedia(`(prefers-reduced-motion: reduce)`).matches === true
    let animTime = 0.3

    fixtures.forEach((f) => {
        const wrapper = document.createElement('div');
        let isResult = !!f.result
        wrapper.classList.add('fixture-wrapper');
        wrapper.dataset.fixtureId = f.id

        if (!f.result){
            return
        }

        let date = new Date(f.date)

        date=date.toLocaleDateString("en-GB")

        if (accessLevel >= 2){
            wrapper.style.cursor = 'pointer'
        }

        if (!reducedMotion && playAnim) {
            setTimeout(() => {
                wrapper.classList.add('show')
                setTimeout(() => {
                    wrapper.style.transition = 'transform 0.2s'
                }, 600)
            }, animTime * 350)
        } else {
            wrapper.classList.add(`show`)
        }

        const info = document.createElement('div');
        info.classList.add('fixture-info', 'barlow-condensed');
        info.innerHTML = `
            <p style="justify-self: end">${date}</p>
            <p>${f.time}</p>
            <p>${f.venue}</p>
        `;

        const fixture = document.createElement('div');
        wrapper.score_toggle_handler = () => score_toggle(wrapper)
        wrapper.addEventListener('click', wrapper.score_toggle_handler)
        fixture.classList.add('fixture');
        if (!isResult) {
            fixture.innerHTML = ``
        } else if (isResult) {
            info.innerHTML = `
            <p style="justify-self: end">${f.date}</p>
            <p>Concluded</p>
            <p>${f.venue}</p>
            `;

            fixture.innerHTML =
            `<div class="team1">
                <h4 class="barlow-condensed">${f.team1.name}</h4>
                <img class="team1-logo" src="static/Placeholder_view_vector.svg">
            </div>

            <p class="middle barlow-condensed" style="justify-self: center">${f.result.team1} - ${f.result.team2}</p>

            <div class="team2">
                <img class="team2-logo" src="static/Placeholder_view_vector.svg">
                <h4 class="barlow-condensed" style="justify-self: end">${f.team2.name}</h4>
            </div>`
            wrapper.classList.add('result')
        }
        wrapper.appendChild(info);
        wrapper.appendChild(fixture);
        container.appendChild(wrapper);
        loadLogo(f.team1.logo, fixture.querySelector('.team1-logo'))
        loadLogo(f.team2.logo, fixture.querySelector('.team2-logo'))
        animTime = animTime + 1
    })
}

document.addEventListener('DOMContentLoaded', buildFixtures)