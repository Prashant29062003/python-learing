
---

## 🔄 `yield` in Python – Quick Notes

### 📌 What is `yield`?

* `yield` is like `return`, **but it pauses** the function and **remembers its state**.
* When the function is called again, execution **resumes from the last `yield`**.
* A function with `yield` is called a **generator**.

---

### 🔍 Generator Function:

```python
def my_gen():
    yield 1
    yield 2
    yield 3
```

```python
for val in my_gen():
    print(val)
```

🖨️ Output:

```
1
2
3
```

---

### ✅ Example 1: Yield Even Numbers

```python
def print_even(lst):
    for i in lst:
        if i % 2 == 0:
            yield i

for val in print_even([1, 4, 5, 6, 7]):
    print(val, end=" ")
```

🖨️ Output:

```
4 6
```

---

### ✅ Example 2: Infinite Square Generator

```python
def nextSquare():
    i = 1
    while True:
        yield i*i
        i += 1

for num in nextSquare():
    if num > 100:
        break
    print(num)
```

🖨️ Output:

```
1 4 9 ... 100
```

---

### ✅ Example 3: Count Word Occurrence with `yield`

```python
def find_geeks(words):
    for word in words:
        if word == "geeks":
            yield word

text = "geeks are known for teaching other geeks and geeks again".split()
print("Count:", sum(1 for _ in find_geeks(text)))
```

🖨️ Output:

```
Count: 3
```

---

## ✅ Advantages of `yield`:

* 💾 **Memory efficient** (no need to store entire list in memory)
* ⏱️ **Faster for large data** (resumes instead of restarting)
* ♻️ Maintains **state between iterations**

---

## ❌ Disadvantages:

* ❗ Can be **harder to debug**
* 🔄 **Logic becomes complex** if not used properly

---

## 🧠 Use When:

* You want to **process large data** piece by piece
* You want **lazy evaluation**
* Writing **infinite** or **on-demand** sequences

---
