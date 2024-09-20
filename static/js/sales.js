document.addEventListener('DOMContentLoaded', () => {
    const salesForm = document.getElementById('sales-form');
    
    salesForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const productName = document.getElementById('product-name').value;
        const quantity = document.getElementById('quantity').value;
        const totalAmount = document.getElementById('total-amount').value;
        
        try {
            const response = await fetch('/api/sales/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_name: productName, quantity: parseInt(quantity), total_amount: parseFloat(totalAmount) }),
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
            alert('An error occurred while processing sale');
        }
    });
});
