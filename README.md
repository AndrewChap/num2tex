# num2tex
Converts a float or int into a latex-formatted string.  Verbatim from https://stackoverflow.com/questions/13490292/format-number-using-latex-notation-in-python/13490601#13490601

## Installation
Install with
```bash
pip install num2tex
```
## Usage
For example,
```python
from num2tex import num2tex
num2tex(1.34e10)
```
returns
```
'1.3 \\times 10^{10}'
```
