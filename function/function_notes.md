# 🔧 Python Functions – Quick Notes

### 📌 1. **Definition & Syntax**

* A **function** is a reusable block of code.

```python
def function_name(parameters):
    """Docstring"""
    statement(s)
    return value
```

---

### 📌 2. **Types of Functions**

* **Built-in functions** – `print()`, `len()`, etc.
* **User-defined functions** – Created using `def`.

---

### 📌 3. **Calling a Function**

```python
def greet():
    print("Hello!")

greet()
```

---

### 📌 4. **Arguments**

* Values passed into the function.

```python
def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
```

---

## 🔹 Types of Arguments

### ✅ a. Default Arguments

```python
def myFun(x, y=50):
    print(x, y)

myFun(10)  # y takes default 50
```

### ✅ b. Keyword Arguments

```python
def student(firstname, lastname):
    print(firstname, lastname)

student(firstname='Geeks', lastname='Practice')
```

### ✅ c. Variable-Length Arguments

#### – `*args` (non-keyword positional)

```python
def myFun(*args):
    for a in args:
        print(a)
```

#### – `**kwargs` (keyword arguments)

```python
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

---

## 📘 5. **Docstring**

* First string in a function to describe it.

```python
def evenOdd(x):
    """Check if number is even or odd"""
    ...
print(evenOdd.__doc__)
```

---

## 🔁 6. **Return Statement**

```python
def square(x):
    return x ** 2

print(square(4))  # 16
```

---

## 🔄 7. **Pass by Reference**

* Python passes arguments by reference.

```python
def myFun(x):
    x[0] = 20

lst = [10, 11, 12]
myFun(lst)
print(lst)  # [20, 11, 12]
```

---

### ❗ Rebinding breaks the link

```python
def myFun(x):
    x = [20, 30, 40]  # Rebinding

lst = [10, 11, 12]
myFun(lst)
print(lst)  # [10, 11, 12]
```

---

## 🔒 8. **Function Inside Function (Nested)**

```python
def outer():
    msg = "Hello"

    def inner():
        print(msg)

    inner()

outer()
```

---

## 🕵️‍♂️ 9. **Anonymous (Lambda) Functions**

```python
cube = lambda x: x*x*x
print(cube(3))  # 27
```

---

## 🔁 10. **Function to Swap**

```python
def swap(x, y):
    temp = x
    x = y
    y = temp

x, y = 2, 3
swap(x, y)
print(x, y)  # 2 3 (No change)
```

---
