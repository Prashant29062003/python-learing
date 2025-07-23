Here are short and easy-to-remember notes for `*args` and `**kwargs`:

---

### 🔹 `*args` – Positional Arguments (Tuple)

* Accepts **any number of positional** arguments.
* Stored as a **tuple**.
* Use when you don’t know how many **values** will be passed.

```python
def func(*args):
    print(args)
```

📌 `func(1, 2, 3)` → `(1, 2, 3)`

🧠 **Think**: `*args` = *All Regular (positional) stuff*

---

### 🔹 `**kwargs` – Keyword Arguments (Dict)

* Accepts **any number of keyword** arguments.
* Stored as a **dictionary**.
* Use when you don’t know how many **key=value** pairs will be passed.

```python
def func(**kwargs):
    print(kwargs)
```

📌 `func(a=1, b=2)` → `{'a': 1, 'b': 2}`

🧠 **Think**: `**kwargs` = *KeyWord ARGS*

---

### ✅ Quick Tip:

You can rename `args` or `kwargs` (e.g., `*values`, `**data`) — just keep the `*` and `**`.

---

Want a single-line cheat for both?
👉 `*args = many values`, `**kwargs = many key=values`
