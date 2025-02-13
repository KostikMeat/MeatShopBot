document.addEventListener("DOMContentLoaded", () => {
    const tg = window.Telegram.WebApp;

    // Загрузка товаров
    fetch('/api/products')
        .then(response => response.json())
        .then(products => {
            const productsContainer = document.getElementById('products');
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.className = 'product';

                productDiv.innerHTML = `
                    <img src="${product.image}" alt="${product.name}">
                    <p>${product.name}</p>
                    <p class="price" data-id="${product.id}">${product.price} руб.</p>
                `;

                productDiv.querySelector('.price').addEventListener('click', () => {
                    addToCart(product.id);
                });

                productsContainer.appendChild(productDiv);
            });
        });

    // Добавление товара в корзину
    function addToCart(productId) {
        tg.sendData(JSON.stringify({ action: 'add_to_cart', productId }));
    }

    // Открытие корзины
    document.getElementById('cart-button').addEventListener('click', () => {
        tg.sendData(JSON.stringify({ action: 'open_cart' }));
    });

    // Помощь
    document.getElementById('help-button').addEventListener('click', () => {
        tg.sendData(JSON.stringify({ action: 'help' }));
    });
});
