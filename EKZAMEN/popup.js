window.onload = function() {
    setTimeout(function() {
        document.getElementById('popup').style.display = 'block';
    }, 3000);
};

// Закрытие попапа по кнопке
document.getElementById('closeBtn').onclick = function() {
    document.getElementById('popup').style.display = 'none';
};

// Закрытие при клике вне попапа (опционально)
window.onclick = function(event) {
    const popup = document.getElementById('popup');
    if (event.target === popup) {
        popup.style.display = 'none';
    }
}; 