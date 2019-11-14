# num2tex
`num2tex` converts a `float` or `int` into a TeX-formatted string.  `num2tex` inherits from `str`.  

1. [Installation](#installation)
2. [Usage](#usage)
3. [num2tex in Jupyter](#num2tex-in-jupyter)
4. [Future Work](#future-work)
5. [Thanks](#thanks)

## Installation
Install with
```bash
pip install num2tex
```
## Usage
`num2tex` can be used in a similar manner to that of `str`

```python
from num2tex import num2tex
print(num2tex(13.6e15))
```
```
1.36 \times 10^{16}
```
which gives the same precision and float/scientific notation formatting as `print(str(13.6e15))` or `print(13.6e15)` but in TeX format.  For some numbers, the default `str` formatting may be unintuitive and give too many significant figures:
```python
print(num2tex(9.876e15))
```
```
9876000000000000.0
```
so instead we can use [`format`](https://pyformat.info/) as we would for a string, in this example specifying 3 significant figures:
```python
print('a = {:.3g}'.format(num2tex(9.876e15)))
```
```
a = 9.88 \times 10^{15}
```

Or we can set the precision from the beginning so that it always displays the desired number of significant figures.
```python
a = num2tex(1.26e10,precision=2)
print('$a = {}$'.format(a))
```
```
$1.3 \\times 10^{10}$
```
but keep in mind that `precision` can still be overridden by a format specifier:
```python
print('$a = {:f}$'.format(num2tex(13.6e10,precision=2)))
```
```
$a = 136000000000.000000$
```

## num2tex in Jupyter
`num2tex` will produce Jupyter-friendly output by default, and can be used in LaTeX-friendly modules like Matplotlib:

<img src="https://raw.githubusercontent.com/AndrewChap/num2tex/master/images/jp_samp_1.png" alt="Sample Jupyter output" width="390"/>

## Using \cdot or parentheses to display the exponent

Use the `num2tex.configure()` option to change how the exponent is displayed:
```python
>>>from num2tex import num2tex
>>>from num2tex import configure as num2tex_configure
>>>num2tex_configure(exp_format='cdot')
>>>num2tex(1.3489e17)
'1.3489 \cdot 10^{17}'
>>>num2tex_configure(exp_format='parentheses')
'1.3489 (10^{17})'
```

## Future Work
 1. Add `format` option e.g. `a = num2tex(num=1.36e10,format='.2g')`
 2. TeX-rendering support for Google Collaboratory
 3. Additional testing
 4. Get user feedback
 5. Look into better Jupyter display of something like `print('$a = {}$'.format(a))` without needing to import `Display` and `Math`, possibly by allowing `num2tex` to accept a string input, and using a different `_repr_latex_()` function if the input is a string.
 
 ## Thanks
num2tex is inspired by a [relevant stack overflow question and Lauritz V. Thaulow's answer](https://stackoverflow.com/questions/13490292/format-number-using-latex-notation-in-python/13490601#13490601) as well as a [num2TeX function for GNU Octave by Karl Wette](https://github.com/octapps/octapps/blob/84d8b2c0b6e1efa1c66c0c9b380e13cf4c6c95e0/src/text-handling/num2TeX.m)
