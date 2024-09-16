onload = function() {
    gira();
}

function gira() {
    var imagem = document.getElementById('idPython');
    if(imagem.getAttribute('src').includes('python')) {
        imagem.setAttribute('src', '/static/img/MeuApp/nohtyp.png');
    }
    else {
        imagem.setAttribute('src', '/static/img/MeuApp/python.png');
    }
    setTimeout(gira, 5 * 1000);
}
   