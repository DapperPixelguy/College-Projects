let fixtureCreate = document.getElementById('fixture-create')
let select = document.querySelectorAll('.team-select')

select.forEach((s)=>s.addEventListener('change', disableSelected))

document.addEventListener('DOMContentLoaded', disableSelected)

function disableSelected(){

    let arr = ['']

    select.forEach(s=>{
        s.querySelectorAll('option').forEach(o=>{
            if (o.selected) arr.push(o.value)
        })
    })

    select.forEach(s=>{
        s.querySelectorAll('option').forEach(o=>{
            o.disabled = !o.selected && arr.includes(o.value)
        })
    })
    console.log(arr)

}