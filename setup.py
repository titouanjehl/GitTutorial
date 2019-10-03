from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()



setup(name='mypackage',
      description='test_package',
      keywords='',
      url='http://github.com/titouanjehl/GitTutorial',
      author='Me',
      author_email='Me@berkeley.edu',
      long_description=readme(),
      packages=find_packages('src'),
      package_dir={'': 'src'},
      setup_requires=['pytest-runner', ],
      tests_require=['pytest', 'mock'],
      zip_safe=False
      )
