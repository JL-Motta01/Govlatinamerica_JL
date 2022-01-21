var dateAndTime = document.getElementById("dateAndTime")
var data = new Date();
dateAndTime.innerHTML = data
var meses = new Array("jan.", "fev.", "mar.", "abr.", "mai.", "jun.", "jul.", "ago.", "set.", "out.", "nov.", "dez.");
var dia = data.getDate();
var mes = data.getMonth();
var ano = data.getFullYear();
dateAndTime.innerHTML = dia + ' ' + meses[data.getDay()] + ' ' + ano + '.';