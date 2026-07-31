document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('togglePassword');
    if (!toggleButton) {
        return;
    }

    const passwordInput = toggleButton.closest('.input-group').querySelector('input');
    const toggleIcon = document.getElementById('togglePasswordIcon');

    toggleButton.addEventListener('click', function () {
        const isPassword = passwordInput.type === 'password';
        passwordInput.type = isPassword ? 'text' : 'password';
        toggleIcon.classList.toggle('bi-eye');
        toggleIcon.classList.toggle('bi-eye-slash');
    });
});
