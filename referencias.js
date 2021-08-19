// Recolhe o span de acesso

const dataPadrao = document.getElementById("data_acesso")
if(dataPadrao === null){
const nulo = document.getElementById("se_nulo")
nulo.innerText = "ABNT não disponível"
}else {
// console.log(dataPadrao)
// const dataPadrao = document.getElementsByClassName("referencia")[0].getElementsByTagName("span");

// Cria data
const data = new Date();

// Arruma mes
let mesNumero = data.getMonth() + 1
const month = (mes) => {
    if(mes === 1){
        return "jan."
    } else if(mes == 2){
        return "fev."
    } else if(mes == 3){
        return "mar."
    } else if(mes == 4){
        return "abr."
    } else if(mes == 5){
        return "mai."
    } else if(mes == 6){
        return "jun."
    } else if(mes == 7){
        return "jul."
    } else if(mes == 8){
        return "ago."
    } else if(mes == 9){
        return "set."
    } else if(mes == 10){
        return "out."
    } else if(mes == 11){
        return "nov."
    } else if(mes == 12){
        return "dez."
    }
}

//modifica o html pela data de acesso
dataPadrao.innerText = `Acesso em: ${data.getDate()} ${month(mesNumero)} ${data.getFullYear()}.`
}
