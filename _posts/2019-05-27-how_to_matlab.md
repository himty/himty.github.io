---
layout: post
title: How to MATLAB
author: Jenny Wang
comments: true
tags:
- coding_notes
minutes: 3
---

## Numerical Data Structures
==========================

`cell`

`vector` = row/column

`matrix` = group of vectors
- is a rectangle

`array `= 3d matrix

Initialize matrix
    ```
    matrix = [1 1;2 2]
    ```
- `;` = new row
- `<space>` = next column

Specify # of cells
- `matrix = zeros(numRows, numColumns)`
- `matrix = ones(numRows, numColumns)`
    - or `ones([numRows numColumns])`

Call data from all numRows rows or numColumns columns
- replace with :
- ex: `matrix(:,4)`

`vector = [1:100]`
- fills vector with numbers 1 to 100

`vector(row, col) = 10`
- change cell value

`vector(row, col)`
- get number and print it out

`sum(vector)`
- sums all numbers in vector

`prod(vector)`
- multiply everything in vector

Math between two vectors/matrices
- use `+`, `-`, `*`, `/`

Math between correlating cells in vectors/matrices
- use `+`, `-`, `.*`, `./`

`vector = vector';`
- make the row vector into a column vector

`matrix(:)`
- take all cells in the matrix

# =================================================

## Other Data Structures
=======================

Strings are in single quotes ''

`num2string(var);`
- change data type

`string2num(var);`
- change data type

# =====================================

## Miscellaneous Syntax
=======================

`NaN` = null

`%` = comment

`...` at the end of the line when you want to press enter
- ex: 
    ```
    var1 *...
    var2
    ```

- put semicolons in scripts
    - won't print onto command window

`lowerLimit:upperLimit`
- vector with all numbers from lowerLimit to upperLimit


`~` = not

`||` = or

`&&` = and

for loops
    ```
    for i = start:end
        %do something
    end
    ```

if statemtents
    ```
    if %condition
        %action
    else
        %action
    end
    ```

# ===============================

## Random Functions
==================

`vector = xlsread('fileName.extension')`
- Read Exel file

`image = imread('imagename');`
- read image

`linspace(start, end, n_points);`
- returns equally spaced points
- includes starting and end points

`[x,y] = meshgrid(xVector, yVector)`
- returns all possible coordinates of pts
- use with linspace

`size(vector, <row or column as in 1 or 2>)`
- returns numRows, numColumns
- don't specify row or column if want both

`imageB = imresize(imageA, scale);`

`imageB = imresize(imageA, [numRows, numCols]);`
- imageB has numRows rows and numCols cols
- or put NaN as one of them to preserve aspect ratio

`imshow(image);`
- make a window with the image on it

`sind(theta)`
- sin

`cosd(theta)`
- cos

`repmat(vector, numTimes)`
- repeat the vector numTimes horizontally and vertically

`repmat(vector, numRows, numColumns)`
- have that many total rows/cols
    
`shuffle(vector)`
- change up the order of all cells, use with repmat

`shuffle(vector, dimension)`
- dimension: 1 = Rows change, 2 = Columns change, 3 = next dimension changes, etc

`vertcat(vector, vector2, vector3, ...)`
- stacks vectors ontop of each other

`horzcat(vector, vector2, vector3, ...)`
- stacks vectors side to side

`RandStream.setGlobalStream(RandStream('mt19937ar', 'seed', sum(100*clock)));`
- put it everywhere just in case you want a random number (for real randomness)

`randperm(upperLimit, numCells);`
- can't get the same number twice

`randperm(upperLimit)`
- numbers 1~upperLimit are reordered

`randi(upperLimit);`
- get one random number

`randi(upperLimit, numRows, numCols);`
- random numbers in matrix numRows x numCols

`randi([lowerLimit, upperLimit]);`
- number from lowerLimit to upperLimit

`randsample(upperLimit, numCells);`
- numCells number of random numbers

