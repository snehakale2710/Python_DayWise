/* ==========================================
   PRODUCT DATA
========================================== */

const products = [

    {
        id: 1,
        name: "Classic Casual Shirt",
        brand: "Roadster",
        category: "men",
        price: 799,
        oldPrice: 1499,
        image: "images/product1.jpg"
    },

    {
        id: 2,
        name: "Women Casual Dress",
        brand: "DressBerry",
        category: "women",
        price: 999,
        oldPrice: 1999,
        image: "images/product2.jpg"
    },

    {
        id: 3,
        name: "Running Sneakers",
        brand: "Puma",
        category: "shoes",
        price: 1499,
        oldPrice: 2999,
        image: "images/product3.jpg"
    },

    {
        id: 4,
        name: "Premium Watch",
        brand: "Fossil",
        category: "accessories",
        price: 2499,
        oldPrice: 4999,
        image: "images/product4.jpg"
    },

    {
        id: 5,
        name: "Men Denim Jacket",
        brand: "Levis",
        category: "men",
        price: 1799,
        oldPrice: 2999,
        image: "images/product5.jpg"
    },

    {
        id: 6,
        name: "Women Handbag",
        brand: "Lavie",
        category: "women",
        price: 1299,
        oldPrice: 2499,
        image: "images/product6.jpg"
    },

    {
        id: 7,
        name: "Sports Shoes",
        brand: "Nike",
        category: "shoes",
        price: 1999,
        oldPrice: 3999,
        image: "images/product7.jpg"
    },

    {
        id: 8,
        name: "Sunglasses",
        brand: "Ray-Ban",
        category: "accessories",
        price: 999,
        oldPrice: 1999,
        image: "images/product8.jpg"
    }

];


/* ==========================================
   CART
========================================== */

let cart = JSON.parse(
    localStorage.getItem("cart")
) || [];


/* ==========================================
   DISPLAY PRODUCTS
========================================== */

function displayProducts(productList = products) {

    const container =
        document.getElementById("productContainer");

    if (!container) {
        return;
    }

    container.innerHTML = "";


    if (productList.length === 0) {

        container.innerHTML = `
            <p style="
                grid-column:1/-1;
                text-align:center;
                padding:40px;
            ">
                No products found.
            </p>
        `;

        return;
    }


    productList.forEach(product => {

        container.innerHTML += `

            <div class="product-card">

                <button
                    class="product-heart"
                    onclick="addWishlist(${product.id})"
                >
                    <i class="fa-regular fa-heart"></i>
                </button>


                <div class="product-image">

                    <img
                        src="${product.image}"
                        alt="${product.name}"
                        onerror="this.src='https://via.placeholder.com/400x450?text=Product'"
                    >

                </div>


                <div class="product-info">

                    <p class="product-brand">
                        ${product.brand}
                    </p>

                    <h3 class="product-name">
                        ${product.name}
                    </h3>

                    <p class="product-price">

                        ₹${product.price}

                        <span class="old-price">
                            ₹${product.oldPrice}
                        </span>

                    </p>


                    <button
                        class="add-cart"
                        onclick="addToCart(${product.id})"
                    >
                        Add To Cart
                    </button>

                </div>

            </div>

        `;

    });

}


/* ==========================================
   ADD TO CART
========================================== */

function addToCart(id) {

    const product =
        products.find(item => item.id === id);

    if (!product) {
        return;
    }


    const existingProduct =
        cart.find(item => item.id === id);


    if (existingProduct) {

        existingProduct.quantity++;

    } else {

        cart.push({

            ...product,

            quantity: 1

        });

    }


    saveCart();

    updateCartCount();

    alert(
        `${product.name} added to cart!`
    );

}


/* ==========================================
   SAVE CART
========================================== */

function saveCart() {

    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );

}


/* ==========================================
   CART COUNT
========================================== */

function updateCartCount() {

    const countElement =
        document.getElementById("cartCount");

    if (!countElement) {
        return;
    }


    const totalItems =
        cart.reduce(
            (total, item) =>
                total + item.quantity,
            0
        );


    countElement.textContent =
        totalItems;

}


/* ==========================================
   OPEN CART
========================================== */

function openCart() {

    const overlay =
        document.getElementById("cartOverlay");

    if (!overlay) {
        return;
    }

    overlay.classList.add("active");

    displayCart();

}


