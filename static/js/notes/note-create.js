import { getCSRFToken } from "../utils/csrf.js";
import { showNotification } from "../utils/notifications.js";
import { previewImage, previewPDF } from "./note-utils.js";

document.addEventListener("DOMContentLoaded", () => {
  const noteForm = document.getElementById("noteForm");
  const imageInput = document.getElementById("id_image");
  const pdfInput = document.getElementById("id_pdf");
  const previewArea = document.getElementById("attachmentPreview");

  if (noteForm) {
    noteForm.addEventListener("submit", e => {
      e.preventDefault();
      saveNote();
    });
  }

  if (imageInput) {
    imageInput.addEventListener("change", e => {
      previewImage(e.target.files[0], previewArea);
    });
  }

  if (pdfInput) {
    pdfInput.addEventListener("change", e => {
      previewPDF(e.target.files[0], previewArea);
    });
  }
});

async function saveNote() {
  const form = document.getElementById("noteForm");
  const saveBtn = document.getElementById("saveBtn");

  saveBtn.disabled = true;
  saveBtn.textContent = "Salvando...";

  try {
    const response = await fetch(form.action || window.location.href, {
      method: "POST",
      body: new FormData(form),
      headers: { "X-CSRFToken": getCSRFToken() }
    });

    if (!response.ok) throw new Error("Erro ao salvar nota");

    const data = await response.json();
    if (data.redirect) {
      window.location.href = data.redirect;
    } else {
      window.location.href = "/anotacoes/";
    }
  } catch (err) {
    showNotification(err.message, "error");
  } finally {
    saveBtn.disabled = false;
    saveBtn.textContent = "Salvar Nota";
  }
}
