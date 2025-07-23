### 📘 **Python `iter()` – Quick Notes**

---

### 🔹 What is `iter()`?

* A built-in function to create an **iterator** from an **iterable**.
* Syntax:

  ```python
  iter_obj = iter(iterable)
  ```

---

### 🔹 How It Works:

* `iter()` returns an object with `__next__()` method.
* Use `next()` to get values one by one.
* Stops with `StopIteration` when done.

---

### 🔹 Practical Uses of `iter()`:

| Use Case                   | Example / Description                                     |
| -------------------------- | --------------------------------------------------------- |
| **Manual iteration**       | `next(iter(data))` – control how much to read             |
| **File reading**           | `iter(file)` – read line-by-line efficiently              |
| **Custom stop condition**  | `iter(callable, sentinel)` – loop until a value is hit    |
| **Custom iterator class**  | Define `__iter__()` and `__next__()` in user classes      |
| **Lazy evaluation**        | Process large data without loading everything into memory |
| **Sensor / input streams** | Use in IoT or simulations to fetch values until stop      |

---

### 🔹 Example:

```python
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
```

```python
# Custom stop
import random
for val in iter(lambda: random.randint(1, 10), 5):
    print(val)
```

---

### ✅ Summary:

* `iter()` is **essential** for memory-efficient loops, custom data streams, and precise control over iteration.
* Very useful in **file handling, data pipelines, real-time input, and custom classes**.
