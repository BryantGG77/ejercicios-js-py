//Crea una función que reciba dos listas de números del mismo tamaño y devuelva una nueva lista con la suma de los elementos uno a uno.

function sumaDeListas(lista1, lista2) {
    let nuevaLista = [];
    if (lista1.length == lista2.length) {
        for (let i = 0; i < lista1.length; i++) {
            let suma = lista1[i] + lista2[i]
            nuevaLista.push(suma);
        }
        return nuevaLista;
    } else {
        return 'Las listas no tienen la misma cantidad de elementos para ser operados y sumados uno a uno'
    }
}
let listaUno = [20, 40, 60, 80];
let listaDos = [10, 20, 30, 40];

let resultado = sumaDeListas(listaUno, listaDos);
console.log(resultado)