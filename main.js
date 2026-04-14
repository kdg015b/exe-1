document.addEventListener('DOMContentLoaded', function() {
    fetch('portfolio.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('portfolio-container');
            if (data.length === 0) {
                container.innerHTML = '<p>No portfolio data available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(asset => {
                html += `<li>${asset.asset}: ${asset.weight}%</li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching portfolio data:', error);
            const container = document.getElementById('portfolio-container');
            container.innerHTML = '<p>Could not load portfolio data.</p>';
        });
});
