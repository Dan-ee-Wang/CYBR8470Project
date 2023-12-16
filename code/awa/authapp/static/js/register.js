// authapp/static/js/register.js

document.addEventListener('DOMContentLoaded', function () {
    const passwordField = document.getElementById('id_password1');
    const repeatPasswordField = document.getElementById('id_password2');
    const passwordTooltip = document.getElementById('password-tooltip');
    const matchTooltip = document.getElementById('match-tooltip');
    const repeatPasswordContainer = document.getElementById('repeat-password-container');

    passwordField.addEventListener('focus', () => {
        passwordTooltip.style.display = 'block';
    });

    passwordField.addEventListener('blur', () => {
        passwordTooltip.style.display = 'none';
    });

    passwordField.addEventListener('input', () => {
        const passwordValue = passwordField.value;
        const repeatPasswordValue = repeatPasswordField.value;

        // Show or hide the repeat password field based on password input
        if (passwordValue.length >= 8) {
            repeatPasswordContainer.style.display = 'block';
        } else {
            repeatPasswordContainer.style.display = 'none';
            matchTooltip.style.display = 'none';
        }

        // Show or hide the password tooltip based on password strength
        // For simplicity, assuming a password with at least 8 characters is strong
        if (passwordValue.length >= 8) {
            passwordTooltip.style.display = 'none';
        } else {
            passwordTooltip.style.display = 'block';
        }

        // Show or hide the match tooltip based on password matching
        if (passwordValue !== repeatPasswordValue) {
            matchTooltip.style.display = 'block';
        } else {
            matchTooltip.style.display = 'none';
        }
    });

    repeatPasswordField.addEventListener('input', () => {
        const passwordValue = passwordField.value;
        const repeatPasswordValue = repeatPasswordField.value;

        // Show or hide the match tooltip based on password matching
        if (passwordValue !== repeatPasswordValue) {
            matchTooltip.style.display = 'block';
        } else {
            matchTooltip.style.display = 'none';
        }
    });
});
