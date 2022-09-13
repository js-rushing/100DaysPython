const expertise_lis = document.querySelectorAll('.hero_expertise_list-item')
const languages_lis = document.querySelectorAll('.hero_languages_list-item')

for (let i = 0; i < expertise_lis.length; i++) {
  addVisible(expertise_lis[i])
}

for (let i = 0; i < languages_lis.length; i++) {
  addVisible(languages_lis[i])
}

function addVisible(li) {
  li.classList.add('visible')
}
