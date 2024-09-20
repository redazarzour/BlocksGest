document.addEventListener('DOMContentLoaded', () => {
    const inventoryChart = document.getElementById('inventory-chart').getContext('2d');
    const productionChart = document.getElementById('production-chart').getContext('2d');
    const salesChart = document.getElementById('sales-chart').getContext('2d');
    const laborChart = document.getElementById('labor-chart').getContext('2d');

    fetchInventoryData();
    fetchProductionData();
    fetchSalesData();
    fetchLaborData();

    async function fetchInventoryData() {
        try {
            const response = await fetch('/api/reports/inventory');
            const data = await response.json();
            
            const rawMaterials = data.raw_materials.map(item => item.name);
            const rawMaterialsQuantities = data.raw_materials.map(item => item.quantity);
            const finishedGoods = data.finished_goods.map(item => item.name);
            const finishedGoodsQuantities = data.finished_goods.map(item => item.quantity);
            
            new Chart(inventoryChart, {
                type: 'bar',
                data: {
                    labels: [...rawMaterials, ...finishedGoods],
                    datasets: [
                        {
                            label: 'Raw Materials',
                            data: [...rawMaterialsQuantities, ...Array(finishedGoods.length).fill(0)],
                            backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        },
                        {
                            label: 'Finished Goods',
                            data: [...Array(rawMaterials.length).fill(0), ...finishedGoodsQuantities],
                            backgroundColor: 'rgba(153, 102, 255, 0.6)',
                        }
                    ]
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

            const inventoryDetails = document.getElementById('inventory-details');
            inventoryDetails.innerHTML = `
                <h4>Inventory Summary</h4>
                <p>Total Raw Materials: ${data.raw_materials.length}</p>
                <p>Total Finished Goods: ${data.finished_goods.length}</p>
                <p>Low Stock Items: ${data.raw_materials.filter(item => item.quantity < 10).length + data.finished_goods.filter(item => item.quantity < 10).length}</p>
            `;
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
            const dates = data.map(item => moment(item.scheduled_date).format('YYYY-MM-DD'));
            
            new Chart(productionChart, {
                type: 'line',
                data: {
                    labels: dates,
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
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            }
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            const productionDetails = document.getElementById('production-details');
            productionDetails.innerHTML = `
                <h4>Production Summary</h4>
                <p>Total Scheduled Productions: ${data.length}</p>
                <p>Total Quantity Scheduled: ${quantities.reduce((a, b) => a + b, 0)}</p>
                <p>Average Quantity per Schedule: ${(quantities.reduce((a, b) => a + b, 0) / data.length).toFixed(2)}</p>
            `;
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
            const dates = data.map(item => moment(item.transaction_date).format('YYYY-MM-DD'));
            
            new Chart(salesChart, {
                type: 'bar',
                data: {
                    labels: dates,
                    datasets: [{
                        label: 'Daily Sales',
                        data: amounts,
                        backgroundColor: 'rgba(255, 206, 86, 0.6)',
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            }
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            const salesDetails = document.getElementById('sales-details');
            salesDetails.innerHTML = `
                <h4>Sales Summary</h4>
                <p>Total Sales: $${amounts.reduce((a, b) => a + b, 0).toFixed(2)}</p>
                <p>Average Sale Amount: $${(amounts.reduce((a, b) => a + b, 0) / data.length).toFixed(2)}</p>
                <p>Best Selling Product: ${products[amounts.indexOf(Math.max(...amounts))]}</p>
            `;
        } catch (error) {
            console.error('Error fetching sales data:', error);
        }
    }

    async function fetchLaborData() {
        try {
            const response = await fetch('/api/reports/labor');
            const data = await response.json();
            
            const workers = data.map(item => item.name);
            const totalHours = data.map(item => item.total_hours);
            
            new Chart(laborChart, {
                type: 'bar',
                data: {
                    labels: workers,
                    datasets: [{
                        label: 'Total Hours Worked',
                        data: totalHours,
                        backgroundColor: 'rgba(153, 102, 255, 0.6)',
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

            const laborDetails = document.getElementById('labor-details');
            laborDetails.innerHTML = `
                <h4>Labor Summary</h4>
                <p>Total Workers: ${workers.length}</p>
                <p>Total Hours Worked: ${totalHours.reduce((a, b) => a + b, 0).toFixed(2)}</p>
                <p>Average Hours per Worker: ${(totalHours.reduce((a, b) => a + b, 0) / workers.length).toFixed(2)}</p>
            `;
        } catch (error) {
            console.error('Error fetching labor data:', error);
        }
    }
});
