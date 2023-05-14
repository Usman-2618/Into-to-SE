let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');
let checkoutButton = document.querySelector('.checkout');

openShopping.addEventListener('click', ()=>{
    body.classList.add('active');
})
closeShopping.addEventListener('click', ()=>{
    body.classList.remove('active');
})
checkoutButton.addEventListener('click', () => {
    window.location.href = "http://127.0.0.1:8000/checkoutpage"  ; // replace checkout.html with the URL of your desired checkout page
  });

let products = [
    {
        id: 1,
        name: 'Mix Platter',
        image: '1.jpg',
        price: 2000
    },
    {
        id: 2,
        name: 'Bar-B-Que Pizza',
        image: '2.jpg',
        price: 1500
    },
    {
        id: 3,
        name: 'Arabia Platter',
        image: '3.avif',
        price: 1500
    },
    {
        id: 4,
        name: 'Chicken Noodles',
        image: '4.avif',
        price: 650
    },
    {
        id: 5,
        name: 'Beef Steak',
        image: '5.avif',
        price: 2500
    },
    {
        id: 6,
        name: 'Chicken Breast and Chips',
        image: '6.avif',
        price: 500
    },
    {
        id: 7,
        name: 'Cheesy Cheese Pizza   ',
        image: '7.PNG',
        price: 1700
    },
    {
        id: 8,
        name: 'Beef Sticks',
        image: '8.avif',
        price: 1200
    },
    {
        id: 9,
        name: 'Salmon Salad',
        image: '9.PNG',
        price: 1350
    },
];

let listCards  = [];
function initApp(){
    products.forEach((value, key) =>{
        let newDiv = document.createElement('div');
        newDiv.classList.add('item');
        newDiv.innerHTML = `
            <img src="static/images2/${value.image}">
            <div class="title">${value.name}</div>
            <div class="price">${value.price.toLocaleString()}</div>
            <button onclick="addToCard(${key})">Add To Cart</button>`;
        list.appendChild(newDiv);
    })
}
initApp();
function addToCard(key){
    if(listCards[key] == null){
        // copy product form list to list card
        listCards[key] = JSON.parse(JSON.stringify(products[key]));
        listCards[key].quantity = 1;
    }
    reloadCard();
}
function reloadCard(){
    listCard.innerHTML = '';
    let count = 0;
    let totalPrice = 0;
    listCards.forEach((value, key)=>{
        totalPrice = totalPrice + value.price;
        count = count + value.quantity;
        if(value != null){
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src="static/images2/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${value.quantity - 1})">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${value.quantity + 1})">+</button>
                </div>`;
                listCard.appendChild(newDiv);
        }
    })
    total.innerText = totalPrice.toLocaleString();
    quantity.innerText = count;
}
function changeQuantity(key, quantity){
    if(quantity == 0){
        delete listCards[key];
    }else{
        listCards[key].quantity = quantity;
        listCards[key].price = quantity * products[key].price;
    }
    reloadCard();
}