# set FLASK_APP=mathjax_test\app.py && flask run
from flask import Flask
import markdown

from mathjax import MathJaxExtension


app = Flask(__name__)
text = r"""
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Hello, World!

$$e^{i\pi} = -1$$

$$
x = \begin{vmatrix} i & j & k \\ x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \end{vmatrix} = i\begin{vmatrix} x_2 & x_3 \\ y_2 & y_3 \end{vmatrix} + j\begin{vmatrix}x_1 & x_3 \\y_1 & y_3\end{vmatrix} + k\begin{vmatrix}x_1 & x_2 \\y_1 & y_2\end{vmatrix} = \\ \\ i(x_2y_3-x_3y_2) - j(x_1y_3-x_3y_1) + k(x_1y_2-x_2y_1)
$$

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$
"""

@app.route('/')
def hello():
    return markdown.markdown(
        text,
        extensions=['fenced_code', 'codehilite', MathJaxExtension()]
    )
