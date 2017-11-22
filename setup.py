from setuptools import setup, find_packages

import os


version = '0.2.5rc1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
        read('README.rst')
        + '\n' +
        read('CHANGES.txt'))

setup(name='zptlint',
      version=version,
      description="Utility to debug Zope Page Templates",
      long_description=long_description,
      classifiers=[
        "Framework :: Zope2",
        "Framework :: Zope3",
      ],
      keywords='zope',
      author='Balazs Ree',
      author_email='ree@ree.hu',
      url='https://trac.bubblenet.be/browser/bubblenet/pythoncode/'
          'zptlint/trunk/README.txt?format=txt',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'zope.pagetemplate',
          'zope.contentprovider',
          # mentioned here because not mentioned in zope.pagetemplate <= 3.5.0
          'zope.traversing',
      ],
      entry_points={
        'console_scripts': [
            'zptlint = zptlint:run',
            ],
        },
      )
