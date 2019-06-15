from setuptools import setup

setup(name='num2tex',
      version='0.8',
      description='Convert float or int to a TeX-formatted string',
      url='http://github.com/AndrewChap/num2tex',
      author='Andrew Chap',
      author_email='andrew@andrewchap.com',
      license='MIT',
      packages=['num2tex'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
