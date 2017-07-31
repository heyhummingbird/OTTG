var csrftoken = getCookie('csrftoken');

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

$(".item").each(function(i) {
  console.log(this) ;
  console.log($(this)) ;
  var button = this.childNodes[0].childNodes[3].childNodes[1] ;
  var item_id = $(this).attr('item_id') ;
  var item_done = $(this).attr('item_done') ;
//  console.log(item) ;
  console.log(item_done) ;
  console.log(item_id) ;
  button.addEventListener('click', function() {
    ChangeColor(i, item_id) ;
  }) 
  
  var complete = item_done.toLowerCase() ;
  if (complete === "true") {
    this.setAttribute('class', 'item delete') ;
    this.childNodes[0].childNodes[3].childNodes[1].innerHTML="undone" ;
  }
});

/*
{% for item in list.item_set.all %}
  var index = {{ forloop.counter }} - 1 ;
  var row = document.querySelector("#id_list_table").rows[index] ;
  var button = row.childNodes[0].childNodes[3].childNodes[1] ;
  button.addEventListener('click', function() {
    ChangeColor({{ forloop.counter }} - 1, {{ item.id }}) ;
  }) 
	var complete = "{{item.done}}".toLowerCase() ;
	if (complete === "true") {
		row.setAttribute('class', 'delete') ;
		row.childNodes[0].childNodes[3].childNodes[1].innerHTML="undone" ;
	}
{% endfor %}
*/

function ChangeColor(index, item_id) {
  var row = document.querySelector("#id_list_table").rows[index] ;
  if (row.classList.contains("delete") === true) {
    row.removeAttribute('class', 'delete') ;
    row.childNodes[0].childNodes[3].childNodes[1].innerHTML="done" ;
  }
  else {
    row.setAttribute('class', 'item delete') ;
    row.childNodes[0].childNodes[3].childNodes[1].innerHTML="undone" ;
  }
  console.log("index = " + index) ;
  console.log(row.classList) ;
  console.log(row.classList.contains("delete")) ;

  var headers = new Headers();
  headers.append('X-CSRFToken', csrftoken);
  headers.append('Accept', "application/json");
  headers.append('Content-Type', "application/json");

  var body = {
    "item_id": item_id
  } ;

  var done_request = new Request('done/', 
                                {method: "post",
                                 body: JSON.stringify(body),
                                 headers: headers,
                                 credentials: 'include'
                                })
  fetch(done_request).then(function(response) {
    //處理 response
  }).catch(function(err) {
      alert("Error!")
  })
  return ;
}