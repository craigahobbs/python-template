# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE

import os

from setuptools import setup


def main():
    # Read the readme for use as the long description
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README{{".md" if nodoc is defined and nodoc else ".rst"}}'), encoding='utf-8') as readme_file:
        long_description = readme_file.read()

    # Do the setup
    setup(
        name='{{package}}',
        description='{{package}}',
        long_description=long_description,
        long_description_content_type='text/markdown',
        version='0.9.0',
        author='{{name}}',
        author_email='{{email}}',
        keywords='{{package}}',
        url='https://github.com/{{github}}/{{package}}',
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
        packages=['{{package | replace("-", "_")}}']{% if nomain is not defined or not nomain %},
        entry_points={
            'console_scripts': [
                '{{package}} = {{package | replace("-", "_")}}.main:main'
            ]
        }{% endif %}
    )


if __name__ == '__main__':
    main()
