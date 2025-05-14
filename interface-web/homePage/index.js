function navigateTo(page) {
  window.location.href = pageUrl(page);
}

// server-side routes: /creation, /hear, /identify
function pageUrl(name) {
  switch (name) {
    case 'creation': return '/creation';
    case 'hear':     return '/hear';
    case 'identify': return '/identify';
    default:         return '/';
  }
}

function showTutorial() {
  document.getElementById('tutorialOverlay').classList.add('show-tutorial');
}

function hideTutorial() {
  document.getElementById('tutorialOverlay').classList.remove('show-tutorial');
}