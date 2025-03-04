// Obtener referencias a las partes del carnet
const frontCard = document.getElementById('front-card');
const backCard = document.getElementById('back-card');

// Agregar evento de clic a la parte frontal
frontCard.addEventListener('click', () => {
  frontCard.style.display = 'none';
  backCard.style.display = 'block';
});

// Agregar evento de clic a la parte trasera
backCard.addEventListener('click', () => {
  backCard.style.display = 'none';
  frontCard.style.display = 'block';
});