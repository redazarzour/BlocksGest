document.addEventListener('DOMContentLoaded', () => {
    const inventoryChart = document.getElementById('inventory-chart').getContext('2d');
    const productionChart = document.getElementById('production-chart').getContext('2d');
    const salesChart = document.getElementById('sales-chart').getContext('2d');
    const laborChart = document.getElementById('labor-chart').getContext('2d');
    const forecastChart = document.getElementById('forecast-chart').getContext('2d');

    fetchInventoryData();
    fetchProductionData();
    fetchSalesData();
    fetchLaborData();
    fetchKPIData();
    fetchForecastData();

    document.getElementById('sales-date-range').addEventListener('change', (event) => {
        fetchSalesData(event.target.value);
    });

    // Add event listeners for export buttons
    document.getElementById('export-inventory').addEventListener('click', exportInventory);
    document.getElementById('export-production').addEventListener('click', exportProduction);
    document.getElementById('export-sales').addEventListener('click', exportSales);
    document.getElementById('export-labor').addEventListener('click', exportLabor);

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
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Quantity'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Inventory Levels'
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
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Quantity'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Production Trends'
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

    async function fetchSalesData(days = 30) {
        try {
            const response = await fetch(`/api/reports/sales?days=${days}`);
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
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Amount ($)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Sales Performance'
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
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Hours'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Worker'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Labor Efficiency'
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

    async function fetchKPIData() {
        try {
            const response = await fetch('/api/reports/kpi');
            const data = await response.json();

            const kpiDashboard = document.getElementById('kpi-dashboard');
            kpiDashboard.innerHTML = `
                <div class="col-md-3 mb-3">
                    <div class="card bg-primary text-white">
                        <div class="card-body">
                            <h5 class="card-title">Total Sales</h5>
                            <p class="card-text">$${data.total_sales.toFixed(2)}</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card bg-success text-white">
                        <div class="card-body">
                            <h5 class="card-title">Total Production</h5>
                            <p class="card-text">${data.total_production}</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card bg-info text-white">
                        <div class="card-body">
                            <h5 class="card-title">Inventory Value</h5>
                            <p class="card-text">$${data.inventory_value.toFixed(2)}</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card bg-warning text-dark">
                        <div class="card-body">
                            <h5 class="card-title">Labor Cost</h5>
                            <p class="card-text">$${data.labor_cost.toFixed(2)}</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card bg-danger text-white">
                        <div class="card-body">
                            <h5 class="card-title">Gross Profit</h5>
                            <p class="card-text">$${data.gross_profit.toFixed(2)}</p>
                        </div>
                    </div>
                </div>
            `;
        } catch (error) {
            console.error('Error fetching KPI data:', error);
        }
    }

    async function fetchForecastData() {
        try {
            const response = await fetch('/api/reports/forecast');
            const data = await response.json();

            new Chart(forecastChart, {
                type: 'line',
                data: {
                    labels: data.dates,
                    datasets: [{
                        label: 'Sales Forecast',
                        data: data.forecast,
                        borderColor: 'rgba(75, 192, 192, 1)',
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
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Forecasted Sales ($)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Sales Forecast (Next 30 Days)'
                        }
                    }
                }
            });

            const forecastDetails = document.getElementById('forecast-details');
            const averageForecast = data.forecast.reduce((a, b) => a + b, 0) / data.forecast.length;
            forecastDetails.innerHTML = `
                <h4>Forecast Summary</h4>
                <p>Average Forecasted Daily Sales: $${averageForecast.toFixed(2)}</p>
                <p>Total Forecasted Sales (30 days): $${data.forecast.reduce((a, b) => a + b, 0).toFixed(2)}</p>
            `;
        } catch (error) {
            console.error('Error fetching forecast data:', error);
        }
    }

    // Export functions
    async function exportInventory() {
        try {
            const response = await fetch('/api/reports/inventory/export');
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'inventory_report.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error exporting inventory data:', error);
        }
    }

    async function exportProduction() {
        try {
            const response = await fetch('/api/reports/production/export');
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'production_report.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error exporting production data:', error);
        }
    }

    async function exportSales() {
        try {
            const days = document.getElementById('sales-date-range').value;
            const response = await fetch(`/api/reports/sales/export?days=${days}`);
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'sales_report.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error exporting sales data:', error);
        }
    }

    async function exportLabor() {
        try {
            const response = await fetch('/api/reports/labor/export');
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'labor_report.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error exporting labor data:', error);
        }
    }
});
