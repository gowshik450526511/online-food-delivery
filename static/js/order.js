var pcart = document.querySelector('#cart');
var ptotal = document.querySelector('#total');
var cart = document.querySelector("#cart1");

function additem(item){
  name='#item' + item;
  var name=document.querySelector(name).innerHTML;

  rupees='#item1'+item;
  var price=document.querySelector(rupees).innerHTML;

  console.log(name+" "+price);

  var orders=JSON.parse(localStorage.getItem('orders'));
  var total = localStorage.getItem('total');
  var cartsize = orders.length;

  orders[cartsize] = [name,price];
  localStorage.setItem('orders', JSON.stringify(orders));

  total = Number(total) + Number(parseInt(price));
  localStorage.setItem('total', total);

//update the number of items in shopping cart
  var cart=document.querySelector("#cart1");
  cart.innerHTML = orders.length;
}

function shoppingcart(){
  var orders=JSON.parse(localStorage.getItem('orders'));
  var total = localStorage.getItem('total');
  var cartsize = orders.length;
  pcart.innerHTML = '';
  for(i = 0; i < cartsize; i++){
    button = '<button class="del" onclick="removecart('+ i +')">x</button>';
    pcart.innerHTML += '<li>'+orders[i][0]+'  '+orders[i][1]+'  '+button+'</li><br>';
  }
  ptotal.innerHTML = '<li>'+' '+"TOTAL"+'  '+total;
}
shoppingcart();

function removecart(no){
  var orders=JSON.parse(localStorage.getItem('orders'));
  var total = localStorage.getItem('total');
  total = Number(total) - Number(orders[no][1]);
  orders.splice(no,1);
  localStorage.setItem('orders',JSON.stringify(orders));
  localStorage.setItem('total',total);
  cart.innerHTML = orders.length;
  shoppingcart();
}
