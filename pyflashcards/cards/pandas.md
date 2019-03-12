##### Question
What is a key difference between pandas Series and NumPy array?

##### Answer
A pandas Series can have an explicitly defined index of any type.

##### Tags
week 2, beginner, pandas

----
##### Question
Manually code a pandas Series of integers.

##### Answer
```python
>>> data = pd.Series([1, 2, 3])
>>> data
0    1
1    2
2    3
dtype: int64
```

##### Tags
week 2, beginner, pandas

----
##### Question
Return the values of a pandas Series. What object type is it?

##### Answer
```python
>>> data = pd.Series([1, 2, 3])
>>> data.values
[1 2 3]
>>> type(data.values)
<class 'numpy.ndarray'>
```

##### Tags
week 2, beginner, pandas

----
##### Question
Which standard python type is the pandas Series somewhat a specialization of? How so?


##### Answer
A dictionary. A dictionary is a structure that maps arbitrary
keys to a set of arbitrary values, and a Series is a structure
which maps typed keys to a set of typed values. The type
information of a Pandas Series makes it much more efficient
than Python dictionaries for certain operations.

##### Tags
week 2, beginner, pandas

----
##### Question
How can a pandas DataFrame be constructed?

##### Answer
* a single Series object
* a list of dicts
* a dictionary of Series objects
* a two-dimensional NumPy array
* a NumPy structured array

##### Tags
week 2, beginner, pandas

----
##### Question
How is a pandas Index object similar to a python set? How is it
different?

##### Answer
They are both immutable, and both support union, intersection, etc. operations.

However, an Index can contain duplicates.

##### Tags
week 2, beginner, pandas

----
##### Question
What is the benefit of using object methods instead of operators when applying ufuncs to Series/DataFrames?

e.g. `A + B` versus `A.add(B)`

##### Answer
The object method takes `fill_value` and `axis` arguments.

##### Tags
week 2, beginner, pandas
