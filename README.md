# python-template

**python-template** is a Python package template for use with
[template-specialize](https://pypi.org/project/template-specialize/).

All generated packages have the following functionality:

- uses [Python Build](https://github.com/craigahobbs/python-build#readme) for build/development experience

- contain setup.py ready to upload to [PyPI](https://pypi.org/)

- setup installs command-line script and [package main](https://docs.python.org/3/library/__main__.html) (optional)

- generates package documentation with [Sphinx](https://pypi.org/project/Sphinx/) (optional)

- publishes package documentation to [GitHub Pages](https://pages.github.com/) (optional)

- 100% unit-test code coverage ("make cover" fails if coverage is less than configurable minimum)


## Create a New Python Package

To generate a new Python package, clone this repository and render the template directory using template-specialize:

```
template-specialize python-template/template/ my-package/ \
    -k package "my-package" \
    -k name "John Doe" \
    -k email "johndoe@gmail.com" \
    -k github "johndoe"
```

The template exposes the following template variables:

- **package** - the Python package name (e.g. "my-package")

- **name** - the package author's full name (e.g. "John Doe")

- **email** - the package author's email address

- **github** - the package author's GitHub account name (e.g. "johndoe")

- **noapi** (optional) - if true, the package API and documentation are omitted

- **nomain** (optional) - if true, the command-line script and package main are omitted
