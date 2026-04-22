// static/js/assets_form.js
document.addEventListener('DOMContentLoaded', () => {
    const assetTypeSelect = document.getElementById('asset_type');
    const sectionTracto = document.getElementById('section-tracto');
    const sectionCaja = document.getElementById('section-caja');

    /**
     * Alterna la visibilidad y habilita/deshabilita inputs
     * @param {string} selectedType - 'tracto' o 'caja'
     */
    const updateFormVisibility = (selectedType) => {
        // Primero ocultamos ambos y deshabilitamos todos los inputs específicos
        [sectionTracto, sectionCaja].forEach(section => {
            section.classList.add('hidden');
            section.querySelectorAll('input, select, textarea').forEach(input => {
                input.disabled = true;
            });
        });

        // Activamos solo la sección correspondiente
        if (selectedType === 'tracto') {
            sectionTracto.classList.remove('hidden');
            sectionTracto.querySelectorAll('input, select, textarea').forEach(input => {
                input.disabled = false;
            });
        } else if (selectedType === 'caja') {
            sectionCaja.classList.remove('hidden');
            sectionCaja.querySelectorAll('input, select, textarea').forEach(input => {
                input.disabled = false;
            });
        }
    };

    // Escuchar cambios en el selector de tipo
    assetTypeSelect.addEventListener('change', (e) => {
        updateFormVisibility(e.target.value);
    });

    // Verificación inicial por si el navegador recuerda la selección al recargar
    if (assetTypeSelect.value) {
        updateFormVisibility(assetTypeSelect.value);
    }
});