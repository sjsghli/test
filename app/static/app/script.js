document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".dropdown-button").forEach((button) => {
    button.addEventListener("click", () => {
      const dropdownContent = button.nextElementSibling;

      if (dropdownContent.classList.contains("visible")) {
        document.querySelectorAll(".dropdown-content").forEach((element) => {
          element.classList.remove("visible");
        });
        dropdownContent.classList.remove("visible");
      } else {
        dropdownContent.classList.add("visible");
      }
    });
  });
});
