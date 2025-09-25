export function showNotification(message, type = "info", duration = 4000) {
  const notification = document.createElement("div");
  notification.className = `notification notification-${type}`;
  notification.textContent = message;

  Object.assign(notification.style, {
    position: "fixed",
    top: "20px",
    right: "20px",
    padding: "12px 16px",
    borderRadius: "8px",
    color: "white",
    fontWeight: "600",
    zIndex: "10000",
    maxWidth: "400px",
    boxShadow: "0 4px 15px rgba(0,0,0,0.2)",
    transform: "translateX(100%)",
    transition: "transform 0.3s ease"
  });

  const colors = {
    success: "#28a745",
    error: "#dc3545",
    warning: "#ffc107",
    info: "#17a2b8"
  };
  notification.style.background = colors[type] || colors.info;

  document.body.appendChild(notification);

  setTimeout(() => (notification.style.transform = "translateX(0)"), 100);
  setTimeout(() => {
    notification.style.transform = "translateX(100%)";
    setTimeout(() => notification.remove(), 300);
  }, duration);
}
