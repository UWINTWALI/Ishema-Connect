document.getElementById('profileIcon').addEventListener('click', function() {
    const profileCard = document.getElementById('profileCard');
    profileCard.style.display = (profileCard.style.display === 'none' || profileCard.style.display === '') ? 'block' : 'none';
});

document.getElementById("close_btn").addEventListener('click', function () {
    profileCard = document.getElementById('profileCard');
    profileCard.style.display = 'none';
})