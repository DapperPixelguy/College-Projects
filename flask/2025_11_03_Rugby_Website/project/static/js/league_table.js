let current_sort = 'played'
let current_asc = false
let table_built = false
let selected_league_elem = document.querySelector('button')
let lastSortKey = 'lastSort'
let selected_league = localStorage.getItem(lastSortKey) || '1'


function loadPage(league='1'){
    document.querySelectorAll('button').forEach(o=>{
        if (o.value === league){
            o.classList.add('selected')
            selected_league_elem = o
        }
    })
    loadTable(undefined,undefined,league)
}

function changeLeague(elem){
    if (selected_league !== elem.value) {
        selected_league_elem.classList.remove('selected')
        selected_league_elem = elem
        selected_league_elem.classList.add('selected')
        selected_league = elem.value
        table_built = false
        loadTable(undefined, undefined, selected_league)
    }

    localStorage.setItem(lastSortKey, selected_league)

}

function toggleSort(sort) {
    if (current_sort === sort) {
        current_asc = !current_asc
    } else {
        current_sort = sort
        current_asc = false
    }

    loadTable(current_sort, current_asc, selected_league)
}

async function loadTable (sort='points', asc='false', league='1') {
    const table_body = document.querySelector('tbody')

    if (!table_built){

    table_body.innerHTML =`
     <tr class="loading">
        <td>Loading...</td>
        <td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
     </tr>
    ` }

    try {
        buildTable(sort, asc, league)

    } catch (error) {

    }

}

function updateTable(data) {
    const rows = document.querySelectorAll('tbody tr')

    data.forEach((team, i)=>{
        const cells = rows[i].querySelectorAll('td')

        cells[0].textContent = team.name

        let c = 1
        for (let v of Object.values(team.standing)) {
            cells[c].textContent = v
            c++
        }
    })

}

async function buildTable(sort, asc, league) {

    let response = await fetch(`/league-table/fetch?league=${league}&sort=${sort}&asc=${asc}`)
    let data = await response.json()

    if (table_built) {
        updateTable(data)
        return
    }

    table_built = true

    const table = document.querySelector('tbody')
    table.innerHTML = ``
    let counter = 0

    data.forEach(team => {
        const entry = document.createElement('tr')
        const standing = team.standing

        console.log(typeof standing.played)
        let name = document.createElement('td')

        if (counter === 1) {
            entry.classList.add('alternate')
            counter --
        } else {
            counter ++
        }

        entry.classList.add('entry')
        name.innerHTML = team.name
        entry.appendChild(name)

        Object.entries(standing).forEach(([key, value]) => {
            let elem = document.createElement('td')
            elem.innerHTML = value
            entry.appendChild(elem)
        })
        table.appendChild(entry)
    })
}

document.addEventListener('DOMContentLoaded', ()=> loadPage(selected_league))