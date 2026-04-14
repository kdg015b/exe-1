document.addEventListener('DOMContentLoaded', function() {
    // Load and display the portfolio
    fetch('portfolio.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('portfolio-container');
            if (!data || data.length === 0) {
                container.innerHTML = '<p>No portfolio data available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(asset => {
                html += `<li><b>${asset.asset}</b>: ${asset.weight}%</li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching portfolio data:', error);
            const container = document.getElementById('portfolio-container');
            container.innerHTML = '<p>Could not load portfolio data.</p>';
        });

    // Load and display the news articles
    fetch('news.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('news-container');
            if (!data || data.length === 0) {
                container.innerHTML = '<p>No news articles available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(article => {
                html += `<li>
                    <h4><a href="${article.url}" target="_blank">${article.title}</a></h4>
                    <p>${article.description || 'No description available.'}</p>
                </li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching news data:', error);
            const container = document.getElementById('news-container');
            container.innerHTML = '<p>Could not load news data.</p>';
        });
});
