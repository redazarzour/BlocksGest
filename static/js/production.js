document.addEventListener('DOMContentLoaded', () => {
    const productionForm = document.getElementById('production-form');
    
    productionForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const productName = document.getElementById('product-name').value;
        const quantity = document.getElementById('quantity').value;
        const scheduledDate = document.getElementById('scheduled-date').value;
        
        try {
            const response = await fetch('/api/production/schedule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_name: productName, quantity: parseInt(quantity), scheduled_date: scheduledDate }),
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
            alert('An error occurred while creating production schedule');
        }
    });
});
