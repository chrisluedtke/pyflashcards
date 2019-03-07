# pyflashcards

A simple way to log and study python tidbits

```
$pip install git+https://github.com/chrisluedtke/pyflashcards.git
$python
>>> import pyflashcards
Enter the tag(s) to study: pandas
Found 6 flashcards. Enter any key to begin.

__PROMPT_______________________________________________________________________

Return the values of a pandas Series. What object type is it?


Know it? y/n/quit: y

__ANSWER_______________________________________________________________________

>>> data = pd.Series([1, 2, 3])
>>> data.values
[1 2 3]
>>> type(data.values)
<class 'numpy.ndarray'>

```
