
/*$(function() {
  $('body').on('click','.plus-minus', function(e) {
    e.preventDefault();
    var delta = +this.dataset.delta;
    var input = $(this).parent().find('input')[0];
  
    input.value = +input.value + delta;
    var target = this.dataset.target;

    console.log(input.value);
    console.log(target);
    
    var getVal = $('#' + target).text();
    var totalPrice = getVal * input.value;
    
    console.log(totalPrice);
    $.ajax({
      type: "POST"
     }).then(function(totalPrice) {
         // resp < 0 there was a problem
        $('#' + target).text(totalPrice);
     });
  })

  
});*/



function plus(pizza_id){
  var input_qty = $('#qty-' + pizza_id);
  var new_qty = parseInt($(input_qty).val()) + 1;
  x(new_qty, pizza_id);
}

function minus(pizza_id){
  var input_qty = $('#qty-' + pizza_id);
  if ($(input_qty).val() > 1){
    var new_qty = parseInt($(input_qty).val()) - 1;
    x(new_qty, pizza_id);
  }
}

function totalPrice(new_qty){
  var price = $('#price');
  var newprice = parseInt($(price).val());
  var total = new_qty * newprice;

  return total;
}

function x(new_qty, pizza_id){
  var input_qty = $('#qty-' + pizza_id);
  var price = $('#price');
  var total = totalPrice(new_qty)
  console.log(totalPrice(new_qty))
  $.ajax({
    type : 'post',
    url: '{% url "index" %}',
	}).then($(function(response) {
    $(input_qty).val(new_qty);
    $(price).val(total);
  }))
}