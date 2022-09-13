"use strict";

var expertise_lis = document.querySelectorAll('.hero_expertise_list-item');
var languages_lis = document.querySelectorAll('.hero_languages_list-item');

for (var i = 0; i < expertise_lis.length; i++) {
  addVisible(expertise_lis[i]);
}

for (var _i = 0; _i < languages_lis.length; _i++) {
  addVisible(languages_lis[_i]);
}

function addVisible(li) {
  li.classList.add('visible');
}