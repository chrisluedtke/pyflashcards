##### Question
How could this code be improved?
```python
ls = [1,2,3]
for i in range(ls):
    print(i, ls[i])
```
##### Answer
```python
for i, item in enumerate(ls):
    print(i, item)
```
##### Tags
effective python

---

##### Question
How could this code be improved?
```python
ls = [1,2,3]
if len(ls) != 0:
    do_something()
```

##### Answer
Empty strings and lists implicitly evaluate to False.
```python
if ls:
    do_something()
```
##### Tags
item 2, effective python

---

##### Question
What's wrong here?
```python
>>> ls = [[0] * 3] * 3
>>> print(ls)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> ls[0][1] = 2
>>> print(ls)
>>> [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
```
##### Answer
Lists don't contain objects - they contain references to objects.
```python
>>> ls_row = [0] * 3
>>> ls = [ls_row.copy() for _ in range(3)]
>>> ls[0][1] = 2
>>> print(ls)
[[0, 2, 0], [0, 0, 0], [0, 0, 0]]
```
##### Tags
item 2, effective python

---
