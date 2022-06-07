/*let a = 2;
a = String(a);
console.log(typeof a);



b = 6
if (b==5) {
    console.log(b)
}
else {
    console.log('gjit')
}


while (b !=0) {
    console.log(b);
    b--;
}


for (let i=1; i < 10; i++) {
    console.log(i)
}
//alert - оповещение
//promt - спросить
//confirm - подтвепдить

do {
    console.log(b)
    b--;
} 
while (b > 0);

*/

/*function helloWorld(name, text) {
    let msg = name + ' ' + text
    console.log(msg)
}
helloWorld('Fyz', 'hui')

function sumNumbers(a,b) {
    return a + b;
}

let a = sumNumbers(10,20);
console.log(a)
*/

/*function agreeCookies(msg, yes, no) {
    if(confirm(msg)) yes();
    else no();
}

agreeCookies(
    'fdosnfsfnds',
    function() {console.log('yes')},
    function() { console.log('no')}

)
*/

/*setTimeout(function() {
    console.log('Gtne[');
}, 2000)

*/
/*
let annonym = () => {
    console.log('fdsagfn')
}
annonym();

let anon = () => 'Ky' // если ставим скобки, то нужен return

console.log(anon());

let hui = (a,b) => a+b;

console.log(hui(1,2));
*/
/*
let book = {
    title : 'yfpdfybt',
    price : 100,
    100 : 100
}

book.isSelled = false
console.log(book.isSelled)
console.log(book[100])

let newKey = 'color';

let car = {
    model : 'toyota',
    [newKey] : 'black'
}

console.log(car.color)


let book2 = {
    title : 'Mumu',
    author : 'ggdfs',
    price : 100
}

for(key in book2) {
    console.log(key + book2[key])
}
*/
/*
let car = {
    model : 'toyota',
    color : 'black',
    go : function (driverName) {
        console.log(driverName + 'vfibyf tltn');
    },
    stop(driverName) {
        console.log(driverName + 'stop')
    },
    getModel() {
        return this.model
    }
}

car.go('Вася');
*/
/*
function Book(title, author, price) {
    this.title = title;
    this.author = author;
    this.price = price;
}

let book = new Book('fds', 'dsaf', 100)
console.log(book.author)
*/
/*
let ar = [1,2,3,4,5]
console.log(ar.length)
*/

/*let divElem = document.getElementById('div_id')
console.log(divElem)
*/
// querySelector querySelectorAll - мотедоы поиска
// closest - родительский ближайший елемент
// contains - содержит ли дочерний элемент
//  console.dir - все елементы содержащиеся в дереве
// innerHTML - изменение тегов или структуры
// outerHTML - меняем тег и текст тега
// data - берем текст или комментарий
//textContent - берем текст из тега
//hidden - скрыть/открыть тег



var req = new XMLHttpRequest();
req.open("GET", "http://1solitary1.pythonanywhere.com/api/v1/sections/java");
req.send();

