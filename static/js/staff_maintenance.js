/**
 * Gestión dinámica de insumos para Transportes Silverado
 */
const SupplyManager = {
    container: document.getElementById('supplies-container'),
    template: document.getElementById('supply-row-template'),

    init() {
        if (!this.container || !this.template) return;
        
        document.getElementById('add-supply-btn').addEventListener('click', () => this.addRow());
        
        // Agregar fila inicial si está vacío
        if (this.container.children.length === 0) {
            this.addRow();
        }
    },

    addRow() {
        const clone = this.template.content.cloneNode(true);
        const row = clone.querySelector('.supply-card');
        
        // Sincronizar Checkbox con Input Oculto para Django
        const checkbox = row.querySelector('.purchase-checkbox');
        const hiddenInput = row.querySelector('.purchase-hidden');
        
        checkbox.addEventListener('change', (e) => {
            hiddenInput.value = e.target.checked ? "true" : "false";
        });

        // Botón Eliminar
        row.querySelector('.btn-remove').addEventListener('click', () => {
            if (this.container.children.length > 1) {
                row.remove();
            }
        });

        this.container.appendChild(clone);
        if (window.lucide) window.lucide.createIcons();
    }
};

document.addEventListener('DOMContentLoaded', () => SupplyManager.init());