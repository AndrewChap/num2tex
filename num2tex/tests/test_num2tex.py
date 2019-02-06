import unittest

from num2tex import num2tex

testInputs = []

class inputAndOutput:
    testInputs = []

    def __init__(
            self,
            value,
            output_str = None,
            ):
        self.value = value
        if output_str is None:
            self.str = str(value)
        else:
            self.str = output_str
        self.repr = 'num2tex(num={})'.format(str(value))
        self.repr_latex = '${}$'.format(self.str)
        inputAndOutput.testInputs.append(self)
    def __str__(self):
        return self.str
    def __repr__(self):
        return self.repr
    def _repr_latex_(self):
        return self.repr_latex
    def __format__(self):
        return self.format

float_tester = inputAndOutput(
        value = 13.6e14)

exp_tester = inputAndOutput(
        value = 13.6e15,
        output_str = '1.36 \\times 10^{16}')

inf_tester = inputAndOutput(
        value = 1.7976931348623159e+308,
        output_str = '\\infty')

neg_inf_tester = inputAndOutput(
        value = -1.7976931348623159e+308,
        output_str = '-\\infty')

nan_tester = inputAndOutput(
        value = 1.7976931348623159e+308-1.7976931348623159e+308,
        output_str = '\\mathrm{NaN}')

class TestNum2tex(unittest.TestCase):
    def test_methods(self):
        for outputType in ['__str__','__repr__','_repr_latex_']:
            print('  Testing method {}.............'.format(outputType))
            for testInput in inputAndOutput.testInputs:
                print('    Testing value {}'.format(testInput.value))
                a = getattr(num2tex(testInput.value),outputType)()
                s = getattr(testInput,outputType)()
                with self.subTest(
                    msg="Test if num2tex(num={}).{} returns '{}'".format(testInput.value,outputType,s)):
                    self.assertEqual(a,s)
    def test_format(self):
        pairs = [
                    [
                        "'a = {}'.format(num2tex(4.6325,precision=2))",
                        'a = {}'.format(num2tex(4.6325,precision=2)),
                        'a = 4.6',
                    ]
                ]
        for pair in pairs:
            with self.subTest(
                    msg="check if [{}] is equal to [{}]".format(pair[0],pair[2])):
                self.assertEqual(pair[1],pair[2])


if __name__ == '__main__':
    unittest.main()
