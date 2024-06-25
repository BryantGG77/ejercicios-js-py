
// Has hecho una compra y sabes el precio del producto y su IVA. Haz un script que te calcule el precio final del producto te recuerdo que para el IVA se aplica un 21%. Para calcular  el IVA debes multiplicar precio por el IVA que es 21%, dividido en 100.

let precio = parseInt(prompt("Cual es el precio del producto: "))

let iva = 21
let ivaProducto = precio * iva / 100
let precioFinal = precio + ivaProducto

console.log("El total son: " + precioFinal);