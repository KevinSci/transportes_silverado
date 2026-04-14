/**
 * Lógica para la interfaz de inicio de sesión.
 * Maneja la visibilidad de contraseña e iconos de Lucide.
 */
document.addEventListener('DOMContentLoaded', () => {
    // Inicializar iconos de Lucide
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    const togglePasswordBtn = document.getElementById('toggle-password');
    const passwordInput = document.getElementById('id_password');
    const eyeIcon = document.getElementById('eye-icon');

    if (togglePasswordBtn && passwordInput) {
        togglePasswordBtn.addEventListener('click', () => {
            // Alternar el tipo de input
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';

            // Actualizar icono visualmente
            const newIconName = isPassword ? 'eye-off' : 'eye';
            eyeIcon.setAttribute('data-lucide', newIconName);
            
            // Re-renderizar solo el icono modificado
            lucide.createIcons({
                attrs: {
                    id: 'eye-icon'
                }
            });
        });
    }
});