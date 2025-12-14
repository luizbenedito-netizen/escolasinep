    document.addEventListener("DOMContentLoaded", function () {
      // Seleciona todos os botões que controlam um collapse
      const toggles = document.querySelectorAll("[data-collapse-toggle]");

      toggles.forEach(toggle => {
        const icon = toggle.querySelector(".rotate-icon");
        const contentId = toggle.getAttribute("data-collapse-toggle");
        const content = document.getElementById(contentId);

        toggle.addEventListener("click", () => {
          // Alterna a classe do ícone
          if (icon) icon.classList.toggle("rotate-180");

          // Alterna a visibilidade do conteúdo
          if (content) content.classList.toggle("hidden");
        });
      });
    });