document.addEventListener('DOMContentLoaded', () => {
    const inventoryChart = document.getElementById('inventory-chart').getContext('2d');
    const productionChart = document.getElementById('production-chart').getContext('2d');
    const salesChart = document.getElementById('sales-chart').getContext('2d');

    fetchInventoryData();
    fetchProductionData();
    fetchSalesData();

    async function fetchInventoryData() {
        try {
            const response = await fetch('/api/reports/inventory');
            const data = await response.json();
            
            const rawMaterials = data.raw_materials.map(item => item.name);
            const rawMaterialsQuantities = data.raw_materials.map(item => item.quantity);
            
            new Chart(inventoryChart, {
                type: 'bar',
                data: {
                    labels: rawMaterials,
                    datasets: [{
                        label: 'Raw Materials Inventory',
                        data: rawMaterialsQuantities,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error fetching inventory data:', error);
        }
    }

    async function fetchProductionData() {
        try {
            const response = await fetch('/api/reports/production');
            const data = await response.json();
            
            const products = data.map(item => item.product_name);
            const quantities = data.map(item => item.quantity);
            
            new Chart(productionChart, {
                type: 'line',
                data: {
                    labels: products,
                    datasets: [{
                        label: 'Production Schedule',
                        data: quantities,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error fetching production data:', error);
        }
    }

    async function fetchSalesData() {
        try {
            const response = await fetch('/api/reports/sales');
            const data = await response.json();
            
            const products = data.map(item => item.product_name);
            const amounts = data.map(item => item.total_amount);
            
            new Chart(salesChart, {
                type: 'pie',
                data: {
                    labels: products,
                    datasets: [{
                        label: 'Sales by Product',
                        data: amounts,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.6)',
                            'rgba(54, 162, 235, 0.6)',
                            'rgba(255, 206, 86, 0.6)',
                            'rgba(75, 192, 192, 0.6)',
                            'rgba(153, 102, 255, 0.6)',
                        ],
                    }]
                },
                options: {
                    responsive: true,
                }
            });
        } catch (error) {
            console.error('Error fetching sales data:', error);
        }
    }
});
