document.addEventListener('DOMContentLoaded', () => {
    // Inicializa los iconos de Lucide
    lucide.createIcons();

    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            // Implementación simple de colapso
            const isHidden = sidebar.style.display === 'none';
            sidebar.style.display = isHidden ? 'flex' : 'none';
        });
    }
});