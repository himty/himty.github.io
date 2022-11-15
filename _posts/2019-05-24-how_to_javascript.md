---
layout: post
title: How to Javascript
author: Jenny Wang
comments: true
tags:
- coding_notes
minutes: 10
---

## HTML STUFF
============

`<!DOCTYPE html>`

`<html>`

`<body onload=function()>`
- onload- does `function()`

`<script>`

`<h1>`

`<p id="demo">`
- `id`-     set the id so its elements can be found w/ getElementById()
    if there is no matching id, creates one at the bottom of the page
events: onchange, onclick, onmouseover, onmouseout, onkeydown, onload

`<br />`
- inserts a line break there

`<noscript>Text to display</noscript>`
- Display that text if javascript is not enabled

`<!-- and //-->`
- outline the script with this comment so unsupported computers skip it

`<div style="" align="" globalAtribbutes>`
- style- "color:#0000FF" => all text within <div> = that color
- align- left/right/center/justify(stretch) the elements
    - not supported in HTML5
- draggable- can click and drag like a picture   

`<form action="code.php" method="post/get">`
- for organization
- action- what to do after submit button is clicked
    - if ommitted, looks within the page
- method- how to submit data, GET = default (data displayed in 
- address field, POST = data hidden

`<fieldset>`
- for organization within `<form>`

`<legend>text</legend>`
- "header" for fieldset

`<input type="" name="name" value="text" onclick="function()">`
- type- none/text=text box, button=button, radio=multiple choice submit=submit button (see <form>)
- name- must be included to be submitted within <form>
    - id- can't be used for <form>
- value- text to initially display (hint). '' is empty
- onclick (buttons)- when element is clicked do blah

`<audio src="dir or website">`
- holds an audio file
- audio accessed by through audioElement.play()
- src- a directory or website that holds the audio file

`.innerHTML / .value`
- .value is for buttons, etc
- .innerHTML is for paragraphs, etc

`<strike>text</strike>`
- text has strikethrough


## GLOBAL ATTRIBUTES
==================
http://www.w3schools.com/TAGS/ref_standardattributes.asp

`draggable=true/false`
- click and drag the element like a picture
`spellcheck=true/false`
- have spellcheck within element or not



## EVENT ATTRIBUTES
=================
http://www.w3schools.com/TAGS/ref_eventattributes.asp

`onclick="function()"`
- do this when the element is clicked
- for string parameters, use quotes DIFFERENT from the one
    - surrounding the function 
    - ex: `"function('hi')"`

`ondblclick="function()"`
    - do this when the element is double clicked

`onload="function()"`
    - do this when the element loads

`onkeydown="function()"`
    - do this when key is down

# ====================================================================
# ====================================================================
# ====================================================================

## JAVASCRIPT STUFF
==================

## RANDOM SYNTAX AND STUFF
=======================

`<script type="text/JavaScript">script</script>`
- make a js script

`<script type="text/JavaScript" src="code.js">`
- reference an external js script

`==`
- equals
- ex: `"7" == 7` => true

`===`
- strict equals, takes var type into account, too
- ex: `"7" === 7` => false

`this`
- the element
- ex: 

        `<button onclick="this.value=Date()> `

    - changes button's own text

`typeof <variable>`
- returns type of variable
- ex: `typeof variable == 'undefined'`

if a variable doesn't exist, it basically == false
- ex:
        function test(callbackFunction)
            if (callbackFunction) {
                callbackFunction();
            }
        }

- and if I put test() with no callbackFunction, it just doesn't do anything
- AKA: can call functions with less arguments than specified

closure: variables created outside an event listener are "kept alive" if the reference in the listener is still there
- creates memory leaks
- use `$('element').off('event')`
    => ex: `$('button').off('click');`
"use strict" ontop of the script
- cannot "pollute the root scope"
    - can't make a new var to fit the uninitialized a = 2 in the window object

```
foo: function(){
    //do something
}
```

- another way to declare the function foo()

`try{ throw "error" } catch(e){ switch(e){ case "error" break;}`
- create + manage errors!
`let`
- block-scoped
- using x before let statement causes error
- only defined in its block
`var`
- function-scoped
- using x before var statement sets x to undefined
`that ${var1 + var2} is cool`
- template literals. Replaces "that " + (var1 + var2) + " is cool"
- can do multiline:

        `hi
        there`


    - (this has a \n in the middle)




