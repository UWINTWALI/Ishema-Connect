document.getElementById('profileIcon').addEventListener('click', function() {
    const profileCard = document.getElementById('profileCard');
    profileCard.style.display = (profileCard.style.display === 'none' || profileCard.style.display === '') ? 'block' : 'none';
});

document.getElementById("close_btn").addEventListener('click', function () {
    profileCard = document.getElementById('profileCard');
    profileCard.style.display = 'none';
})


// DONATION POP UP WINDOW


document.addEventListener('DOMContentLoaded', function () {
  const donationCards = document.querySelectorAll('.donation-amount');
  const customAmountInput = document.getElementById('custom-amount');

  donationCards.forEach(card => {
    card.addEventListener('click', function () {
      // Remove 'selected' class from other cards
      donationCards.forEach(card => card.classList.remove('selected'));
      // Add 'selected' class to clicked card
      this.classList.add('selected');
      // Set the value in the custom amount input
      customAmountInput.value = this.getAttribute('data-amount');
    });
  });

  // Allow manual entry to override card selection
  customAmountInput.addEventListener('input', function () {
    donationCards.forEach(card => card.classList.remove('selected'));
  });
});
