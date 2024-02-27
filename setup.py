from setuptools import setup

setup(name='python-api-test',
  version='0.1',
  description='Various API calls',
  url='http://github.com/camsimba/python-api-test',
  author='camsimba',
  author_email='nah',
  license='nah',
  packages=['python-api-test'],
  install_requires=[
      'markdown',
      'tabulate',
      'PIL',
      'html2image'
  ],
  zip_safe=False)