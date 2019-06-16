import unittest

from num2tex import num2tex

testInputs = []

class inputAndOutput:
    testInputs = []

    def __init__(
            self,
            value,
            output_str = None,
            output_str_dict = None,
            ):
        self.value = value
        if output_str_dict is not None:
            self.output_is_dict = True
            self.output_str_dict = output_str_dict
        else:
            self.output_is_dict = False
            if output_str is None:
                self.str = str(value)
            else:
                self.str = output_str
        #self.repr = 'num2tex(num={})'.format(str(value))
        #self.repr_latex = '${}$'.format(self.str)
        inputAndOutput.testInputs.append(self)
    def set_exp_format(self,exp_format):
        self.str = self.output_str_dict[exp_format]

    def __str__(self):
        return self.str
    def __repr__(self):
        return 'num2tex(num={})'.format(str(self.value))
    def _repr_latex_(self):
        return '${}$'.format(self.str)
    def __format__(self):
        return self.format

float_tester = inputAndOutput(
        value = 13.6e14)

exp_tester = inputAndOutput(
        value = 13.6e15,
        output_str_dict = {
            'times'       : '1.36 \\times 10^{16}',
            'cdot'        : '1.36 \\cdot 10^{16}',
            'parentheses' : '1.36 (10^{16})',
            '\,e{}'       : '1.36 \,e{16}',
        })

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
                if testInput.output_is_dict:
                    testedStrings = []
                    acceptStrings = []
                    for key,val in testInput.output_str_dict.items():
                        testedStrings.append(getattr(num2tex(testInput.value,exp_format=key),outputType)())
                        testInput.set_exp_format(key)
                        acceptStrings.append(getattr(testInput,outputType)())
                else:
                    acceptStrings = [getattr(testInput,outputType)()]
                    testedStrings = [getattr(num2tex(testInput.value),outputType)()]
                for acceptString,testedString in zip(acceptStrings,testedStrings):
                    with self.subTest(
                        msg="Test if {} returns '{}'".format(testedString,acceptString)):
                        self.assertEqual(acceptString,testedString)

    def test_format(self):
        pairs = [
                    [
                        "'a = {}'.format(num2tex(4.6325,precision=2))",
                        'a = {}'.format(num2tex(4.6325,precision=2)),
                        'a = 4.6',
                    ],
                    [
                        "'{0:.2e} + {1:.2e}'.format(num2tex(0.00000012423),num2tex(0.00000000000009))",
                        '{0:.2e} + {1:.2e}'.format(num2tex(0.00000012423),num2tex(0.00000000000009)),
                        '1.24 \\times 10^{-7} + 9.00 \\times 10^{-14}',
                    ]
                ]
        for pair in pairs:
            with self.subTest(
                    msg="check if [{}] is equal to [{}]".format(pair[0],pair[2])):
                self.assertEqual(pair[1],pair[2])

if __name__ == '__main__':
    unittest.main()
