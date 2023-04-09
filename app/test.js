//get all values in database
const url = new URL('http://127.0.0.1:5001/getall');
fetch(url).then(response => response.json()).then(data => console.log(data));

//add new value to database
const url_add = new URL('http://127.0.0.1:5001/add');
const params_add = {item:'country chicken',date:'2020-01-01',weight:3,transtype:'purchase',remark:'testing with javascript'};
url_add.search = new URLSearchParams(params_add).toString();
fetch(url_add).then(response=>response.json()).then(data=>console.log(data));

//update value in database
const url_update = new URL('http://127.0.0.1:5001/update');
const params_update = {item:'country chicken',date:'2020-01-01',weight:3,transtype:'sale',remark:'testing with javascript'};
url_update.search = new URLSearchParams(params_update).toString();
fetch(url_update).then(response=>response.json()).then(data=>console.log(data));

//delete value in database
const url_delete = new URL('http://127.0.0.1:5001/delete');
const params_delete = {item:'test'};
url_delete.search = new URLSearchParams(params_delete).toString();
fetch(url_delete).then(response=>response.json()).then(data=>console.log(data));

//fetch by value
const url_fetch = new URL('http://127.0.0.1:5001/get');
const params_fetch = {item:'country chicken'};
url_fetch.search = new URLSearchParams(params_fetch).toString();
fetch(url_fetch).then(response=>response.json()).then(data=>console.log(data));