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
    
    barraProgreso('#html-bar', 51);
    barraProgreso('#css-bar', 47);
    barraProgreso('#python-bar', 42);
    barraProgreso('#django-bar', 45);
    barraProgreso('#tkinter-bar', 73);
    barraProgreso('#mysql-bar', 35);
    barraProgreso('#javascript-bar', 20);
