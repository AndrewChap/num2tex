# from https://stackoverflow.com/questions/13490292/format-number-using-latex-notation-in-python/13490601#13490601
def num2tex(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str
