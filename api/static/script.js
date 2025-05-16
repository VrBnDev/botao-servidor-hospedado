const physicalButton = document.getElementById('physicalButton');

function atualizarStatus(texto) {
  physicalButton.textContent = texto;
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') atualizarStatus("Pressionado");
});

setInterval(() => {
  fetch('/status')
    .then(res => res.json())
    .then(data => {
      if (data.action === 'pressed') atualizarStatus('Pressionado');
      else atualizarStatus('Solto');
    })
    .catch(err => console.error('Erro na conexão:', err));
}, 1000); // a cada 1 segundo
