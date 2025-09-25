import { showNotification } from "../utils/notifications.js";

export function previewImage(file, previewArea) {
  if (!file.type.startsWith("image/")) {
    showNotification("Por favor, selecione apenas imagens.", "error");
    return;
  }
  if (file.size > 5 * 1024 * 1024) {
    showNotification("A imagem deve ter no máximo 5MB.", "error");
    return;
  }
  const reader = new FileReader();
  reader.onload = e => {
    previewArea.innerHTML = `<div class="attachment-preview-item">
      <img src="${e.target.result}" alt="Preview" class="preview-image">
      <span class="file-name">${file.name}</span>
    </div>`;
  };
  reader.readAsDataURL(file);
}

export function previewPDF(file, previewArea) {
  if (file.type !== "application/pdf") {
    showNotification("Por favor, selecione apenas PDF.", "error");
    return;
  }
  if (file.size > 10 * 1024 * 1024) {
    showNotification("O PDF deve ter no máximo 10MB.", "error");
    return;
  }
  previewArea.innerHTML = `<div class="attachment-preview-item">
    <span class="pdf-icon">📄</span>
    <span class="file-name">${file.name}</span>
  </div>`;
}
