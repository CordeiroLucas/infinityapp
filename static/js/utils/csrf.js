export function getCSRFToken(name = "csrftoken") {
  let cookieValue = null;
  if (document.cookie) {
    document.cookie.split(";").forEach(cookie => {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
      }
    });
  }
  return cookieValue;
}
