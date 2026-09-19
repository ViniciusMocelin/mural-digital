document.addEventListener("DOMContentLoaded", () => {
    // Efeito de confirmação dinâmica nos cards
    const cards = document.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            console.log("Card selecionado:", card.querySelector("h3").innerText);
        });
    });
});