/* ==========================================
   CLOSE CART
========================================== */

function closeCart() {

    const overlay =
        document.getElementById("cartOverlay");

    if (!overlay) {
        return;
    }

    overlay.classList.remove("active");

}


/* ==========================================
   DISPLAY CART
========================================== */

function displayCart() {

    const cartItems =
        document.getElementById("cartItems");

    const cartTotal =
        document.getElementById("cartTotal");


    if (!cartItems) {
        return;
    }


    cartItems.innerHTML = "";


    if (cart.length === 0) {

        cartItems.innerHTML = `

            <div style="
                text-align:center;
                padding:40px 10px;
            ">

                <i
                    class="fa-solid fa-cart-shopping"
                    style="
                        font-size:40px;
                        margin-bottom:15px;
                    "
                ></i>

                <p>
                    Your cart is empty.
                </p>

            </div>

        `;

        if (cartTotal) {
            cartTotal.textContent = "0";
        }

        return;
    }


    let total = 0;


    cart.forEach(item => {

        total +=
            item.price *
            item.quantity;


        cartItems.innerHTML += `

            <div class="cart-item">

                <img
                    src="${item.image}"
                    alt="${item.name}"
                    onerror="this.src='https://via.placeholder.com/80x90?text=Product'"
                >


                <div class="cart-item-info">

                    <h4>
                        ${item.name}
                    </h4>

                    <p>
                        ₹${item.price}
                    </p>

                    <p>
                        Quantity:
                        ${item.quantity}
                    </p>

                </div>


                <button
                    class="remove-cart"
                    onclick="removeFromCart(${item.id})"
                >
                    <i class="fa-solid fa-trash"></i>
                </button>

            </div>

        `;

    });


    if (cartTotal) {
        cartTotal.textContent = total;
    }

}


/* ==========================================
   REMOVE FROM CART
========================================== */

function removeFromCart(id) {

    cart =
        cart.filter(
            item => item.id !== id
        );


    saveCart();

    updateCartCount();

    displayCart();

}


/* ==========================================
   CATEGORY FILTER
========================================== */

function filterCategory(category) {

    const filteredProducts =
        products.filter(
            product =>
                product.category === category
        );


    displayProducts(filteredProducts);


    document
        .getElementById("products")
        .scrollIntoView({
            behavior: "smooth"
        });

}


/* ==========================================
   SEARCH
========================================== */

const searchInput =
    document.getElementById("searchInput");


if (searchInput) {

    searchInput.addEventListener(
        "input",
        function () {

            const searchText =
                this.value
                    .toLowerCase()
                    .trim();


            const filtered =
                products.filter(product =>

                    product.name
                        .toLowerCase()
                        .includes(searchText)

                    ||

                    product.brand
                        .toLowerCase()
                        .includes(searchText)

                    ||

                    product.category
                        .toLowerCase()
                        .includes(searchText)

                );


            displayProducts(filtered);

        }
    );

}


/* ==========================================
   MOBILE MENU
========================================== */

function toggleMenu() {

    const menu =
        document.getElementById("mobileMenu");

    if (!menu) {
        return;
    }

    menu.classList.toggle("active");

}


/* ==========================================
   WISHLIST
========================================== */

function addWishlist(id) {

    const product =
        products.find(item => item.id === id);

    if (!product) {
        return;
    }


    let wishlist =
        JSON.parse(
            localStorage.getItem("wishlist")
        ) || [];


    const exists =
        wishlist.some(
            item => item.id === id
        );


    if (!exists) {

        wishlist.push(product);

        localStorage.setItem(
            "wishlist",
            JSON.stringify(wishlist)
        );

        alert(
            `${product.name} added to wishlist!`
        );

    } else {

        alert(
            "Product is already in wishlist."
        );

    }

}


/* ==========================================
   CHECKOUT
========================================== */

function checkout() {

    if (cart.length === 0) {

        alert(
            "Your cart is empty."
        );

        return;
    }


    alert(
        "Checkout feature will be added next."
    );

}


/* ==========================================
   NEWSLETTER
========================================== */

const newsletterForm =
    document.getElementById(
        "newsletterForm"
    );


if (newsletterForm) {

    newsletterForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();

            alert(
                "Thank you for subscribing!"
            );

            newsletterForm.reset();

        }
    );

}


/* ==========================================
   PAGE LOAD
========================================== */

displayProducts();

updateCartCount();