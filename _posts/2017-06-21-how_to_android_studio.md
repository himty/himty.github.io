---
layout: post
title: How to Android Studio
author: Jenny Wang
comments: true
tags:
- coding_notes
minutes: 3
---

## PIXELS AND SCREEN COMPATIBILITY
================================

`dp to pixels`
- float scale = getResources().getDisplayMetrics().density;
- numPixels = (int) (dp * scale + 0.5f);

`ViewConfiguration`
- .get(myContext).getScaledTouchSlop()
    - returns int of the distance in pixels a touch
    - can wander before we think the user is scrolling


## android.util package
=====================

`Log`
- log stuff to console
- .i
    - information
- .e
    - error
- .d
    - debug


## USER INPUT
=======

`Button`
- android:onClick- the function to call when button is clicked
- alternative\/\/\/

        .setOnClickListener(new View.onClickListener() {
            @Override
            public void onClick(View v) {
                //do something
            }
        }

`ImageButton`
- a button that can have an image on it
- see Button

`CheckBox`
- yes/no input
- checkBoxElem.isChecked()
    - to get yes/no

`Spinner`
- dropdown menu but in popup form
- selection choices are strings in an array in strings.xml
    - see string arrays in strings.xml below
- spinnerElem.getSelectedItem().toString()
    - to get selected item

`EditText`
- collect text input
- lines- number of lines the textbox will have
- editTextElem.getText().toString()
    - to get entered text

## LAYOUT
=======

`ScrollView`

    <ScrollView></ScrollView>

- things inside are scrollable

`LinearLayout`
- one thing after another

        <LinearLayout>
            <Element/>
            <Element/>
        </LinearLayout>
    


## strings.xml
===========

- stores app-wide string values/names

        <string-array name="name">
            <item>@string/stringName</item>

    - accessed with @array/name

```
<color name="white">#FFFFFF</color>
```

- add color
- can be accessed in code w/ @color/white


## METHODS
========

`findViewById(int id)`
- get an element from the UI
- ex: final EditText nameField = (EditText)findViewById(R.id.EditText'sId);
    - where EditText'sId is found in id="@+id/EditText'sId"

`getBaseContext()`
- returns base context (replaces this)

`finish()`
- sends activity to the background