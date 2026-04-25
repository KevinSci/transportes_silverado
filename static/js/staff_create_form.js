document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('supply-modal');
    const btnAdd = document.getElementById('btn-add-supply');
    const btnClose = document.getElementById('btn-close-modal');
    const btnDiscard = document.getElementById('btn-discard-supply');
    const btnSave = document.getElementById('btn-save-supply');
    const suppliesList = document.getElementById('supplies-list');

    // Inputs del modal
    const nameInput = document.getElementById('modal-name');
    const brandInput = document.getElementById('modal-brand');
    const modelInput = document.getElementById('modal-model');
    const qtyInput = document.getElementById('modal-qty');
    const purchaseInput = document.getElementById('modal-purchase');

    const toggleModal = (show) => {
        if (show) {
            modal.classList.remove('hidden');
            nameInput.focus();
        } else {
            modal.classList.add('hidden');
            clearModal();
        }
    };

    const clearModal = () => {
        nameInput.value = '';
        brandInput.value = '';
        modelInput.value = '';
        qtyInput.value = '1';
        purchaseInput.checked = false;
    };

    btnAdd.addEventListener('click', () => toggleModal(true));
    btnClose.addEventListener('click', () => toggleModal(false));
    btnDiscard.addEventListener('click', () => toggleModal(false));

    btnSave.addEventListener('click', () => {
        const name = nameInput.value.trim();
        if (!name) {
            alert('El nombre del insumo es obligatorio.');
            return;
        }

        const brand = brandInput.value.trim();
        const model = modelInput.value.trim();
        const qty = qtyInput.value;
        const needsPurchase = purchaseInput.checked;

        addSupplyToForm(name, brand, model, qty, needsPurchase);
        toggleModal(false);
    });

    const addSupplyToForm = (name, brand, model, qty, needsPurchase) => {
        // Crear elemento visual
        const itemDiv = document.createElement('div');
        itemDiv.className = 'supply-item';

        // Etiqueta visual si requiere compra
        const purchaseBadge = needsPurchase ? '<span class="supply-badge">Requiere Compra</span>' : '';
        const details = [brand, model].filter(Boolean).join(' - ');
        
        itemDiv.innerHTML = `
            <div class="supply-info">
                <strong>${name} ${purchaseBadge}</strong>
                <span>Cant: ${qty} ${details ? '| ' + details : ''}</span>
            </div>
            <button type="button" class="btn-remove" aria-label="Eliminar insumo">
                <i data-lucide="trash-2"></i>
            </button>
            
            <input type="hidden" name="supply_names[]" value="${escapeHtml(name)}">
            <input type="hidden" name="supply_brands[]" value="${escapeHtml(brand)}">
            <input type="hidden" name="supply_models[]" value="${escapeHtml(model)}">
            <input type="hidden" name="supply_qtys[]" value="${escapeHtml(qty)}">
            <input type="hidden" name="supply_needs_purchase[]" value="${needsPurchase ? 'true' : 'false'}">
        `;

        // Evento para eliminar
        itemDiv.querySelector('.btn-remove').addEventListener('click', () => {
            itemDiv.remove();
        });

        suppliesList.appendChild(itemDiv);
        
        // Re-renderizar iconos de Lucide en el nuevo elemento
        if (window.lucide) {
            lucide.createIcons({ root: itemDiv });
        }
    };

    // Utilidad para prevenir inyección XSS básica en los inputs ocultos
    const escapeHtml = (unsafe) => {
        return (unsafe || '').toString()
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
    };
});