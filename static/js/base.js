// static/js/base.js
document.addEventListener('DOMContentLoaded', () => {
    // Inicializa iconos con manejo de errores para no bloquear el resto del script
    try {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    } catch (e) {
        console.error("Lucide no pudo cargar:", e);
    }

    // Sidebar Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            // Verificación más robusta del estado actual
            const display = window.getComputedStyle(sidebar).display;
            sidebar.style.display = (display === 'none') ? 'flex' : 'none';
        });
    }

    // Menú de Perfil
    const profileTrigger = document.getElementById('profile-menu-trigger');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileTrigger && profileDropdown) {
        profileTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const isHidden = profileDropdown.style.display === 'none' || profileDropdown.style.display === '';
            profileDropdown.style.display = isHidden ? 'block' : 'none';
        });

        // Cerrar al hacer clic fuera
        document.addEventListener('click', (e) => {
            if (!profileDropdown.contains(e.target) && !profileTrigger.contains(e.target)) {
                profileDropdown.style.display = 'none';
            }
        });
    }
});