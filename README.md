# Mutable pass-by-reference/id

```py
a = [1, 2]
b = a
print(f"a : {id(a)}") # a : 2103974454592
print(f"b : {id(b)}") # b : 2103974454592
b[0] = 3 # we replace the first element of only ** b ** with 3 , but a also reflects the changes
print(f"a : {a}") # a : [3, 2]
print(f"b : {b}") # b : [3, 2]

```

→ Both `a` and `b` point to the same list (same memory `id`).  
Changing `b` also changes `a`.

### Output:

```py
a : 2103974454592 # same id
b : 2103974454592 # same id
a : [3, 2]
b : [3, 2]
```
# On Other Hand

If you do

```py
b = a.copy()
```

→ `b` becomes a new list with a different `id`.         
Changing `b` won’t affect `a`.

```py

a : [1, 2]
b : [3, 2]
```

# Immutable pass-by-value

```py
a = 10
b = a
b = 20

print(f"a : {id(a)}")
print(f"b : {id(b)}")
```
### output:
```py
a : 140715980039368
b : 140715980039688
```

* **Immutable (int, str, tuple, etc.)** → assigning a new value makes a new object, original stays same.
* **Mutable (list, dict, set, etc.)** → changes affect all references to that object.
