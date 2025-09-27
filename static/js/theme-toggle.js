const theme = localStorage.getItem("theme") || "dark-mode";
document.documentElement.setAttribute("theme", theme);

const themeToggleBtn = document.getElementById("toggle-theme");

if (themeToggleBtn.classList.contains("btn-light") && theme === "light-mode") {
  themeToggleBtn.textContent = "Dark";
  themeToggleBtn.classList.replace("btn-light", "btn-dark");
} else {
  themeToggleBtn.textContent = "Light";
  themeToggleBtn.classList.replace("btn-dark", "btn-light");
}

themeToggleBtn.addEventListener("click", () => {
  const currentTheme = document.documentElement.getAttribute("theme");
  const newTheme = currentTheme === "light-mode" ? "dark-mode" : "light-mode";

  themeToggleBtn.textContent = newTheme === "light-mode" ? "Dark" : "Light";

  document.documentElement.setAttribute("theme", newTheme);
  localStorage.setItem("theme", newTheme);

  if (themeToggleBtn.classList.contains("btn-light")) {
    themeToggleBtn.classList.replace("btn-light", "btn-dark");
  } else {
    themeToggleBtn.classList.replace("btn-dark", "btn-light");
  }
});
