var nam = document.querySelector('#name');
var price = document.querySelector('#price');
var bill = document.querySelector('#total');
var rm = document.querySelector('#remove');
var cart =document.querySelector('#cart1');

function shoppingcart()
{
  var orders=JSON.parse(localStorage.getItem('orders'));
  var total = localStorage.getItem('total');
  var cartsize = orders.length;

  nam.innerHTML = '';
  price.innerHTML = '';
  rm.innerHTML = '';

  nam.innerHTML = '<h3>Name</h3><br>'
  price.innerHTML ='<h3>Price</h3><br>'
  rm.innerHTML = '<h3>Remove</h3><br>'

  for(i = 0; i < cartsize; i++){
    nam.innerHTML += '<h4>'+orders[i][0]+'</h4>'
    price.innerHTML += '<h4>'+orders[i][1]+'</h4>'
    rm.innerHTML += '<h6><button class="btn-danger" onclick="removecart(' + i + ')">x</button></h6>'
  }
  bill.innerHTML = '<h3>'+'<div class="btn btn-success">TOTAL</div>'+' '+total+' '+'rupees'+'</h3>'
  cart.innerHTML = orders.length
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
