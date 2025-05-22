const physicalButton = document.getElementById('physicalButton');

function atualizarStatus(texto) {
  physicalButton.textContent = texto;
}

setInterval(() => {
  fetch('/status')
    .then(res => res.json())
    .then(data => {
      if (data.action === 'pressed') atualizarStatus('Pressionado');
    })
    .catch(err => console.error('Erro na conexão:', err));
}, 2000); // a cada 1 segundo
