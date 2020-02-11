# 0x13. Javascript - Objects, Scopes and Closures

## Description

Learning objetives this project:

* How to create an object in Javascript
* What `this` means
* What `undefined` means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

---

### [0. Rectangle #0](./0-rectangle.js)

* Empty class Rectangle that defines a rectangle using the ES6 class notation.

### [1. Rectangle #1](./1-rectangle.js)

* Class Rectangle that defines a rectangle using the ES6 class notation with:
  * A constructor that must take 2 arguments w and h.
  * Initialize the instance attribute width with the value of w.
  * Initialize the instance attribute height with the value of h.

### [2. Rectangle #2](./2-rectangle.js)

* Class Rectangle that defines a rectangle using the ES6 class notation with:
  * A constructor that must take 2 arguments w and h.
  * Initialize the instance attribute width with the value of w.
  * Initialize the instance attribute height with the value of h.
  * If w or h is equal to 0 or not a positive integer, create an empty object.

### [3. Rectangle #3](./3-rectangle.js)

* Class Rectangle that defines a rectangle using the ES6 class notation with:
  * A constructor that must take 2 arguments w and h.
  * Initialize the instance attribute width with the value of w.
  * Initialize the instance attribute height with the value of h.
  * If w or h is equal to 0 or not a positive integer, create an empty object.
  * An instance method called print() that prints the rectangle using the character X.

### [4. Rectangle #4](./4-rectangle.js)

* Class Rectangle that defines a rectangle using the ES6 class notation with:
  * A constructor that must take 2 arguments w and h.
  * Initialize the instance attribute width with the value of w.
  * Initialize the instance attribute height with the value of h.
  * If w or h is equal to 0 or not a positive integer, create an empty object.
  * An instance method called print() that prints the rectangle using the character X.
  * An instance method called rotate() that exchanges the width and the height of the rectangle.
  * An instance method called double() that multiples the width and the height of the rectangle by 2

### [5. Square #0](./5-square.js)

* Class Square that defines a square and inherits from Rectangle of 4-rectangle.js using the ES6 class notation and extends with:
  * The constructor must take 1 argument: size
  * The constructor of Rectangle must be called (by using super())

### [6. Square #1](./6-square.js)

* Class Square that defines a square and inherits from Square of 5-square.js using the ES6 class notation and extends with:
  * An instance method called charPrint(c) that prints the rectangle using the character c
    * If c is undefined, use the character X

### [7. Occurrences](./7-occurrences.js)

* Function that returns the number of occurrences in a list:
  * Prototype: `exports.nbOccurences = function (list, searchElement)`

### [8. Esrever](./8-esrever.js)

* Function that returns the reversed version of a list:
  * Prototype: `exports.esrever = function (list)`
  * Can't use the built-in method reverse

### [9. Log me](./9-logme.js)

* Function that prints the number of arguments already printed and the new argument value:
  * Prototype: `exports.logMe = function (item)`
  * Output format: `<number arguments already printed>: <current argument value>`

### [10. Number conversion](./10-converter.js)

* Function that converts a number from base 10 to another base passed as argument:
  * Prototype: `exports.converter = function (base)`
  * Can't import any file
  * Can't declare any new variable (var, let, etc..)

### [11. Factor index](./100-map.js)

* Script that imports an array and computes a new array:
  * Must import list from the file `100-data.js`
  * Must use a map
  * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
  * Print both the initial list and the new list

### [12. Sorted occurences](./101-sorted.js)

* Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence:
  * Must import dict from the file `101-data.js`
  * In the new dictionary:
    * A key is a number of occurrences
    * A value is the list of user ids
  * Print the new dictionary at the end

### [13. Concat files](./102-concat.js)

* Script that concats 2 files:
  * The first argument is the file path of the first source file
  * The second argument is the file path of the second source file
  * The third argument is the file path of the destination

---

## Author

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
