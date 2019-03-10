# QUESTION
What is a key difference between pandas Series and NumPy array?

# ANSWER

```
A pandas Series can have an explicitly defined index of any type.
```

# TAGS
week 2, beginner, pandas
-------------------------

# QUESTION
Manually code a pandas Series of integers.

# ANSWER

```
>>> data = pd.Series([1, 2, 3])
>>> data
0    1
1    2
2    3
dtype: int64
```

# TAGS
week 2, beginner, pandas
-------------------------

# QUESTION
Return the values of a pandas Series. What object type is it?

# ANSWER

```
>>> data = pd.Series([1, 2, 3])
>>> data.values
[1 2 3]
>>> type(data.values)
<class 'numpy.ndarray'>
```

# TAGS
week 2, beginner, pandas
-------------------------

# QUESTION
Which standard python type is the pandas Series somewhat a
specialization of? How so?

# ANSWER

```
A dictionary. A dictionary is a structure that maps arbitrary
keys to a set of arbitrary values, and a Series is a structure
which maps typed keys to a set of typed values. The type
information of a Pandas Series makes it much more efficient
than Python dictionaries for certain operations.
```

# TAGS
week 2, beginner, pandas
-------------------------
# QUESTION
How can a pandas DataFrame be constructed?

# ANSWER

```
* a single Series object
* a list of dicts
* a dictionary of Series objects
* a two-dimensional NumPy array
* a NumPy structured array
```

# TAGS
week 2, beginner, pandas
-------------------------

# QUESTION
How is a pandas Index object similar to a python set? How is it
different?

# ANSWER

```
They are both immutable. However, an Index can contain duplicates.
They both support union, intersection, etc. operations.
```

# TAGS
week 2, beginner, pandas
-------------------------

# QUESTION
What is the benefit of using object methods instead of operators
when applying ufuncs to Series/DataFrames?
e.g. A + B versus A.add(B)

# ANSWER

```
The object method takes fill_value and axis arguments.
```

# TAGS
week 2, beginner, pandas
-------------------------
