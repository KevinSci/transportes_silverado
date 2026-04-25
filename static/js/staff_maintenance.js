document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('supplies-container');
    const template = document.getElementById('supply-row-template');
    const addBtn = document.getElementById('add-supply-btn');

    // Función para añadir una nueva fila de insumos
    const addNewSupply = () => {
        if (!template || !container) return;

        const clone = template.content.cloneNode(true);
        const card = clone.querySelector('.supply-card');
        
        // Sincronización del checkbox de compra para el backend
        const checkbox = card.querySelector('.purchase-checkbox');
        const hiddenInput = card.querySelector('.purchase-hidden');
        
        checkbox.addEventListener('change', (e) => {
            hiddenInput.value = e.target.checked ? "true" : "false";
        });

        // Eliminar fila
        card.querySelector('.remove-supply-btn').addEventListener('click', () => {
            if (container.querySelectorAll('.supply-card').length > 1) {
                card.remove();
            }
        });

        container.appendChild(clone);
        
        // Refrescar iconos de Lucide
        if (window.lucide) {
            window.lucide.createIcons();
        }
    };

    // Evento del botón "+"
    if (addBtn) {
        addBtn.addEventListener('click', (e) => {
            e.preventDefault();
            addNewSupply();
        });
    }

    // Insertar la primera fila por defecto al cargar
    if (container && container.children.length === 0) {
        addNewSupply();
    }
});