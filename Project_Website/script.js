// Image Gallery Script
let currentIndex = 0;
const images = document.querySelectorAll('.images img');
const dots = document.querySelectorAll('.dot');

// Function to show the image based on the index
function showImage(index) {
  images.forEach((img, i) => {
    img.style.display = i === index ? 'block' : 'none';
  });

  dots.forEach((dot, i) => {
    dot.classList.remove('active');
    if (i === index) {
      dot.classList.add('active');
    }
  });
}

// Function to automatically switch images every 5 seconds
function autoSlide() {
  currentIndex = (currentIndex + 1) % images.length; // Cycle through the images
  showImage(currentIndex);
}

// Event listeners for manual image switching when clicking dots
dots.forEach(dot => {
  dot.addEventListener('click', () => {
    currentIndex = parseInt(dot.getAttribute('data-index'));
    showImage(currentIndex);
  });
});

// Initial Image Display
showImage(currentIndex);

// Start auto-slide every 5 seconds
setInterval(autoSlide, 5000);  // 5000ms = 5 seconds
