import pdb
# Default options
option_configure_help_text = True
option_exp_format = '\\times 10^{}'
option_display_singleton = False

# Function to set options
def configure(**kwargs): #exp_format=None, display_singleton=None):
    global option_configure_help_text, option_exp_format, option_display_singleton

    if 'help_text' in kwargs:
        option_configure_help_text = kwargs['help_text']
    if option_configure_help_text:
        print('''num2tex configure options:
 - help_text: boolean whether this help text is displayed when configure() is called
 - exp_format: string format specification for how the power of 10 is displayed in scientific format.
     - also accepts specifiers 'times', which is converted to '\\times 10^{}', 'cdot': '\\cdot 10^{}', and 'parentheses': '(10^{})'
 - display_singleton: boolean on whether the "1 \\times" is printed in "1 \\times 10^{p}"
          '''
        )

    if 'exp_format' in kwargs:
        option_exp_format = kwargs['exp_format']
    if 'display_singleton' in kwargs:
        option_display_singleton = kwargs['display_singleton']

class num2tex(str):
    def __new__(self, num, precision=None, format_spec=None, exp_format=None, display_singleton=None):
        self.num = num
        self.precision = precision
        self.format_spec = format_spec
        self.exp_format = option_exp_format if exp_format is None else exp_format
        if self.exp_format == 'times':
            self.exp_format = '\\times 10^{}'
        elif self.exp_format == 'cdot':
            self.exp_format = '\\cdot 10^{}'
        elif self.exp_format == 'parentheses':
            self.exp_format = '(10^{})'
        self.display_singleton = option_display_singleton if display_singleton is None else display_singleton
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
            num_string = self
        else:
            if formatUnspecified:
                format_spec = str.format('0.{}',self.precision)
            format_spec_braced = '{:'+format_spec+'}'
            num_string = str.format(format_spec_braced,float(self))
        if 'e' in num_string:
            base, exponent = num_string.split('e')
            exp = str.format((str.format(self.exp_format,'{{{}}}')),int(exponent))
            if base == '1' and self.display_singleton is False:
                return str.format(r'{0}',exp)
            else:
                return str.format(r'{0} {1}',base,exp)
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
