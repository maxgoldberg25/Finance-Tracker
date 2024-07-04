function showFlashMessage(message, category) {
    var flashMessageDiv = document.getElementById('flash-message');
    var overlayDiv = document.getElementById('flash-overlay');
    
    flashMessageDiv.innerHTML = message;
    flashMessageDiv.style.display = 'block';
    overlayDiv.style.display = 'block';

    if (category === 'info') {
        flashMessageDiv.style.backgroundColor = '#d9edf7';
        flashMessageDiv.style.color = '#31708f';
    }
}

function closeFlashMessage() {
    document.getElementById('flash-message').style.display = 'none';
    document.getElementById('flash-overlay').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    const messages = JSON.parse(document.getElementById('flash-messages-data').textContent);
    if (messages.length > 0) {
        messages.forEach(([category, message]) => showFlashMessage(message, category));
    }
});


// Functions to simulate deposit and withdrawal
function deposit() {
    let amount = parseFloat(document.getElementById('depositAmount').value);
    let currentBalance = parseFloat(document.getElementById('currentBalance').innerText.replace('$', ''));
    document.getElementById('currentBalance').innerText = `$${currentBalance + amount}`;
}

function withdraw() {
    let amount = parseFloat(document.getElementById('withdrawAmount').value);
    let currentBalance = parseFloat(document.getElementById('currentBalance').innerText.replace('$', ''));
    document.getElementById('currentBalance').innerText = `$${currentBalance - amount}`;
}



document.addEventListener('DOMContentLoaded', function() {
    initPieChart();
});

var expenseChart;  // Global variable to hold the chart instance

function initPieChart() {
    var ctx = document.getElementById('expenseChart').getContext('2d');
    expenseChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Rent', 'Groceries', 'Savings', 'Utilities'],
            datasets: [{
                data: [300, 150, 100, 50],  // Default data
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            let label = tooltipItem.label || '';
                            let value = tooltipItem.raw;
                            return `${label}: $${value.toLocaleString()}`;
                        }
                    }
                }
            }
        }
    });
}
function updateChartData() {
    var rent = parseFloat(document.getElementById('rentInput').value) || 300;  // Use default or user input
    var groceries = parseFloat(document.getElementById('groceriesInput').value) || 150;
    var savings = parseFloat(document.getElementById('savingsInput').value) || 100;
    var utilities = parseFloat(document.getElementById('utilitiesInput').value) || 50;

    console.log('Data to update:', rent, groceries, savings, utilities);

    expenseChart.data.datasets[0].data = [rent, groceries, savings, utilities];
    expenseChart.update();
}