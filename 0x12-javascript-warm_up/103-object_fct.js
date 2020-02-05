#!/usr/bin/node
// In the line 9 insert into myObject a function
// to increment the value of myObject value.
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = () => (myObject.value = myObject.value + 1);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
