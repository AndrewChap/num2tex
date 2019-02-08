# Default options
option_exp_format = '\\times 10^{}'
option_display_singleton = False

# Function to set options
def configure(exp_format=None, display_singleton=None):
    global option_exp_format
    if exp_format is not None:
        option_exp_format = exp_format
    if display_singleton is not None:
        option_display_singleton = display_singleton

class num2tex(str):
    def __new__(self, num, precision=None, format_spec=None):
        self.num = num
        self.precision = precision
        self.format_spec = format_spec
        return str.__new__(self,num)

    # __format__() gets called, for example,
    # when evaluating 'a={0.2g}'.format(num2tex(2.5456))
    def __format__(self,format_spec):
        return self.__str__(format_spec)

    # method that converts the number into a string
    # with precision given by f (of type string)
    # or by self.precision (of type int)
    def __str__(self,format_spec=None):
        if format_spec is None:
            format_spec = self.format_spec
        if self.num is None:
            return '\\mathrm{None}'
        elif self.num == float('inf'):
            return '\\infty'
        elif self.num == -float('inf'):
            return '-\\infty'
        elif self.num != self.num:
            return '\\mathrm{NaN}'
        formatUnspecified = (format_spec is None) or (format_spec == '')
        if formatUnspecified and self.precision is None:
            num_string = str(self.num)
        else:
            if formatUnspecified:
                format_spec = '0.{}'.format(self.precision)
            num_string = '{0:{1}}'.format(self.num,format_spec)
        if 'e' in num_string:
            base, exponent = num_string.split('e')
            exp = (option_exp_format.format('{{{}}}')).format(int(exponent))
            if base == '1' and option_display_singleton is False:
                return r'{0}'.format(exp)
            else:
                return r'{0} {1}'.format(base,exp)
        else:
            return num_string

    # unambiguous string representation of num2tex object
    def __repr__(self):
        if self.precision is None:
            return 'num2tex(num={})'.format(self.num)
        else:
            return 'num2tex(num={}, precision={})'.format(self.num,self.precision)

    # for pretty printing in a Jupyter Notebook
    def _repr_latex_(self):
        return '$' + self.__str__() + '$'
