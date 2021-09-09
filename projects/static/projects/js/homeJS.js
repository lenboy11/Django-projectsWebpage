const popups = document.getElementsByClassName("popup");

function openPopupA(id) {
  const popup = document.getElementById("div " + id);
  const overlay = document.getElementById("overlay");
  popup.classList.remove("passive");
  popup.classList.add("active");
  overlay.classList.remove("passive");
  overlay.classList.add("active");
}

function closePopupA(id) {
  const popup = document.getElementById("div " + id);
  popup.classList.remove("active");
  popup.classList.add("passive");

  const overlay = document.getElementById("overlay");
  overlay.classList.remove("active");
  overlay.classList.add("passive");
}

function overlayClose() {
  for (let i = 0; i < popups.length; i++) {
    popups[i].classList.remove("active");
    popups[i].classList.add("passive");
  }

  const overlay = document.getElementById("overlay");
  overlay.classList.remove("active");
  overlay.classList.add("passive");
}
