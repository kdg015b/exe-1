document.addEventListener('DOMContentLoaded', function() {
    // Load and display the crypto portfolio
    fetch('portfolio.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('portfolio-container');
            let html = '<ul>';
            data.forEach(item => {
                html += `<li>${item.name} (${item.ticker}): ${item.percentage}%</li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        });

    // Load and display the Korean stock portfolio
    fetch('korean_stock_portfolio.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('korean-stock-container');
            let html = '<ul>';
            data.forEach(stock => {
                html += `<li><b>${stock.name} (${stock.ticker})</b>: ${stock.reason}</li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        });

    // Load and display portfolio recommendations
    fetch('portfolio_recommendations.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('recommendations-container');
            let html = '';
            for (const key in data) {
                const recommendation = data[key];
                html += `<h3>${recommendation.title}</h3>`;
                html += '<ul>';
                recommendation.stocks.forEach(stock => {
                    html += `<li><b>${stock.rank}. ${stock.name} (${stock.ticker})</b></li>`;
                });
                html += '</ul>';
            }
            container.innerHTML = html;
        });

    // Load and display the news
    fetch('news.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('news-container');
            let html = '<ul>';
            data.articles.forEach(article => {
                html += `<li><a href="${article.url}" target="_blank">${article.title}</a></li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        });
});
