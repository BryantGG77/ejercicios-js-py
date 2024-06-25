// En una variable tienes el lado de un cuadrado y el area del cuadrado. Haz un script que te calcule el perimetro y el area de un cuadrado. el area la calculas multiplicando el lado por si mismo. El perimetro es la suma de todos los lados del cuadrado.

let lado = parseInt(prompt("Cual es el lado del cuadrado: "))
let area = lado * lado
let perimetro = lado * 4


console.log("El area es: " + area);
console.log("El perimetro es: " + perimetro);