## FUNCTIONS/ATTRIBUTES
======================
`window.alert(<text or num>);` [or just alert()]
    popup alert

`document`

- `.write(<text or num or object>);`
    - cannot write numbers when it is not in a function
    - only for testing purposes
    - if it is object, can type as `"<p>paragraph</p>"`
    - "`string" + num = "stringnum"`
    - `num + num = sum`
- `.getElementById(id);`
    - access an HTML element
    - `.innerHTML = "text";`
        - change the element's text
- `.body`
    - do something to the <body>
    - .appendChild('elementVariable')
        - add the element (ex: button) to the document
- `.createElement("element")`
    - ex: "button", "br" (line break)
    - create the element. 
    - can save it w/ `var btn = document.createElement("button");`
- `.createTextNode("text")`
    - create the text node (variable)
    - can save it w/ `var t = document.createTextNode("text");`

Any element variable (ex: btn)
- `btn.appendChild(textNode)`
- `.previousSibling`
    - returns element right before it in the parent
- `.replaceChild(newChildElement, oldChildElement)`
    - replace the old with the new
    - later do newChild.appendChild(oldChild) to restructure

`console.log(text/num, text/num, etc);`
- log text into the console (inspect element)
- multiple parameters => a space in the 

`str`
- `.indexOf("string"[, fromIndex]);`
    - returns first index of "string" within str
        - returns-1 if not found
    - begin looking from the index fromIndex
- `.lastIndexOf("string");`
    - returns last index of "string within str
        - returns -1 if there's nothing
- `.search("string")` or `.search([regexp object])`
    - can use regexp (but slower)
- `.match([regexp object])`
    - better search method
    - ex: `match(/m/gi)` (see regexp)
- `.substr(start, length);`
    - start at start and end length chars later
    - start is negative => start from the end of the string
- `.substring(start, end);`
    - start at start and end at end
- `.slice(start[, end]);`
    - almost same as `substring()`
    - if start/end are negative, count from the end of the string
        - doesn't work in Internet Exploerer 8 or earlier
    - only one parameter => slice out the rest of the string
- `.split("searchTerm"[, numElementsToReturn]);`
    - return array of str split at the search terms
    - can stop looking for new terms after numElementsToReturn
- `.charAt(index)`
    - returns char at the index
- `.replace("findThis", "replaceWithThis");`
    - replace all "findThis"'s with the replacement
- `.toLowerCase()`
    - returns string in all lowercase
- `.toUpperCase()`
    - returns string in all uppercase
- `.strike()`
    - returns <strike>[str.value]</strike>
- `.length`
    - returns length of string

`element.fireevent(eventStartingWithOn, event)`
- can be used without the () and stuff in it
- returns if the event was cancelled (ex: can't click there)
- eventStartingWithOn/event are more specifications

`Math.random()`
- returns rand number from 0 to 1
- `Math.floor(Math.random()*50)` for rand int between 0 and 50

`Array`
- .splice(index, number)
    remove element(s) from the array
- .push(element)
    add element to end of array
- .includes(element)
    - returns if the element is in the array
- .pop()
    removes and returns last element
- .shift()
    - removes and returns first element. all elements are shifted left
- can initialize with var a = [1, 2, 3]
- adding elements outside the array puts undefined in the middle

        var a = [1, 2, 3]
        a[5] = 0
        // a = [1, 2, 3, undefined, undefined, 0]

- an instanceof Array




## EVENTS FOR STUFF
==================

`document`
- `.ready()`
    - does what's inside () when doc is ready
`onerror = <function>`
- calls `<function>` when the document errors.



## VARIABLE MAGIC
================

`var varName = <something>;`

`window.varName`
- all global variables in HTML are part of the window object

`var car = {brand:"Fiat", price:"3000000000000"};`
- get values with car.price or car["price"]
- can have methods as elements
    - use with car.function()

`this.innerHTML = <blah>`
- change own element (ex: if in <button>, change button name)

strings
- `txt.length`
    - returns length of string

string objects
- For `var x = new String("Some Text");`
    - `x == y` (another new String()) => false
    - `x == x` => true
    - `!= "Some Text"`

if variable not given in parameter of function, it = undefined
    - ex: `func(x,y)` => use `func(1)` => y = undefined

2D Array
    - is arrays in an array
    - ex: 
            var array = new Array(columns);
            for (i = 0; i < columnds; i++) {
                array[i] = new Array(rows);
            }
    - access with `array[1][2]`




## PROTOTYPES
=============
- basically parent classes in java
- different from classes b/c they are hoisted
    - can be used in lines above it b/c it's basically in the head
- create prototype:

        function Person(n, a){
            this.name = n;
            this.age = a;
            this.talk = function() {console.log("Hi")};
        }

- add properties within prototype once made:
    - `Person.prototype.newProtoName = "value";`
- create new object from prototype:
    - `var joe = new Person("Joe", 70);`
- add property to existing object
    - `myObject.newProperty = "value";`
    - (creates it automagically for myObject and not prototype)
- add method to existing object

        myObject.property = function () {
            return "I dunno";
        };

`object.prototype.isPrototypeOf(obj)`
- returns whether object.prototype is in prototype chain of obj




## CLASSES
=========

- not hoisted

        class B extends A {
            publicField = 0;
            #privateField = 1;
            uninitialized;

            constructor(x, y) {
                this.x = x;
                this.y = y;
            }

            foo() {
                <function body>
            }
        }

- constructor is named "constructor"
- don't put `def`/`var`/`function` keywords in front of methods



## REGULAR EXPRESSIONS (regexp)
===============================

- object representing formatting
- syntax: `/pattern/modifiers`
    - pattern- word/char/[multiple things] to look for
    - modifiers- i (case-insensitive), 
        - `g` (global, find multiple matches)
        - `m` (multi-line matching)
- ex: `str.match(/m/gi)`
- ex: `var rEPattern1 = /z/i;`
`reg`
    - `.exec()`
        - returns first match if found
        - returns false if none found
        - if just called for the same string, starts searching after the previous match
    `.test()`
        - returns true if found, false if not found
        - if just called for the same string, starts searching after the previous match





## BUILT IN VARIABLES
=====================
`Date()`

`document.location`
- is website url






## HELPER FUNCTIONS
===================

Append text to document body

        document.body.appendChild(document.createTextNode("hi"));

Simulate a click without clicking there

        function eventFire(el, etype){
          if (el.fireEvent) {
            el.fireEvent('on' + etype);
          } else {
            var evObj = document.createEvent('Events');
            evObj.initEvent(etype, true, false);
            el.dispatchEvent(evObj);
          }
        }

- usage: `eventFire(document.getElementById('mytest1'), 'click');`

Get mouse coordinates when it changes

```
(function() {
    document.onmousemove = handleMouseMove;
    function handleMouseMove(event) {
        var dot, eventDoc, doc, body, pageX, pageY;

        event = event || window.event; // IE-ism

        // If pageX/Y aren't available and clientX/Y are,
        // calculate pageX/Y - logic taken from jQuery.
        // (This is to support old IE)
        if (event.pageX == null && event.clientX != null) {
            eventDoc = (event.target && event.target.ownerDocument) || document;
            doc = eventDoc.documentElement;
            body = eventDoc.body;

            event.pageX = event.clientX +
              (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
              (doc && doc.clientLeft || body && body.clientLeft || 0);
            event.pageY = event.clientY +
              (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
              (doc && doc.clientTop  || body && body.clientTop  || 0 );
        }

        // Use event.pageX / event.pageY here
    }
})();
```





## TERMS
========

String interpolation
- add variable value to a string
- ex: console.log(var+"hi");
- Escaping a letter
    - in a quote `"There\'s something"`
        - put a slash to print the apostrophe






## TIPS
======

- while testing on a web server
    - disable cache in inspect element
        - `Network->Disable cache`
- change order of elements by appending/something the `document.getElementById`



# ====================================================================
# ====================================================================
# ====================================================================

## JQUERY
========

`$(thing)`
- means the element is from jquery and should act like one >:D

`$(document)`

`$('button')`
- it's a button element!
    - `.on('event', doThis)`
        - 'event' is the event psh. ex: 'click'
        - doThis can be a function

# ====================================================================
# ====================================================================
# ====================================================================

## Notes
========

Should probably use a modern front end library like `ReactJS` so that the site doesn't become spaghetti code. These notes are a way to get started with HTML and Javascript, but don't really talk about best coding practices.
