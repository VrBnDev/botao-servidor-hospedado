const physicalButton = document.getElementById('physicalButton');
let ultimoStatus = ''; // Armazena o último estado exibido

function atualizarStatus(novoStatus) {
  if (novoStatus !== ultimoStatus) {
    physicalButton.textContent = novoStatus === 'pressed' ? 'Pressionado' : 'Solto';
    ultimoStatus = novoStatus;
  }
}

function buscarStatus() {
  fetch('/status')
    .then(res => {
      if (!res.ok) throw new Error('Placa não conectada!');
      return res.json();
    })
    .then(data => {
      if (data.action === 'pressed' || data.action === 'unpressed') {
        atualizarStatus(data.action);
      } else {
        console.warn('Resposta inesperada:', data);
      }
    })
    .catch(err => {
      console.error('Erro na conexão:', err.message);
    });
}

setInterval(buscarStatus, 2000); // Executa a cada 2 segundos
