document.addEventListener("DOMContentLoaded", () => {
  const frontCard = document.getElementById("front-card");
  const backCard = document.getElementById("back-card");

  if (frontCard && backCard) {
    frontCard.addEventListener("click", () => {
      frontCard.style.display = "none";
      backCard.style.display = "block";
    });

    backCard.addEventListener("click", () => {
      backCard.style.display = "none";
      frontCard.style.display = "block";
    });
  }
});

function hideCircles() {
  const background = document.querySelector('.background');
  if (window.innerWidth <= 700) {
    background.style.display = 'none';
  } else {
    background.style.display = 'block';
  }
}

window.addEventListener('resize', hideCircles);
window.addEventListener('load', hideCircles);