# Lesson 1: Introduction to the Python elective

<div align="right">
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson-02-Introduction-to-Python-and-Python-Strings/blob/master/README.md">next</a>
</div>

> Agenda 08-02-2019

## Topics today
Today will be an "overview" and "installation" day. We need to be on the same level before we start. You will furthermore get an introduction to the unix filesystem and commandline and you will have exercises in controling your computer through the commandline. 

## Required reading
* [Learning Objectives](/other_materials/learning_objectives.md)
* [Installations](/other_materials/installation.md)
* [Unix Commands](/other_materials/unix_commands.md)
* [Exercise: Unix Commands](/exercises/UNIX_commands.md)

### Supplementary reading
* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
* [Git Tutorial](/other_materials/git-tutorial.md)

## Exercises
* [Unix Commands](/exercises/UNIX_commands.md)

## Installation
* [Instalations for this semester](/other_materials/installation.md)
* Special for Mac OS: [Create an alias python/python3](/other_materials/mac_alias.md)
 

## How will our development enviroment look like this semester?
* Windows
* Mac
* Linux

> [Code example](code_from_today/hello.py)

## Course overview

![](other_materials/src/python_semester.png)

## Teachings / Exercises
* [Teaching Plan](https://python-elective-1-spring-2019.github.io/)  
---
* Techings 6 lektions a week for 15 weeks.  
    * Teachings - Exercises - Recap  
---

## The UNIX File system and Terminal Commands
* [Unix Commands](/other_materials/unix_commands.md)
* [Exercise: Unix Commands](/exercises/UNIX_commands.md)
---
* If you want to chalenge yourself this semester:
    * [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
    * [Ubuntu](https://www.ubuntu.com/)
---

## Exam & Mandatory Assignments
* 2 Mandatory assignments
    * 1 in the middle
    * 1 in the end 
* Exam
    * Not settled yet, either
        * 24 hours written assignment
        * 30 minutes oral exam
    <!--* 24 hour exam
        * You get 10 randomly chosen exam questions/assignments
        * You are evaluated on 
          * "Correct code"
          * Code quallity
            * Test cases
            * Documentation
            * Finnish -->

## What is Python used for?
* Youtube
* Google
* Spotify
* Reddit
---
* Machine learning
* Linkedin / Jobindex

## Why did you choose this elective? 

### What can you expect


## Required and Supplementary readings
* [Python docs](https://docs.python.org/3.7/index.html)
* [Real Python](https://realpython.com/)

<div align="center">
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson-02-Introduction-to-Python-and-Python-Strings/blob/master/README.md">next</a>
</div>

# Lesson 02: Introduction to python and python strings
<div align="right">
<a href="../../../Lesson-01-Introduction-to-the-Python-elective/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson_03_Python_Types_simple_types_Lists_Tuples_and_Sorting_Functions/blob/master/README.md">next</a>
</div>

> Agenda 19-02-2019

Today we will jump into the python programming world. You will get an overview of the language and you will start to get familiar with the language and the development enviroment. We will focus these first lesson on strings and string manipulations.
## Required reading
* [3. An Informal Introduction to Python](https://docs.python.org/3.7/tutorial/introduction.html#an-informal-introduction-to-python)
* [3.1. Using Python as a Calculator](https://docs.python.org/3.7/tutorial/introduction.html#using-python-as-a-calculator)
* [3.1.1. Numbers](https://docs.python.org/3.7/tutorial/introduction.html#numbers)
* [3.1.2. Strings](https://docs.python.org/3.7/tutorial/introduction.html#strings)
* [Text Sequence Type — str](https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str)
* [String Methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods)
* [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
* [4.1. if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)


### Suplementary reading
* [RealPython Search results for "string"](https://realpython.com/search?q=string)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [Splitting, Concatenating, and Joining Strings in Python](https://realpython.com/python-string-split-concatenate-join/)


## Exercises

* [string1.py](exercises/string1.py)
* [string2.py](exercises/string2.py)
* [Solutions](exercises/solution/)
<!--
* [letter_change.py](exercises/letter_change.py)
* [Python Strings and Character Data Quiz](https://realpython.com/quizzes/python-strings/)
* [Python Strings and Character Data Quiz](https://realpython.com/quizzes/python-strings/)
-->

## Code from today
* [hello.py](code_from_today/hello.py)



## Strings

### Slicing
The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"

![](other_materials/hello.png)

* s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
* s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
* s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
* s[1:100] is 'ello' -- an index that is too big is truncated down to the string length

The standard zero-based index numbers give easy access to chars near the start of the string. As an alternative, Python uses negative numbers to give easy access to the chars at the end of the string: s[-1] is the last char 'o', s[-2] is 'l' the next-to-last char, and so on. Negative index numbers count back from the end of the string:

* s[-1] is 'o' -- last char (1st from the end)
* s[-4] is 'e' -- 4th from the end
* s[:-3] is 'He' -- going up to but not including the last 3 chars.
* s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

It is a neat truism of slices that for any index n, s[:n] + s[n:] == s. This works even for n negative or out of bounds. Or put another way s[:n] and s[n:] always partition the string into two string parts, conserving all the characters. As we'll see in the list section later, slices work with lists too. _(dev.google.com)_




<div align="center">
<a href="../../../Lesson-01-Introduction-to-the-Python-elective/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson_03_Python_Types_simple_types_Lists_Tuples_and_Sorting_Functions/blob/master/README.md">next</a>
</div>
# Exercise Solutions

* String1.py
* String2.py

Look in branches for alternative solutions# Lesson 3: Python Types, simple types, Lists, Tuples and Sorting
<div align="right">
<a href="../../../Lesson-02-Introduction-to-Python-and-Python-Strings/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson-04-Dictionary-Sets-Reading-and-Writing-Files/blob/master/README.md">next</a>
</div>

> Agenda 22-02-2019

Today we will talk about Lists and Tuples. We will also look at how to sort list and you will have some exercises covering the topic of today.  


## Required reading
* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [4.2. for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
* [4.3. The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
* [5.1. More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* [4.2. for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
* [4.3. The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
* [5.1. More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* [5.3. Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html#sorting-how-to)



### Suplementary reading


## Exercises
* [list1.py](exercises/list1.py)
* [list2.py](exercises/list2.py)
* [solutions](exercises/solution/)


## Sorting

![](other_materials/sorted.png)

<div align="center">
<a href="../../../Lesson-02-Introduction-to-Python-and-Python-Strings/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson-04-Dictionary-Sets-Reading-and-Writing-Files/blob/master/README.md">next</a>
</div>
# Lesson 4: Dictionary, Sets, Reading and writing files
Agenda 26-02-2019

## Required reading
* [5.5. Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [5.6. Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
* [5.7. More on Conditions](https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions)
* [5.8. Comparing Sequences and Other Types](https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)
* [5.4. Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
* [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [7.2.1. Methods of File Objects](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)
* [8.4. The try statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
* [8.5. The with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
* [Open](https://docs.python.org/3/library/functions.html#open)
* [file object](https://docs.python.org/3/glossary.html#term-file-object)


### Suplementary reading
* [Dictionaries in Python](https://realpython.com/python-dicts/)
* [Reading and Writing Files in Python (Guide)](https://realpython.com/read-write-files-python/)

## Exercises
* [words.py](exercises/words.py)
    * [small.txt](exercises/small.txt)
    * [alice.txt](exercises/alice.txt)
* [blabish.py](exercises/blabish.py)
* [Python Dictionaries Quiz](https://realpython.com/quizzes/python-dicts/)
* [Python Sets Quiz](https://realpython.com/quizzes/python-sets/)


# Lesson 5: Python Utilities and Modules
Agenda 01-03-2019


## Required reading
* [HOWTO Fetch Internet Resources Using The urllib Package](https://docs.python.org/3/howto/urllib2.html)
* [subprocess — Subprocess management](https://docs.python.org/3.7/library/subprocess.html#module-subprocess)
* [urllib — URL handling modules](https://docs.python.org/3/library/urllib.html#module-urllib)
* [urllib.request — Extensible library for opening URLs](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
* [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [8.4. The try statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
* [8.5. The with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
* [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

## Suplementary reading
* [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
* [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/)

## Exercises
* [Mandatory Assignment](https://github.com/python-elective-1-spring-2019/Lesson-07-Required-reading-Exercise/blob/master/exercises/README.md)

<!-- * [copy.py](copy/copy.py) - _(To practice the file system and external-commands material)_
    * [xyz_hello.txt](copy/xyz_hello.txt)
    * [zz__something__.jpg](copy/zz__something__.jpg) 
* [puzzle.py](puzzle/puzzle.py) - _(To practice the urllib material)_
    * [animal_code.com](puzzle/animal_code.com)
    * [place_code.com](puzzle/place_code.com)
--># Lesson 6: Git, Markdown and Required reading Exercise
Agenda 05-03-2019


## Required reading

* [Mandatory Assignment: Required reading Exercise](https://github.com/python-elective-1-spring-2019/Lesson-07-Required-reading-Exercise/blob/master/exercises/README.md)
* [The Markdown syntax](other_materials/markdown.md)

### Supplementary reading

* [Git Tutorial](other_materials/git-tutorial.md)
* [How to Learn Python in Five Minutes](https://www.youtube.com/watch?v=ohr6O78jGzs)

# Lesson 7: Required reading Exercise
Agenda 08-03-2019

# Mandatory Assignment: Required readings List
> Mandatory Assignment: creating a Required readings List from the _## Required reading paragraph_ in the readme files, on github.

All the following should be done through Python, not manually. Even though there are many ways to solve the subtasks in this exercise you should only use the elements we covered so far. 

## Requirements for the application
The overall function of this application is that it should be able to generate a **required_reading.md** file containing a list of the litterature you will need to be familiar with at the exam in the end of this semester. An example of this can be seen [here](https://github.com/clbokea/required_reading/blob/master/required_reading.md)
For this, the application should be able to _clone_ and later _pull_ all repositories from the the github organization "Python Elective I spring 2019" (our classroom git repositories) and store it locally on your machine.   
Then it should loop through all the readme.md files and look for the bullet points contained in the _Required readings_ paragraph.  
Then it should write this collected list into a new file (required_reading.md) and push this file to a repository on your github account. The outcome will be that you have a list of links to the material/texts that is the curriculum of this python elective. 

## Step - by - step instructions
1. Get all repositories clone urls from the organization 'python-elective' and save them in a list, tuple, set or dictionary. For this you should make use of the [urllib](https://docs.python.org/3/library/urllib.html?highlight=urllib) module, and you can get all info about the repositories at this [api](https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100).  
_(Treat and read the json data as a text file. imagine something like a repository_info.txt. Then use the string searching and manipulations teqniques that we have worked with so far. Dealing with json data comes later this semester.)_    
2. Clone all repos from the organisation. (for this you will need the modul: [subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess))
    1. or if the repository is alredy cloned you should make sure that you have an up to date version of the repository by a _pull_ request. (for some of the tasks in this operation you will need the modul: [subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess) like before and for some you will need the module: [OS](https://docs.python.org/3/library/os.html?highlight=os#module-os)) 
3. Traverse through all repos locally and get the readme files content in a list ie. (for this you will need the module: [glob](https://docs.python.org/3/library/glob.html?highlight=glob#module-glob))
4. Search the content of the list and find the "## Required reading" paragraph and put the content of that paragraph into list.
4. Write the list to a required_reading.md in a new curriculum repository. (for this operation you will again need the modul: [OS](https://docs.python.org/3/library/os.html?highlight=os#module-os)) 
    1. The links in the readme file should be:
        1. Ordered Alphabetically
        1. Beginning character should be capitalized
        1. The list should look good/normal, e.g no blank bullet points, no whitepsaces in wrong places etc.
        1. No dublicate link should occour. 
5. push that repository to your own github account.

### Extra tasks
1. When this is done you should make your application able to dynamically handle the github api url, dynamically handle where on your computer the repositories should be stored. 
1. If a repo online is removed the application should be able to detect this and delete the local version of the repository. Thus keeping the list up to date.

## Project management
Follow the advice in the [5 minutes video](https://www.youtube.com/watch?v=ohr6O78jGzs) we watched in class.
1. First day (7 hours), messy coding
1. Second day (7 hours), Refactor your code into functions, modules ie. 
1. Third day (7 hours), focus on delivery, documentation, making the project ready for the presentation.

## Code Quality
You code should look good, and it should be easy to read. This means it should be commented, it should have nice variable/function names ie. 

## Error handeling
It is important that your application is robust. And you should handle the errors that might occour. 

## Resources
* [Github Api](https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100)
* [urllib](https://docs.python.org/3/library/urllib.html?highlight=urllib)
* [subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess)
* [glob](https://docs.python.org/3/library/glob.html?highlight=glob#module-glob)
* [OS](https://docs.python.org/3/library/os.html?highlight=os#module-os)
* [HOWTO Fetch Internet Resources Using The urllib Package](https://docs.python.org/3/howto/urllib2.html)

## Timeframe for this mandatory assignment
For this assignment you will have one week. You will at tuesday the 12/03 have to show what you did and explain your application to me (Claus) (for 5 minutes). You are allowed to work together and you are allowed to ask me (Claus) for help when we have lessons, but you should create an individual version of the assignment. (you can not present the assignment as a group). You will have to work on the assignment at home, and you will have time to work on the assignment in class at friday the 8/03, and on tuesday the 12th. The assignment will be evaluated with a "passed" og "not passed". 



&copy; KEA, Claus Bove, 04-01-2019
# Lesson 8: Required reading Exercise
Agenda 12-03-2019
<head>
  <style> 
    
    h1:first-of-type {display: none;}
    #github {text-align: right; margin:-50px 0 50px 0}
    #teachings {text-align: right; margin: 0px 0 10px 0}
    #tbl {display: inline-table}
    td {vertical-align: top;}
    thead th {background-color: #3a7090; color:#ffffff}
    td:nth-child(1) {color: #3a7090; text-align:center}
  </style>
</head>
# Python Elective I Spring 2019

<!-- <div id="github"><a href="https://github.com/python-elective-1-spring-2019/">GitHub</a>
</div> -->

<div id="teachings">
  Teachings: <br> Tuesdays: 08:30 - 11:00<br>Fridays: 08:30 - 11:00<br> 
</div>

<table id="tbl">
  <thead>
  <tr>
      <th>Date</th>
      <th>Topic</th>
      <th>Notes</th>
  </tr>
  </thead>
  <tbody>
  <tr>
      <td>1</td>
      <td>    
        <a href="https://github.com/python-elective-1-spring-2019/Lesson-01-Introduction-to-the-Python-elective/blob/master/README.md">Lesson 1: Introduction to the Python elective</a></td>
    <td></td>
  </tr>
  
  <tr>  
      <td>1</td>
      <td>
        <a href="https://github.com/python-elective-1-spring-2019/Lesson-02-Introduction-to-Python-and-Python-Strings/blob/master/README.md">Lesson 2: Introduction to Python and Python Strings</a></td>
      <td></td>
  </tr>
  
  <tr>
      <td>2</td>
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-03-Python-Types-simple-types-Lists-Tuples-and-Sorting/blob/master/README.md">Lesson 3: Python Types, simple types, Lists, Tuples and Sorting, Functions</a></td>
      <td></td>
  </tr>
  
  <tr>    
      <td>2</td>
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-04-Dictionary-Sets-Reading-and-Writing-Files/blob/master/README.md">Lesson 4: Dictionary, Sets, Reading and Writing Files</a></td>
      <td></td>
  </tr>
  
  <tr>
      <td>3</td>
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-05-Python-Utilities-and-Modules/blob/master/README.md"><s>Lesson 5: Python Utilities and Modules</s></a></td>
      <td></td>
  </tr>  
  
  <tr>    
      <td>3</td> 
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-05-Python-Utilities-and-Modules/blob/master/README.md">Lesson 5: Python Utilities and Modules</a><br>
      
      <a href="https://github.com/python-elective-1-spring-2019/Lesson-06-Git-Markdown-and-Required-reading-Exercise/blob/master/README.md">Lesson 6: Git, Markdown and the Mandatory "Required reading Exercise"</a></td>
      <td></td>
  </tr>
    <tr>     
      <td>4</td>
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-07-Required-reading-Exercise/blob/master/README.md">Lesson 7: Mandatory "Required reading Exercise"</a></td>
      <td></td>
  </tr>
    <tr>
      <td>4</td>
      <td><a href="https://github.com/python-elective-1-spring-2019/Lesson-08-Required-reading-Exercise/blob/master/README.md">Lesson 8: Mandatory "Required reading Exercise" presentation</a></td>
      <td></td>
  </tr>
    <tr>   
      <td>5</td>
      <td><a href="">Lesson 9: Unit Tests</a></td>
      <td></td>
  </tr>
    <tr>  
      <td>5</td>
      <td><a href="">Lesson 10: Classes, OOP, Virtual Environments and Packages</a></td>
      <td></td>
  </tr>
  <tr> 
      <td>6</td>
      <td><a href="">Lesson 11: Classes, OOP, Generators, </a></td>
      <td></td>
  </tr>
  <tr>      
      <td>6</td>
      <td><a href="">Recursion, Searching, Sorting, Merging Algorithms</a></td>
      <td></td>
  </tr>
  
  <tr>  
      <td>7</td>
      <td><a href="">Searching, Sorting, Merging Algorithms</a></td>
      <td></td>
  </tr>
  
  <tr> 
      <td>7</td>
      <td><a href="">Searching, Sorting, Merging Algorithms</a></td>
      <td></td>
  </tr>

  <tr>  
      <td>8</td>
      <td><a href="">Searching, Sorting, Merging Algorithms</a></td>
      <td></td>
  </tr>
  
  <tr> 
      <td>8</td>
      <td><a href="">Searching, Sorting, Merging Algorithms</a></td>
      <td></td>
  </tr>
  <tr >
      <td>9</td>
      <td style="background-color: #3a7090; color:#fff">Easter Holliday</td>
      <td style="background-color: #3a7090; color:#fff"></td>
  </tr>
  <tr >
      <td>9</td>
      <td style="background-color: #3a7090; color:#fff">Easter Holliday</td>
      <td style="background-color: #3a7090; color:#fff"></td>
  </tr>
  <tr> 
      <td>10</td>
      <td><a href="">Threads, Sockets & Chat Server</a></td>
      <td></td>
  </tr>
  <tr>
      <td>10</td>
      <td><a href="">Sockets & Chat Server</a></td>
      <td></td>
  </tr>
  <tr>
      <td>11</td>
      <td><a href="">JSON, Datetime, CSV files</a></td>
      <td></td>
  </tr>
  <tr>
      <td>11</td>
      <td><a href="">Functions, Map, Filter, Reduce, decorators, Lambda, List Comprehensions, Generator expressions</a></td>
      <td></td>
  </tr>
  <tr>
      <td>12</td>
      <td><a href="">Functions, Map, Filter, Reduce, decorators, Lambda, List Comprehensions, Generator expressions</a></td>
      <td></td>
  </tr>
  <tr>
      <td>12</td>
      <td style="background-color: #3a7090; color:#fff">No Teachings - St. Bededag</td>
      <td style="background-color: #3a7090; color:#fff"></td>
  </tr>
  <tr>
      <td>13</td>
      <td><a href="">Test Exam</a></td>
      <td></td>
  </tr>
  <tr>
      <td>13</td>
      <td><a href="">Test Exam</a></td>
      <td></td>
  </tr>
  <tr>
      <td>14</td>
      <td><a href="">Evaluation & Recap</a></td>
      <td></td>
  </tr>
  <tr>
      <td>14</td>
      <td><a href="">Test Exam II</a></td>
      <td></td>
  </tr>
  <tr>    
      <td>15</td>
      <td><a href="">Test Exam II</a></td>
      <td></td>
  </tr>
  <tr>
      <td>15</td>
      <td><a href="">Evaluation II & Recap</a></td>
      <td></td>
  </tr>

  </tbody>
</table>
            
\* Changes to this plan can occour. <br>

__Teacher: Claus Bové (clbo@kea.dk)__

<script>
 var dates = [

        {week : 1, date : '08-02'},

        {week : 2, date : '19-02'},
        {week : 2, date : '22-02'}, 

        {week : 2, date : '26-02'}, 
        {week : 2, date : '01-03'}, 

        {week : 3, date : '05-03'}, 
        {week : 3, date : '08-03'},

        {week : 4, date : '12-03'}, 
        {week : 4, date : '15-03'},

        {week : 5, date : '19-03'}, 
        {week : 5, date : '22-03'}, 

        {week : 6, date : '26-03'}, 
        {week : 6, date : '29-03'}, 

        {week : 7, date : '02-04'}, 
        {week : 7, date : '05-04'},

        {week : 8, date : '09-04'},
        {week : 8, date : '12-04'},

        // week 9 Easter
        {week : 9, date : '23-04'},        
        {week : 9, date : '26-04'},

        {week : 10, date : '30-04'},
        {week : 10, date : '03-05'},

        {week : 11, date : '07-05'},
        {week : 11, date : '10-05'},

        {week : 12, date : '14-05'},
        {week : 12, date : '17-05'}, // st. bededag

        {week : 13, date : '21-05'},
        {week : 13, date : '24-05'},

        {week : 14, date : '28-05'},
        {week : 14, date : '31-05'},

        {week : 15, date : '04-06'},
        {week : 15, date : '07-06'}

    ]; 
  
 var table = document.getElementById("tbl");  
 var rows = table.getElementsByTagName("tr");
 
 for(i = 1; i < rows.length; i++){

     if(rows[i].getAttribute("class") === 'holliday'){
        i++;   
     }

      var tds = rows[i].getElementsByTagName("td"); 
      tds[0].innerHTML= dates[i-1].date + '-2019'; 
      // tds[1].innerHTML= dates[i-1].date + ' - 2018';  
    } 
 
</script>
