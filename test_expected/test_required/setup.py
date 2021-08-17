# Licensed under the MIT License
# https://github.com/johndoe/package-name/blob/main/LICENSE

# pylint: disable=missing-function-docstring, missing-module-docstring

import os

from setuptools import setup


def main():
    # Read the readme for use as the long description
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst'), encoding='utf-8') as readme_file:
        long_description = readme_file.read()

    # Do the setup
    setup(
        name='package-name',
        description='package-name',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        version='0.9.0',
        author='John Doe',
        author_email='johndoe@gmail.com',
        keywords='package-name',
        url='https://github.com/johndoe/package-name',
        license='MIT',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Utilities'
        ],
        package_dir={'': 'src'},
        packages=['package_name'],
        entry_points={
            'console_scripts': [
                'package-name = package_name.main:main'
            ]
        }
    )


if __name__ == '__main__':
    main()