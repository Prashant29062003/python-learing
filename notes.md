# Python Inner Working

- python my_python.py

> ##  **source code** --> Byte Code (Mostly Hidden) --> **Python VM** (Virtual Machine)

--- 

1. Compile to Byte Code (Low level & Python Independent)

- Byte Code runs faster
> .pyc  --> Compiled python (**frozen Binaries**)

--- 

> ## **__ pycache __**

> Source Change & Python Version
--> hello_python.cpython-313.pyc
(here -> 313 is version of python)

- Works only for imported files

- not for top level files 


## **Python Vertual Machine (PVM)**

- Code loop to iterate byte Code
- Run time Engine
- A.K.A. Python Interpreter

## **Byte Code is Not Machine code**

- python specific interpretetion
- cpython(Standard Implementation) , jython, Iran Python, Stackless, PyPy


---

# mutable Immutable

- In python data is stored as objects so, when we declare some variable then it stored in memory i.e here the variable is pointing to the reference of that data type objects ( Integers, Floating-point numbers, Boolean, Strings, Tuples, Frozen set, Bytes ) --> Immutable Data-types

- And those data types which can be altered directly in memory then called Mutable Data-types (List, Set, Dictionary, Bytearray, Array).


```
x = 10
y = x


x --> y
i.e 
y --> 10

if
x = 20
y --> 10 (still remains with same reference)
```

> NOTE: basically those data types which are not altred in memory then called Immutable Data types.

> Here,
>- ( x = 10 )x has referenced to 10
>- (y = x) --> y take that refence i.e. pointing to the **'10' not 'x'**
>- (x = 20) now 'x' pointing to a new integer **but** y still pointing to 10 (reference)