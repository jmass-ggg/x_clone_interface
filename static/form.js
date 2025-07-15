document.addEventListener('DOMContentLoaded', function() {
    var loginForm = document.getElementById('loginForm');
    var registerForm = document.getElementById('registerForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            var username = document.getElementById('username').value.trim();
            var password = document.getElementById('password').value.trim();
            var errorMsg = document.getElementById('errorMsg');
            if (!username || !password) {
                errorMsg.style.display = 'block';
                e.preventDefault();
            } else {
                errorMsg.style.display = 'none';
            }
        });
        document.getElementById('password').addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                document.querySelector('button[type="submit"]').focus();
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            var username = document.getElementById('username').value.trim();
            var email = document.getElementById('email').value.trim();
            var password = document.getElementById('password').value.trim();
            var errorMsg = document.getElementById('errorMsg');
            if (!username || !email || !password) {
                errorMsg.style.display = 'block';
                e.preventDefault();
            } else {
                errorMsg.style.display = 'none';
            }
        });
        document.getElementById('password').addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                document.querySelector('button[type="submit"]').focus();
            }
        });
    }
}); 