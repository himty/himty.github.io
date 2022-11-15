---
layout: post
title: How to Java (APCS level)
author: Jenny Wang
comments: true
tags:
- coding_notes
minutes: 3
---

## Accessible methods in the Java Quick Reference
===============================================

`Object`
- `boolean equals(Object other)`
- `String toString()`

`Integer`
- `Integer(int value)`
- `int intValue()`
    - returns value in int
- `Integer.MIN_VALUE`
    - smallest value that can be stored in an int
- `Integer.MAX_VALUE`
    - largest value that can be stored in an int

`Double`
- `Double(double value)`
- `double doubleValue()`

`String`
- `int length()`
- `String substring(int from, int to)`
- `String substring(int from)`
- `int indexOf(String str)`
- `int compareTo(String other)`
    - returns
        - `0` if equivalent
        - some number > 0 if earlier in alphabet
        - some number < 0 if later in alphabet

`Math`
- `abs(int/double x)`
- `pow(double base, double exponent)`
- `sqrt(double x)`
- `double random()`
    - double in the range [0,1)

`List<E>`
- `int size()`
- `boolean add(E obj)`
    - returns true after adding it ._.
- `void add(int index, E obj)`
- `E get(int index)`
    - if it's a number, returns Integer/smth else
        - (not int/double, but Integer/Double)
- `E set(int index, E obj)`
- `E remove(int index)`
    - changes indices of next elements. BEWARE IN LOOPS
        

## TERMS
========

- API = Application Programming Interface
    - methods, routines, etc used to program
- nested/inner class
    ```
    class foo {
        class bar {...}
    }
    ```
    - ^^ bar is nested class
    - bar sees everything from foo, but isn't a foo
    - ex: String is a nested class of Object
- child class
    - `class bar extends foo {...}`
    - ^^bar is child class
    - bar sees everything from foo, and is a foo



## KEYWORDS
===========

`implements`
- for interfaces (methods not defined)
- provide definitions for APIs

`extends`
- for Classes (methods defined)
- parent-child relationship

`static`
- modifies/takes stuff from the class
- nonstatic (aka not putting static there) modifies the instance

`Integer/Double`
- can == null => can't assign null to an int
    - otherwise, it's the same as int/double in Java 5+

`List`
- from index 0
- see methods
- to initialize
    - `List<Integer/etc> a = Arrays.asList(ele1, ele2, ...);`
- is immutable (cannot be modified)
- is an interface

`ArrayList`
- extends AbstractList that extends List
- from index 0
- to initialize
    - `ArrayList<Integer/etc> a = new ArrayList(Arrays.asList(ele1, ...);`
- is a Class



## CONTROL STATEMENTS
=====================

- enhanced for loop ("for-each")
    ```
    String[] array = {...};
    for (String element : array) {
        //do something for all elements in array
    }
    the same as:
        for (int i=0; i<array.length(); i++) {
            ;
        }
    ```




## SORTS
========

- insertion sort
- selection sort
- bubble sort
- mergesort
- heapsort
- quick sort






# ==================================================

Java unrelated to APCS

- concurrency
    - processes happen at the same time
    - use threads
- immutable
    - that instance cannot be changed after it is made
    - uses the keyword final
- \unnnn (escape sequence like \n)
    - line break LOL
- `assert <boolean expression>`
    - check for bugs in the code
    - if expression after it is false, it stops the program
    - ex: assert varIsTrue == false
    
