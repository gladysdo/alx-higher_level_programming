#!/usr/bin/node
// If w or h is equal to 0 or not a positive integer 
// Create an empty object

class Rectangle {
  constructor(w, h) {
  if (w > 0 && h > 0) {
  this.width = w;
  this.heigh = h;
  }
 }
}

module.exports = Rectangle;
