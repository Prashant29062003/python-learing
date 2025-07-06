# Object Types / Data Types

## 1. Immutable Data Types
>- Number : 123, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
>- String : 'k', "Prashant", b'a\x01c', u'sp\xc4m'
>- Booleans : True, False
>- tuple : (1, 'span', 4, 'U'), tuple('spam'), namedtuple


## 2. Mutable Data types
>- List : [1, [2, 'three'], 4.5, list(range(10))]
>- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
>- Set : set('abc'), {'a','b', 'c'}
>- File : open('eggs.txt'), open('C:ham.bin', 'wb')


## Other Concepts
>- Functions
>- Modules
>- classes

## Advance
>- Decorators
>- Generators
>- Iterators
>- MetaPramming

---

# List vs Tuple Python
- In Python, tuples and lists are both used to store collections of items, but they have distinct characteristics and use cases. Here are the key differences:

>- Mutability: Lists are mutable, meaning their elements can be changed, added, or removed after creation. Tuples, on the other hand, are immutable, so their elements cannot be modified once they are set.
>- Performance and Memory Usage: Tuples are generally more memory-efficient and faster to iterate over compared to lists. This is because tuples are stored in a single memory block, while lists require extra space for dynamic resizing.
>- Use Cases: Lists are better for performing operations such as insertion and deletion, making them suitable for scenarios where the data needs to be modified frequently. Tuples are more appropriate for accessing elements efficiently and for data that should remain constant, ensuring data integrity.
>- Built-in Methods: Lists have more built-in methods for modifying the data, such as append(), extend(), and remove(). Tuples have fewer built-in methods, primarily for accessing and iterating over the data.
>- Hashability: Tuples can be hashable if they contain immutable elements, allowing them to be used as keys in dictionaries or elements in sets. Lists, being mutable, cannot be hashable.