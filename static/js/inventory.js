document.addEventListener('DOMContentLoaded', () => {
    const inventoryForm = document.getElementById('inventory-form');
    
    inventoryForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const itemType = document.getElementById('item-type').value;
        const itemId = document.getElementById('item-id').value;
        const quantity = document.getElementById('quantity').value;
        
        try {
            const response = await fetch('/api/inventory/update', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ item_type: itemType, item_id: itemId, quantity: parseFloat(quantity) }),
            });
            
            const result = await response.json();
            
            if (result.success) {
                alert(result.message);
                location.reload();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while updating inventory');
        }
    });
});
