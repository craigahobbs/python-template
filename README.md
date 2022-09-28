# python-template

**python-template** is a Python project template for use with
[template-specialize](https://github.com/craigahobbs/template-specialize#readme).
Generated projects have the following functionality:

- creates a new Python package project

  - optional command-line script and package main

- build/development experience using [python-build](https://github.com/craigahobbs/python-build#readme)

- runs unit tests with [unittest](https://docs.python.org/3/library/unittest.html)

  - optionally run unit tests with [unittest-parallel](https://github.com/craigahobbs/unittest-parallel#readme)

- code coverage using [coverage](https://github.com/nedbat/coveragepy#readme)

  - 100% code coverage enforced (configurable)

- optionally generates package documentation with [Sphinx](https://www.sphinx-doc.org/en/master/)

- package ready to upload to [PyPI](https://pypi.org/)

- contains a license file ([MIT License](https://choosealicense.com/licenses/mit/))


## Create a New Python Project

To create a new Python project, clone this repository and render the template using
[template-specialize](https://github.com/craigahobbs/template-specialize#readme). For example:

~~~
template-specialize python-template/template/ my-package/ \
    -k package "my-package" \
    -k name "John Doe" \
    -k email "johndoe@gmail.com" \
    -k github "johndoe"
~~~

The template defines the following template variables:

- **package** - the Python package name (e.g., "my-package")

- **name** - the package author's full name (e.g., "John Doe")

- **email** - the package author's email address

- **github** - the package author's GitHub account name (e.g., "johndoe")

- **noapi** (optional) - if true, the package API and documentation are omitted

- **nomain** (optional) - if true, the command-line script and package main are omitted


## Development Basics

Generated projects have a complete build/development experience using
[python-build](https://github.com/craigahobbs/python-build#readme).
It provides commands for running unit tests on all supported Python versions (with and without code coverage),
running static code analysis, building API documentation, publishing API documentation to GitHub Pages,
creating and updating a changelog file, and publishing the package to PyPI.

Here are a few basic commands to help you get started. For more detailed documentation, see the
[python-build documentation](https://github.com/craigahobbs/python-build#contents).

Before any commit, run the **make commit** command to run all tests:

~~~
make commit
~~~

To run unit tests on all supported Python versions, use the **make test** command:

~~~
make test
~~~

To run unit tests on a specific Python version, specify the version-specific test command:

~~~
make test-python-3-X
~~~

To run unit tests on a specific unit test, use the **TEST** argument:

~~~
make test TEST=module.Class.test_method
~~~

To run unit tests with code coverage, use the **make cover** command:

~~~
make cover
~~~

To publish API documentation to [GitHub Pages](https://pages.github.com/), use the **make gh-pages** command:

~~~
make gh-pages
~~~

To create or update a changelog file, use the **make changelog** command:

~~~
make changelog
~~~

Finally, to publish to [PyPI](https://pypi.org/), use the **make publish** command:

~~~
make publish
~~~


## Project Structure

The default project structure is as follows:

~~~
|-- .gitignore
|-- LICENSE
|-- Makefile
|-- README.rst
|-- doc
|   |-- conf.py
|   |-- index.rst
|   `-- reference.rst
|-- setup.py
`-- src
    |-- __init__.py
    |-- my_package
    |   |-- __init__.py
    |   |-- __main__.py
    |   |-- main.py
    |   `-- my_package.py
    `-- tests
        |-- __init__.py
        |-- test_main.py
        `-- test_my_package.py
~~~

If you set the **noapi** template argument, the package API source files and the Sphinx documentation project
directory are removed. Notice also that the project now contains a "README.md" file instead of a "README.rst" file.

~~~
|-- .gitignore
|-- LICENSE
|-- Makefile
|-- README.md
|-- setup.py
`-- src
    |-- __init__.py
    |-- my_package
    |   |-- __init__.py
    |   |-- __main__.py
    |   `-- main.py
    `-- tests
        |-- __init__.py
        `-- test_main.py
~~~

If you further set the **nomain** template argument, the command-line script and package main source files are removed:

~~~
|-- .gitignore
|-- LICENSE
|-- Makefile
|-- README.md
|-- setup.py
`-- src
    |-- __init__.py
    |-- my_package
    |   `-- __init__.py
    `-- tests
        |-- __init__.py
        `-- test.py
~~~
