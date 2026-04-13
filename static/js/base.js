// static/js/base.js
document.addEventListener('DOMContentLoaded', () => {
    // Inicializa los iconos de Lucide
    lucide.createIcons();

    // Lógica del Sidebar
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            const isHidden = sidebar.style.display === 'none';
            sidebar.style.display = isHidden ? 'flex' : 'none';
        });
    }

    // Lógica del Menú de Perfil
    const profileTrigger = document.getElementById('profile-menu-trigger');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileTrigger && profileDropdown) {
        profileTrigger.addEventListener('click', (e) => {
            e.stopPropagation(); // Evita que el clic se propague al documento
            const isVisible = profileDropdown.style.display === 'block';
            profileDropdown.style.display = isVisible ? 'none' : 'block';
        });

        // Cerrar el menú si se hace clic en cualquier otro lugar de la pantalla
        document.addEventListener('click', (e) => {
            if (!profileDropdown.contains(e.target) && !profileTrigger.contains(e.target)) {
                profileDropdown.style.display = 'none';
            }
        });
    }
});