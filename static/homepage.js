// This code is going to contain the JS for my homepage button!

// Locate the button and sound and assign variables
const homeBtn = document.getElementById('homeBtn');
const hiddenSound = document.getElementById('hiddenSound');

// Add event listener to button to play sound!
homeBtn.addEventListener('click', (event) => {
    event.preventDefault(); // Don't redirect immediately on click
    hiddenSound.currentTime = 0; // Make sure sound starts from beginning
    hiddenSound.volume = 0.8; // Make volume 80% of original
    hiddenSound.play(); // Play sound!

    // Redirect to next page AFTER full sound has played
    setTimeout(() => {
        window.location.href = homeBtn.href; // Set window link to the home button's link AFTER the delay below
    }, 1300); // 1.3 sec delay
})