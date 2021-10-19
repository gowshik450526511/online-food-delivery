var hours = 24;
var now  = new Date().getTime();
var stepTime = localStorage.getItem('stepTime');

if (stepTime == null){
    localStorage.setItem('stepTime',now);
}
else {
  if(now - stepTime > hours*60*60*1000) //1000 is for millisecond
  {
      localStorage.clear();            //clear the local storage of that particular person
      localStorage.setItem('stepTime',now); //set the new login time
  }
}

var orders=JSON.parse(localStorage.getItem('orders'));
var total = localStorage.getItem('total');

if(orders == null || orders == undefined ){
  localStorage.setItem('orders',JSON.stringify([]))
  orders = JSON.parse(localStorage.getItem('order'));
}
if(total == null || total == undefined ){
  localStorage.setItem('total',0);
  total = localStorage.getItem('order');
}

// var cart=document.querySelector("cart");
// cart.innerHTML = orders.length;
