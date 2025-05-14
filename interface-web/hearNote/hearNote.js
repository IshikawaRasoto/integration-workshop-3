let volume = 50;
let holdTimer = null;
let audioContext = null;
let noteOscillator = null;

// Set up event listeners when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Setup for note play button
  document.getElementById('playNoteBtn').addEventListener('click', playNote);

  // Setup for volume up button
  const volUpBtn = document.getElementById('volUpBtn');
  volUpBtn.addEventListener('mousedown', function() {
    changeVolume(5); // Immediate change
    holdTimer = setInterval(() => changeVolume(5), 250); // Change every 250ms
  });
  
  volUpBtn.addEventListener('mouseup', function() {
    clearInterval(holdTimer);
  });
  
  volUpBtn.addEventListener('mouseleave', function() {
    clearInterval(holdTimer);
  });
  
  // Setup for volume down button
  const volDownBtn = document.getElementById('volDownBtn');
  volDownBtn.addEventListener('mousedown', function() {
    changeVolume(-5); // Immediate change
    holdTimer = setInterval(() => changeVolume(-5), 250); // Change every 250ms
  });
  
  volDownBtn.addEventListener('mouseup', function() {
    clearInterval(holdTimer);
  });
  
  volDownBtn.addEventListener('mouseleave', function() {
    clearInterval(holdTimer);
  });
  
  // Touch support for mobile devices
  volUpBtn.addEventListener('touchstart', function(e) {
    e.preventDefault(); // Prevent default touch behavior
    changeVolume(5);
    holdTimer = setInterval(() => changeVolume(5), 250);
  });
  
  volUpBtn.addEventListener('touchend', function() {
    clearInterval(holdTimer);
  });
  
  volDownBtn.addEventListener('touchstart', function(e) {
    e.preventDefault();
    changeVolume(-5);
    holdTimer = setInterval(() => changeVolume(-5), 250);
  });
  
  volDownBtn.addEventListener('touchend', function() {
    clearInterval(holdTimer);
  });
});

function changeVolume(d) {
  volume = Math.max(0, Math.min(100, volume + d));
  document.getElementById('volumeDisplay').textContent = `🔊 ${volume}%`;
}

function play() { 
  alert('Playing…'); 
}

function stop() { 
  alert('Stopped.'); 
}

function selectMusic() {
  alert(`You selected: ${document.getElementById('musicSelect').value}`);
}

function goBack() {
  window.location.href = '/';   
}

function playNote() {
  // Initialize audio context if not already created
  console.log("Playing");
}