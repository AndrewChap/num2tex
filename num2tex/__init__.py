class num2tex(str):
    def __new__(self, num, precision=None):
        self.num = num
        self.precision = precision
        return str.__new__(self,num)

    # __format__() gets called, for example,
    # when evaluating 'a={0.2g}'.format(num2tex(2.5456))
    def __format__(self,f):
        return self.__str__(f)

    # method that converts the number into a string
    # with precision given by f (of type string)
    # or by self.precision (of type int)
    def __str__(self,f=None):
        if self.num is None:
            return '\mathrm{None}'
        elif self.num == float('inf'):
            return '\infty'
        elif self.num == -float('inf'):
            return '-\infty'
        elif self.num != self.num:
            return '\mathrm{NaN}'
        if f is None and self.precision is None:
            num_string = str(self.num)
        else:
            if f is None:
                f = '0.{}'.format(self.precision)
            num_string = '{0:{1}}'.format(self.num,f)
        if 'e' in num_string:
            base, exponent = num_string.split('e')
            return r'{0} \times 10^{{{1}}}'.format(base, int(exponent))
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
        return '$$' + self.__str__() + '$$'
