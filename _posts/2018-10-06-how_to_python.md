---
layout: post
title: How to Python
author: Jenny Wang
comments: true
tags:
- coding_notes
minutes: 10
---

## Weird things compared to Java
============
- Passes lists to functions as references
    - `list[1] = 2` actually changes data in list
- No semicolon (;)
- Tabs/spaces are necessary
- Print does everything
- Arrays replaced by lists
- Comments are # (not //)
- No main method (type everything together: global vars, functions, statements)
    - runs top to bottom (like javascript)
- "" same as '' (aka strings)
- booleans' values are 0 or 1 (more below)
- &&, \|\|, and ! are written as and, or, and not
- True and False are capitalized
- No variable type declaration (ex: var, int, double)
- "To the power of" is `** `
    - ex: `2 ** 4 == 16`
- == works for strings
- Multiline comments use triple quotes """
    - ex: 

            """I am a comment
            that can span
            multiple lines"""

- Continuation character \
    - Signifies that the next line is a part of the line above
    - ex: 

            var this = \
            some_value

- Functional programming allowed (Use lambda keyword)
    - Can pass functions as variables
- Define multiple variables on one line
    - ex: 

            var1, var2, var3 = val1, val2, val3

        - Must have one value per variable
- Number is True if it isn't 0 (if you're not doing ==, but like if or while or smth)
    None would be False
    Returns the second to last # if the last # throws an error (ex: 1/0)



## Terms
======

`docstring`

        '''Comment'''

- Describes something

`doctest`

        >>> print("Test")
        Test

- shows that this is how to use the function
- can do python3 -m doctest <filename> to test it. 
    - Prints out errors if output isn't the same as expected



## Operators
=========

`7 / 2`
- div
- Returns decimal representation of result

`7 // 2`
- floordiv
- Returns the rounded down integer of the result




## booleans
=========

`True`, `False`
- can be evaluated to 1 or 0 
    - ex: 

            points = isHit*pointsHit + (1-isHit)*pointsMiss

        - gives points correctly

`not` applies to the next boolean
- ex: `not 3 == 2` is `True`



## for loops
=========

`for i in range(<number>):`
    does it `<number>` times
    consider `<number> = len(myList)`

`for i in range(minIndex, maxIndex):`
- i is from [minIndex, maxIndex)
    - Note the inclusive \[ and exclusive )

`for elm in myList:`
- like a for-each loop in Java
- elm is an element in myList

`for key in myDictionary:`
- like for-each
- get the value by doing myDictionary[key]
- Keys are used in reverse-alphabetical order (z to a)
    - not necessarily in the order they were initialized to

`for char in "string":`
- for each character in the string
- because strings are lists

`for index, item in enumerate(list):`
- index is the index of item in the list
- item is the next item
- A magical for-each loop with indices too

`for a, b in zip(listA, listB):`
- Gives items in pairs. Will stop at the end of the shorter list
- a is the nth item in listA
- b is the nth item in listB
- Can do this for as many lists as you want

`for x in set(lst_a).intersection(lst_b):`
- Gives x if x is both in lst_a and lst_b

`for x in set(lst_a).difference(lst_b):`
- Gives x if x is in lst_a but not in lst_b


## if statements
=============

    if <expression>:
        <do something>
    elif <expression>:
        <do something>
    else:
        <do something else>
    <I'm out of the if statement!>



## Functions
==========

    def funcName(parameters):
        <"fuction docstring"> # Basically a comment to document the code
        <do something>
        <return [expression]>
         ^^^
        <"function docstring">- optional statement to document the function
        <do something>- the code block
        <return [expression]>- the return statement (optional)
                     - no return statement = return None

`*args`
- ex: `f(*args)`
    - function takes in an arbitrary number of arguments
- ex: run a generic function multiple times:

        def make_avg_f(fn, num_times):
            def avg_f(*args):
                return avg(f(*args))
            return avg_f
        >>> avg_f = make_avg_f(foo, 1000)
        >>> avg_f(foo_arg1, foo_arg2)
        100342342348729




## Classes
========

    class ClassName([BaseClass])
        member_var = True

        def __init__(self[, init_parameter, more, etc, ...]):
            self.init_parameter = init_parameter
        
        def other_method(self[, other_parameter, more, etc, ...]):
            <do something>

- `BaseClass` - think about superclasses
    - If it's not given, BaseClass defaults to object
    - Override methods by just making a new one with the same name/parameters
    - Classes that override don't need the __init__() method

- `__init__` must have at least one parameter
    - self will refer to the object being created

- In the example, .init_parameter is an attribute (no need for doing int attr, etc)
    - Access with my_square = Square() ==> my_square.sides

- `init_parameter` is a member variable (not instance variable-to particular instances of the class)
    - only available to members of the ClassName class

- `member_var` can be accessed by all objects of the ClassName class
    - But changing the value of one instance with hippo.is_alive = False doesn't
        - change the value of the other ex: cat.is_alive

- Use `self.var` to change any variables for that class's instance

- Methods - functions in a class
    - Must take self as first parameter
    - But when calling it, you don't have to include self inside the ()
    - ex: temp = ClassName() ==> temp.other_method()

- Call superclass's methods
    - super(ChildClass'sName, self).super_method()

- Functions from object
    - .__init__(self[, other_parameters, etc, ...])
        - Think of a constructor
    - .__repr__(self)
        - Stands for representation
        - Tells Python how to represent the object, ex: when printing
        - ex: `def __repr__(self): return "hi"`




## Lists
=======

- ARRAYS DO NOT EXIST (but think of them). They are LISTS
- Note the [] instead of the {} (dictionaries)
- Use len(list) for number of items

`myList = []`
- make a list
- put values in [] if you want to initialize w/ values
    - ex: `list = [2,3]`

`print myList`
- prints it in the format [value, value, value]

`myList[<index or sublist>]`
- index: the index from 0 to len(myList)
- sublist: <startval>:<endval> (inclusive:exclusive)
    - ex: 
        - `[3:5]` gives list with elements 3 and 4
        - `[:5]` gives list w/ elements up until 4 (no 5)
        - `[3:]` gives list w/ elements 3 up until the end
        - `[:]` gives entire list
- ex: `myList[0:2] = [0,1]`
    - AMAZING
    - array size on left doesn't have to equal size on right. simply replaces. AMAZING

- List comprehension for new lists
    - Initialize a fancy list

            [<var and expression] <for loop> [<if statement>]]

        - ex: `list = [i for i in range(10)]`
            - numbers 0 to 9 inclusive
        - ex: `list = [i * 2 for i in range(10)]`
            - even numbers 0 to 18 inclusive
        - ex: `list = [i for i in range(51) if i % 2 == 0]`
            - even numbers 0 to 50 inclusive 
        - ex: `list = [x*2 for x in range(6) if (x*2) % 3 == 0]`
            - Even numbers that are divisible by 3 from 0 to 5 inclusive
                - So [6] (which is 3 * 2)
        - Also a good counter
            - ex: `list = ["C" for x in range(5) if x < 3]`

- Concatenate lists with +
    - ex: `x = [1,2], y=[2,3] => x + y = [1, 2, 2, 3]`

- Create list with repeating values
    - ex: `[0] * 5 == [0, 0, 0, 0, 0]`
    - ex: `[0] * 2 * 2 == [0, 0, 0, 0] (not two lists inside a list)`
        - Use .append() instead

- To print without [] brackets
        `list = [1, 2, 3] ==> " ".join(list) ==> "1 2 3"`

- functions
    - `.append(val)`
        - Add val into the last slot of the array
    - `.count(val)`
        - Returns int of the # of occurances of val in the list
    - `.index(val)`
        - returns index of val in the list
        - BEWARE: throws ValueError if m isn't in the list
    - `.insert(index, item)`
            - inserts item at index (or the end of the list)
            - ex: insert at 100 then .index => at len(list)
    - `.pop(index)`
        - Removes item at index and returns it
    - `.remove(value)`
        - removes first item in the list that matches the value
        - NOTE: NOT THE INDEX
    - `.sort(reverse=bool, key=func)`
        - sorts items in the list (ex: alphabetical, smallest to largest)
        - modifies the list and doesn't return a new one
        - reverse=True => descending order. Else or not included, ascending order
        - key=func => applied to the element before sorting
            - ex: `lambda pair: pair[0]` to sort by the zeroth element of the objects
    - `del(list[index])`
        - Removes the item at index and won't return it
    - `sum(myList)`
        - returns sum of all elements in p



## Dictionaries
============

- Note the {} instead of the [] (lists)
- Think of structs
- Access values by looking up a key
- Can put list in dictionaries O:
- ex: 

        names = {"dog":"Spike", "cat":"Fluffy", "bird":"Sugar"}
        names["dog"] == "Spike"

- ex: 

        residents = {1:"Bob", 2:"Joe", 3:"What are more names"}
        residents[1] == "Bob"

- ex: 

        dict = {} # Empty dictionary

- ex: 

        dict["new key"] = new_value
        adds a new key-value pair to the dictionary

- ex: 

        dict["old key"] = new_value
        changes the value associated with the key

`del dict[key_name]`
- removes key_name and its associated value from the dictionary

- Functions

    `.items()`
    - Returns a list of tuples of key-value pairs in the dictionary in no particular order
        - Tuple = group (a key/value pair in this case)

    `.keys()`
    - Returns list of keys of the dictionary in no particular order
    `.values()`
    - Returns  list of the dictionary's values in no particular order

`defaultdict(default_value)`
- high performance container datatype that gives default_value if that key isn't found


## Tuple
======

- An immutable list (unchangeable)
- Surrounded by ()s and can contain any data type


## Data structures
===============

- Contained within collections
- deque(iter_for_init[, maxlen]) ("DEHK" pronounciation)
    - Double-sided queue
    - `append(x)`, `appendleft(x)`, `extend(iter)`, `extendleft(iter)`, `pop()`, `popleft()`
    - `remove(val)`, `reverse()`, `clear()`
    - `count(x)` - returns # of deque elements equal to x
    - `rotate(n=1)` shift in circular way to the right
    - `maxlen` - max length of the deque (corresponding # of items discarded as added if length > maxlen)


## Bitwise operators
=================

- Operators
    - `>>` - Right shift
        - "divide by 2 and round down"
        - Good for making a mask while not writing all the digits
    - `<<` - Left shift
        - "multiply by 2"
        - Good for making a mask while not writing all the digits
    - `&`  - Bitwise AND
        - "determine if a bit is on"
    - `|`  - Bitwise OR
        - "turn a bit on if it's off and leave the rest on"
    - `^`  - Bitwise XOR
        - "flips a bit wherever there's a 1 in the mask"
        - ex: `0b0110 ^ 0b1101 = 0b1011`
    - `~`  - Bitwise NOT
        - Equivalent to adding 1 to the number and making it negative
- ex: flip nth bit

        num = num ^ 0b1 << (n - 1)

- Denoting bases
    - base 2 - `0b<number>`
    - base 8 - `0o<number>`
    - base 16 - `0x<number>`

- Helpful functions
    - `bin(num)`
        - Returns binary representaion of num as a STRING
        - Can input binary, decimal, hex, etc (not string)
    - `hex(num)`
        - Returns hexadecimal representation of num as a STRING
    - `oct(num)`
        - Returns octadecimal representation of num as a STRING
    - `int(<num as another type>[, baseTheNumCurrentlyIsIn])`
        - Normally converts the num as another type to an integer
        - If num is a string, the optional parameter converts it to decimal (int)




## Strings
========

### \*\*\*NOTE THE PRESCENCE AND LACK OF . BEFORE THE FUNCTION NAME\*\*\*
`s[index]`
- returns char at index

`s[start:end:stride]`
- Returns substring from [start,end) with the step stride
- Note that both start and end are optional
- stride - like a step

<br/>

- To reverse a string
    - `s[::-1]` or `reversed(s)`
- String Encoding declarations- `'str'`, `u'str'`, `r'str'`
    - Are equivalent. They're strings represented in different ways
    - u => Unicode
    - r => Raw
    - Convert among them with raw(str), unicode(str), str(str)
- To remove a character
    ex: `s = s[:3] + s[4:]`
    ex: `s = s.replace("old", "")`
- Functions
    - `ord(char)`
        - returns ASCII code of that character
    - `chr(<ascii code>)`
        - returns character represented by that ASCII code
    - `len("string")`
        - returns length of string
    - `len(string)`
        - returns length of string
    - `max(string)`
        - returns character w/ highest ASCII value in that string
    - `min(string)`
        - returns character w/ lowest ASCII value in that string
    - `str1 in str2`
        - returns whether str1 appears in str2
            - ^^ boolean True/False O.o
    - `str1 <string comparison> str2`
        - `>`,` <`, `<=`, `>=`    compares ASCII values
        - `==`, `!=`      check by value (not memory location)
    - `isalnum(str)`
        - returns if the string is alphanumeric
    - `isalpha(str)`   
        - returns True if string contains only alphabets
    - `isdigit(str)`  
        - returns `True` if string contains only digits
    - `isidentifier(str)`   
        - return `True` is string is valid identifier
    - `isspace(str)`   
        - returns `True` if string contains only whitespace
        - includes `"\t"`, `"\n"`, etc
    - `endswith(s1: str)`
        - returns `True` if strings ends with substring s1
    - `startswith(s1: str)`
        - returns `True` if strings starts with substring s1
    - `count(substring)`
        - returns number of occurrences of substring the string
    - `.find(s1)`
        - returns lowest index from where s1 starts in the string, if string not found returns -1
        - INDEXOF()! My love!
    - `.rfind(s1)`
        - returns highest index from where s1 starts in the string, if string not found returns -1
    - `.lower()`
        - return string by converting every character to lowercase
    - `.upper()`
        return string by converting every character to uppercase
    - `.split("str")`
        - Returns a list that has elements separated by str
        - The "str" is removed
    - `.replace(oldStr, newStr[, numTimes])`
        - No numTimes - returns str with every occurrence of old string replaced with new string
        - numTimes - Number of oldStrs to be replaced at maximum
    
    
    
## Console Functions
==============

`touch <filename.txt>`
- Creates filename.txt in the current directory

`print var1[, var2, var3, ...]`
- ex: print p
- print out to console
- if variable is an array, prints like [0.1, 0.2] (array elements)
- NOTE: print (with nothing afterwards) prints an empty line
- \*\*Putting multiple variables seperated by commas seperates them by a space
- \*\*print var, means that the next print statement will print on the same line

`print("Number: %d, String: %s") % (my_num, my_str)`
- prints the string with %d's, %s's, etc replaced by the nth variable in ()

`print(var[, end="string"])`
- prints the variable
- end- prints "string" after printing the var
    - default = "\n"

`input("Question")`
- prints question to console and returns the string response
- NOTE: Returns a string, so to compare numbers, do int(input)



## Keywords
========

`break`
- exits the for loops

`in`
- Returns whether the var is in the list
- ex: x in range(8) == true
- ex: x not in range(8) == false

`lambda`
- Creates an anonymous function (define functions in-line)
- Good for passing functions as parameters to functions
- `lambda <parameters>: <return expression>`
    - Don't have to have a parameter but must have a return
        - ex: `(lambda: 3)() returns 3`
- ex: `foo(lambda x: x % 3 == 0)`
    - `foo()` can use that function as a parameter (renamed in the foo())
- ex: `lambda x: lambda: x`
    - Returns a function that returns a number
- ex: `lambda f: f(4)`
    - Use a function as a parameter
- Used with `filter()`

`pass`
- Doesn't do anything. It's a good placeholder
    - (; would throw a syntax error)



## File I/O
========

- Open a file

            f = open("filename.txt", "w")

   - Then you can f.write, f.close, f.read, etc
- Functions that can't be directly invoked
    - `__enter__()`
    - `__exit__()`
        - Automatically closes the file afterwards like .close()
            ex: 

                    with open("filename", "w" as textfile:
                        textfile.write("Success")
                        <read or write to file>

- Attributes
    - `closed`
        - Returns True if the file is closed (eg: with .close())
        - Returns False if otherwise
- Functions
    - `open("filename.txt", "mode")`
        - "filename.txt" is the filename
        - "mode" - 
            - "w" - write
            - "r" - read
            - "r+" - read and write
            - "a" - append to the end of the file
    - `.close()`
        - Must be done or else text won't be written properly
        - nd you can't read until you're "done" writing
    - `.read()`
        - Returns literally the whole text file lmao
    - `.readline()`
        - Returns a line from the file, including the newline
    - `.write(str)`
        - MUST BE A STRING (use `str()`)
        - Does not add newlines ("\n"); must do it yourself


## Multiprocessing
==============

- `multiprocessing.Queue`

        >>> q = Queue()
        >>> q.put('something')
        >>> q.get()
        'something'
        >>> q.get() --> blocks and waits forever




## Built-in Functions
==================

`abs(var)`
- Returns abs value of number
- Only takes one number

`dir([obj])`
- Returns obj's list of attributes
- If no obj parameter - returns list of names in current local scope
- ex: `import math` -> `dir(math)` is list of vars/funcs in math module
- Can print dir(obj) to get all attributes

`enumerate(list)`
- "supplies a corresponding index to each element in the list that you pass it"
- Good for for loops
- Get an index while still using a for-each loop

`filter(function, list)`
- Returns list of elements in list that return True when passed through function
- function- can be made anonymously with lambda keyword

`id(var)`
- returns memory address of var
- `id(var1) == id(var2)` to see if both point to same object

`max(var)`
- Returns max value of var
- See `min(var)`

`min(var)`
- Returns minimum value of var
    - its value if it's one number
    - the lowest in the iterable if it is one
- Best to use it with integers and floats only (not strings)
- Takes any number of arguments

`range(stop)`
- Returns list with numbers 0 to stop - 1

`range(start, stop)`
- Returns list with numbers start to stop - 1

`range(start, stop, step)`
- Returns list with numbers start to stop - step with step step :P

`reversed(str)`
- Returns the string with characters in reverse order

`str(obj)`
- Returns a string containing a nicely printable version of the object
- Think of toString() from Java

`sum(list)`
- Returns the sum of the values in list
- Only for numbers

`type(obj)`
- Returns type of obj
- ex: `1 => <type 'int'>, 2.0 => <type 'float'>, "hi" => <type 'str'>`
- ex: `type(1.0) == float, type(1) == int`

`zip(list1, list2[, list3, list4, ...])`
- Gives pairs of items from each list. Good for for loops
- Will stop with the shorter list
- ex: `zip([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)]`
    - Access result with` result[0][0] == 1`
    - The () are tuples O:



## Cool Modules (like libraries)
=============================

- Generic import- `import <module name>`
    - Must use module.function_name() to use function
    - ex: import math
- Function import- `from <module name> import <function/variable>`
    - Imports only that function from module
    - Can use function_name to use function instead of module.function()
    - ex: import sqrt from math
Universal `import- from <module name> import *`
    - Imports all functions/variables from the module and don't use module.function()
    - Makes code confusing b/c high possibility of conflicting names
- Use functions/variables from:
    - `math`
        - `sqrt(x)`
        - returns square root of x
    - `random`
        - `randint(min, max)`
        - generates random integer from min to max inclusive
    - `from numpy import np`
        - good for vectors, matrices (2D arrays w/ extra features), and arrays (any dimension)
        - matrices can use * to multiply (not arrays)
        - `arr[::3]` etc works
        - `arr1 + arr2` is addition of elements and not concatenation (reg lists)
        - `.arange(start,end,step)`
            - Returns NumPy array with numbers step away from each other from start to end exclusive
        - `np.zeros([num_rows, num_cols])`
            - Returns NumPy array that contains all 0s
        - `np.eye(n)`
            - Returns identity NumPy array with n rows and n cols
        - `np.empty([m,n], dtype=np.int)`
            - Returns empty m x n NumPy array with datatype int inside
        - `np.matrix([[a11, a12], [a21, a22]])`
            - Returns matrix with initial values
        - `np.linspace(start, stop, num_divisions)`
            - Returns NumPy array that has num_division numbers from start to stop equally spaced
        - `np.concatenate([arr1, arr2, ...], axis)`
            - Returns concatenation of arrays
            - axis 
                - = 0 => stack vertically (1 ontop of another)
                - = 1 => stack horizontally
            - or np.vstack([arr1, arr2]) and np.hstack([arr1, arr2])
        - `.flatten()`
            - Returns array in one dimension
        - `.reshape([m, n, ...])`
            - Returns array with that many rows/columns/any other dimension
            - To get a 1D vector, just put a number inside
        - `np.transpose(arr)`
            - Returns transpose of arr
            - Also: `mat.T`
        - `np.linalg.inv(arr)`
            Returns inverse of arr
        - `np.linalg.solve(a, b)`
            - solves `Ax = b`. And returns as an array
        - `np.dot(arr1, arr2)`
            - Returns the result of matrix multiplication btwn arr1 and arr2
            - Order matters
        - `np.floor(num)`
        - `np.ceil(num)`
        - `np.max(arr)`
            - Returns max in an array
        - `np.min(arr)`
        - `np.argmax(arr)`
            - Returns index of max in an array
        - `np.argmin(arr)`
        - `np.multiply(a, b)`
            - Returns the multiplication of a and b element-wise
        `- np.roll(arr, num_cells_to_roll, axis)`
            - Shifts cells and puts the excess on the other side
            vNo need axis arg for 1D array
        - `np.diagonal(arr)`
            - Return diagonal elements of arr in another arr
    - `argparse`
        - `.ArgumentParser(description="desc")`
            - creates parser that you can do:
            - `.add_argument("--parsed_name?", "-shortname", action='store_true',help="Runs strategy experiments")`
            - `.parse_args()`
                - Returns parsed arguments in a... struct?
                - `args.parsed_name`
                    - Boolean. 
                        - `True`- was included when running the file
                        - `False`- not included when running the file
    
