// static/js/users.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("Módulo de usuarios cargado exitosamente.");

    // Ejemplo: Confirmación antes de limpiar búsqueda
    const clearBtn = document.querySelector('.btn-clear-search');
    if (clearBtn) {
        clearBtn.addEventListener('click', (e) => {
            if (document.querySelector('input[name="q"]').value === '') {
                e.preventDefault();
            }
        });
    }
});