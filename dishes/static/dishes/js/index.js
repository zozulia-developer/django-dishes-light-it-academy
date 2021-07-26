let dishForm = document.querySelectorAll(".di-formset")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-ingredient")
let totalForms = document.querySelectorAll("input[name=di-TOTAL_FORMS]")

let formNum = dishForm.length - 1

addButton.addEventListener('click', (e) => {
    e.preventDefault()

    let newForm = dishForm[0].cloneNode(true)
    let formRegex = RegExp(`di-(\\d){1}-`, 'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `di-${formNum}-`)
    container.insertBefore(newForm, addButton)

    totalForms = document.querySelectorAll("input[name=di-TOTAL_FORMS]")
    totalForms.forEach(e => e.setAttribute('value', `${formNum+1}`))
})