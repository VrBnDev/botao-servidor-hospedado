const physicalButton = document.getElementById('physicalButton');

function atualizarStatus(texto) {
  physicalButton.textContent = texto;
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') atualizarStatus();
});


const socket = io();

socket.on('command', (data) => {
  if (data.action === 'pressed') atualizarStatus('Pressionado'); 
  if (data.action === 'unpressed') atualizarStatus('Solto'); 
});

