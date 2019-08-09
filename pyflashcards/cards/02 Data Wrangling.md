# q

What are some methods of **handling missing values** in tabular data? Why is this important?

# a

Missing data often contain useful information, so we should be careful in how we handle them. For example, missing data may be predictive of our target or lend us clues about other features or how the data were gathered. However, many machine learning models cannot process missing data.

Some options:
* Remove the entire column, in the case where the missing data are not useful or are entirely explained by a different column.
* Remove the entire record/row containing a missing value for some column.
* Replace missing values with 0 (or a 'null' category given categorical data). This may harm machine learning models that assume linear relationships.
* Infer or "back in" to the missing value through calculations applied to other features. Commonly we replace missing values with the mean of the non-missing values. This can get more complicated by grouping samples into the categories of another attributes and using the means from those groupings.
