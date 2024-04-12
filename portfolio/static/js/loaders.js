'use strict'

function barraProgreso(id, limite){
    var contador = 0
    setInterval(() => {
        if(contador < limite){
            var variable = document.querySelector(id);
            contador ++;
            variable.style.width = contador + '%';
            variable.innerHTML = contador + '%';
        }
    }, 60)
    }
    
    barraProgreso('#html-bar', 62);
    barraProgreso('#css-bar', 68);
    barraProgreso('#python-bar', 82);
    barraProgreso('#django-bar', 75);
    barraProgreso('#tkinter-bar', 93);
    barraProgreso('#mysql-bar', 70);
    barraProgreso('#javascript-bar', 20);
