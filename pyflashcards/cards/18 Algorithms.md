## q

What is **runtime complexity**, or **Big O**?

## a
It describes the *numerber of operations* required of an algorithm in relation to the *number of elements* being processed, when considering the worst case scenario or average case scenario.

For example, an `O(n ^ 2)` algorithm carries out n_elements ^ 2 operations to complete the task.

---
## q

What are common types of **runtime complexity**, or **Big O**, in order of performance?

## a

1. `O(c)` constant time
1. `O(log(n))` logarithmic time
1. `O(n)` linear time
1. `O(nlog(n))` log-linear time
1. `O(n^c)` quadratic time
1. `O(c^n)` exponential time
1. `O(n!)` factorial time

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/1024px-Comparison_computational_complexity.svg.png" width="100%">

---
## q
How does a **constant time** solution perform in terms of runtime complexity?

## a
This is the best performance possible. The number of operations is constant regardless of the number of elements or inputs.

---
## q
Explain a **binary search**. What is its **runtime complexity**?

*Note: search algorithms return the index location of a target value in a sorted list of numbers*

## a
This algorithm runs in **logarithmic time**, `O(log(n))`, since our operations are cut in half with each step.

```python
def binary_search(sorted_array, target, idx_min=0, idx_max=None):
    if not sorted_array[0] <= target <= sorted_array[-1]:
        return False
    if idx_max is None:
        idx_max = len(sorted_array) - 1

    idx_mid = (idx_min + idx_max) // 2

    if sorted_array[idx_mid] == target:
        return idx_mid
    elif target < sorted_array[idx_mid]:
        idx_max = idx_mid - 1 
    elif sorted_array[idx_mid] < target:
        idx_min = idx_mid + 1

    return binary_search(sorted_array, target, idx_min, idx_max)
```

---
## q
What are examples of algorithms with log-linear runtime complexity, `O(n * log(n))`? What is significant about this runtime complexity?

## a
`O(n * log(n))` is the best (average) performance a comparison-based sorting method can achieve.

Some examples:

* Quicksort
* Mergesort
* Heapsort
* Timsort

---
## q
What are some examples of scenarios with exponential runtime complexity, `O(c ^ n)`?

## a
* cracking as unknown password
* the knapsack problem
* the minesweeper consistency problem
* prime factorization of large integers
* the longest common subsequence of strings

---

## q
How would the more common form of runtime complexity of `O(n ^ 2 + 4n + 90)` be written?

## a
`O(n ^ 2)`. Algorithmic runtime complexity is commonly defined by the **dominating term**.

---

## q
Explain a **bubble sort** algorithm. What is its runtime complexity? When is it useful?

## a
Quadtratic, `O(n ^ c)`, since it will require more loops with more inputs. Bubble sort can be useful when we can assume our information is *mostly* sorted.

```python
def bubble_sort(arr):
    swap_made = True
    while swap_made:
        swap_made = False
        for i in range(len(arr) - 1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]  # swap
                swap_made = True

    return arr
```

---

## Q
What are examples of algorithms with quadtratic, `O(n ^ c)`, time complexity?

## A

* bubble sort
* listing all permutations of the characters in a string
* nested loops are a good "code sniff" for quadratic runtime performance

```python
def print_all_pairs(array):
    for first_item in array:
        for second_item in array:
            print(first_item, second_item)
```

---

## q
What is are **stack frame** and **call stack**?

## a
The **call stack** is the collection of **stack frames**. A **stack frame** is the representation of state at each iteration of a recursive algorithm. It contains the local variables in that instance of the recursion.

## q
What are **Polya's Problem solving steps**?
