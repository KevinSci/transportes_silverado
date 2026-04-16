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
            const display = window.getComputedStyle(sidebar).display;
            sidebar.style.display = (display === 'none') ? 'flex' : 'none';
        });
    }

    const updateActiveNavLink = () => {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-item');

        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            if (currentPath === linkPath) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    };

    updateActiveNavLink();

    // Menú de Perfil
    const profileTrigger = document.getElementById('profile-menu-trigger');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileTrigger && profileDropdown) {
        profileTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            // Alterna la clase dropdown-hidden para mostrar/ocultar
            profileDropdown.classList.toggle('dropdown-hidden');
        });

        // Cerrar al hacer clic fuera del menú
        document.addEventListener('click', (e) => {
            if (!profileDropdown.contains(e.target) && !profileTrigger.contains(e.target)) {
                profileDropdown.classList.add('dropdown-hidden');
            }
        });
    }
});