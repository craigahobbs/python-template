# python-package-template

**python-package-template** is a Python package template for use with
[template-specialize](https://pypi.org/project/template-specialize/).

The generated Python package has the following functionality:

- uses [Python Build](https://github.com/craigahobbs/python-build#readme) for build and development experience

- setup.py ready to upload to [PyPI](https://pypi.org/)

- command-line script (optional, same as the [package main](https://docs.python.org/3/library/__main__.html))

- package documentation generated with [Sphinx](https://pypi.org/project/Sphinx/) (optional)

- 100% unit-test coverage ("make cover" fails if actual coverage is less than 100%)


## Usage

To generate a new Python package project, render it using template-specialize:

```
template-specialize python-package-template/template/ my-package/ \
    -k package "my-package" \
    -k name "John Doe" \
    -k email "johndoe@gmail.com" \
    -k github "johndoe"
```


## Template Variables

The following template variables are defined:

- **package** - the Python package name (e.g. "my-package")

- **name** - the package author's full name (e.g. "John Doe")

- **email** - the package author's email address

- **github** - the package author's GitHub account name (e.g. "johndoe")

- **nodoc** (optional) - if true, package documentation is omitted from the generated project

- **nomain** (optional) - if true, package main is omitted from the generated project