`randsample([1 2 3], 2)`
- numCells number of rand numbers from the vector

`any(vector)`
- returns true if any of cells is nonzero

`floor(num)`
- returns num rounded down to whole number

`ismember(element, vector)`
- returns true if element is found inside the vector

`WaitSecs(seconds);`
- how long to wait

`GetSecs()`
- get seconds from start of program
- use to make sure the time intervals are right

`[keyIsDown, secs, keyCode] = KbCheck()`
- if have different keyboards, put 1/2/3/4/5 in parenthesis for specific keyboard
- keyIsDown = any button down (1 or 0 => true or false)
- secs = time from GetSecs()
- keyCode = key that is down
    - ex: strcmp('s', KeyName(keyCode)), see if it is 's'                                                                                                                                                                                         

`[x,y,clicks] = GetMouse()`
- x, y = mouse position coordinates
- if clicks = [0,0,0] => no click, [1, 0, 0] = left click
- test with any(clicks)

`GetClicks()`
- get number of mouse clicks

`strcmp(string1, string2)`
- returns true if identical, false if not

`string = strcat(string1, string2)`
- combine string1 and string2

`KeyName('UnifyKeyNames')`
- make codes from key presses the same from macs/windows/etc

`save(fileName, 'variable')`
- ex: `save('result', 'p', 'q');`
- save some variables in a file (.mat)

`string = upper(string)`
- all letters uppercase

`isdir(directoryString)`
- true if there already is a directory with that name, false if no
- example of directoryString is from pwd()

`mkdir(directoryString)`
- create a folder with directory directoryString

`sortrows(matrix, colNum)`
- make numbers in the colNum-th column be in ascending order

`resizem(input, scale)`

`resizem(input, [numRows, numCols])`
- expand and contract matrix




# ====================================================

## Command Line Commands
=======================

COMMANDS CAN BE PUT INTO SCRIPTS

`pwd`
- print your directory
- usage examples:
    ```
    rootDir = pwd();
    resultsDir = [rootDir '/results/']
    if ~isdir(resultsDir) %if don't have this directory already
        mkdir(resultsDir) %make the directory/folder
    end
    ```

`cd(folderName)`
- change directory
- go one level up => cd ..

`ls`
- list of files in the folder

`clear all`
- clears variables from other experiments

`clc`
- clear command window

# ===========================================

## Keyboard Shortcuts
====================

`ctrl+c then s then c then a then enter`
- bring back window (if it crashes)
- might need to alt+tab (switch windows) before doing above


# =================================================================

## Psychtoolbox
===============

A library for psychology experiments

Screen has many settings
- access w/ `Screen('something', <specific>, <more specific>, <etc>);`
- `Screen('CloseAll');`
    - closes all screens
- `Screen('Preference', 'SkipSyncTests', 1);`
    - yes to skipping sync tests

`[window, rect] = Screen('OpenWindow', 0, [], [500 500 700 700]); `
- open the window
    - 0 = open on this monitor
    - 1 = open on other monitor
- 2nd matrix = where the screen will be
- window = pointer
- rect = (startX, startY, endX, endY)
    - corner coordinates;
- Screen puts data into window/rect

`x = Screen('MakeTexture', window, uint8(image));`
- uint8 because colors in image can't be > 255

`Screen('DrawTextures', window, x);`
- draw the texture. x is from function above

`Screen('DrawTextures', window, tid(rand_oranges(i,:)), [], xy_rect, orientation);`
- xy_rect = corners of each picture 
- orientation = degrees of rotation=========================================================================

`A = Screen('Flip', window);`
- display onto monitor
- usually don't need A

`Screen('Flip', window, A + seconds);`
- show a blank screen (if nothing is made with window) second seconds later
- more accurate than WaitSecs()

`KbWait(); `
- wait for keyboard input before going on




- how to get rid of background of image
    - add transparent mask ontop
    - mask must be same size as image 