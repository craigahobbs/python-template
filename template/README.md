# {{package}}

[![PyPI - Status](https://img.shields.io/pypi/status/{{package}})](https://pypi.org/project/{{package}}/)
[![PyPI](https://img.shields.io/pypi/v/{{package}})](https://pypi.org/project/{{package}}/)
[![GitHub](https://img.shields.io/github/license/{{github}}/{{package}})](https://github.com/{{github}}/{{package}}/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{package}})](https://pypi.org/project/{{package}}/)

Coming soon!


## Development

This project is developed using [Python Build](https://github.com/craigahobbs/python-build#readme). It was started
using [python-package-template](https://github.com/craigahobbs/python-package-template#readme) as follows:

```
template-specialize python-package-template/template/ {{package}}/ \
    -k package {{package}} \
    -k name "{{name}}" \
    -k email "{{email}}" \
    -k github "{{github}}" \{% if nodoc is defined and nodoc %}
    -k nodoc 1{% endif %}{% if nomain is defined and nomain %}
    -k nomain 1{% endif %}
```
