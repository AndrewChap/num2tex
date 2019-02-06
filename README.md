# num2tex
Converts a float or int into a TeX-formatted string.  `num2tex` inherits from `str`.  

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
print(num2tex(13.4e10))
```
```
134000000000.0
```
which gives the same precision and float/scientific notation formatting as `print(str(1.34e10))` or `print(str(1.34e10))`.  We can customize the format as we would for a string:
```python
# Print in string with two significant figures
print('$a = {:0.2g}$'.format(num2tex(13.6e10)))
```
```
'1.4 \\times 10^{11}'
```
Or we can set the precision from the beginning so that it always displays the desired number of significant figures.
```python
a = num2tex(1.4e10,precision=2)
print('$a = {}$'.format(a))
```
returns
```
'1.3 \\times 10^{10}'
```
but `precision` can still be overridden by a format specifier:
```python
print('$a = {:f}$'.format(num2tex(13.6e10,precision=2)))
```
```
$a = 136000000000.000000$
```
## num2tex in Jupyter
`num2tex` will produce Jupyter-friendly output by default, and can be used in LaTeX-friendly modules like Matplotlib:

<img src="https://raw.githubusercontent.com/AndrewChap/num2tex/master/images/jp_samp_1.png" alt="Sample Jupyter output" width="390"/>

## Future Work
 1. Add global option to use `\cdot 10^{p}` or `(10^p)` instead of `\times 10^{p}` in exponential-format
 2. Support for Google Collaboratory
 3. Additional testing in num2tex/tests
 4. Get user feedback
 
 ## Thanks
num2tex is inspired by a [relevant stack overflow question and Lauritz V. Thaulow's answer](https://stackoverflow.com/questions/13490292/format-number-using-latex-notation-in-python/13490601#13490601) as well as a [num2TeX function for GNU Octave by Karl Wette](https://github.com/octapps/octapps/blob/84d8b2c0b6e1efa1c66c0c9b380e13cf4c6c95e0/src/text-handling/num2TeX.m)
