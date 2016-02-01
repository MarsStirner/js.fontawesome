import os

from setuptools import find_packages
from setuptools import setup

version = '4.5.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = read('README.rst')

setup(
    name='js.fontawesome',
    version=version,
    description="Fanstatic packaging of FontAwesome",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Mikhael Malkov',
    author_email='viruzzz.soft@gmail.com',
    url='https://github.com/hitsl/js.fontawesome',
    license='SIL OFL 1.1, MIT',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.bootstrap',
        'js.angular',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'fontawesome = js.fontawesome:library',
            ],
        },
    )
