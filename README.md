# num2tex
Converts a float or int into a latex-formatted string.  `num2tex` inherits from `str`.  

1. [Installation](#installation)
2. [Usage](#usage)
3. [num2tex in Jupyter](#num2tex-in-jupyter)

## Installation
Install with
```bash
pip install num2tex
```
## Usage
`num2tex` inherits from `str`, and so can be used in a similar manner.

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
`num2tex` will produce Jupyter-friendly output:
```python
from num2tex import num2tex
a = num2tex(13.4e10,precision=2)
a
```
![Jupyter output](https://raw.githubusercontent.com/AndrewChap/num2tex/master/images/jp_samp_0.png)

## Thanks
num2tex is inspired by https://stackoverflow.com/questions/13490292/format-number-using-latex-notation-in-python/13490601#13490601 and https://github.com/RoaldFre/octaveScripts/blob/master/num2tex.m

## Future
 1. Add format option i.e. `num2tex(13.6e10,format=':.2g')`
 2. Add support for Google Collaboratory
 3. Add testing
 4. Get user feedback
