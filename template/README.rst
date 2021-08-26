{{package}}
{{ '=' * (package | length) }}

.. |badge-status| image:: https://img.shields.io/pypi/status/{{package}}
   :alt: PyPI - Status
   :target: https://pypi.python.org/pypi/{{package}}/

.. |badge-version| image:: https://img.shields.io/pypi/v/{{package}}
   :alt: PyPI
   :target: https://pypi.python.org/pypi/{{package}}/

.. |badge-license| image:: https://img.shields.io/github/license/{{github}}/{{package}}
   :alt: GitHub
   :target: https://github.com/{{github}}/{{package}}/blob/main/LICENSE

.. |badge-python| image:: https://img.shields.io/pypi/pyversions/{{package}}
   :alt: PyPI - Python Version
   :target: https://www.python.org/downloads/

|badge-status| |badge-version| |badge-license| |badge-python|

Coming soon!


Links
-----

- `Documentation on GitHub Pages <https://{{github}}.github.io/{{package}}/>`__
- `Package on pypi <https://pypi.org/project/{{package}}/>`__
- `Source code on GitHub <https://github.com/{{github}}/{{package}}>`__


Development
-----------

This project is developed using `python-build <https://github.com/craigahobbs/python-build#readme>`__. It was started
using `python-template <https://github.com/craigahobbs/python-template#readme>`__ as follows::

    template-specialize python-template/template/ {{package}}/ -k package {{package}} -k name '{{name}}' -k email '{{email}}' -k github '{{github}}'{% if noapi is defined and noapi %} -k noapi 1{% endif %}{% if nomain is defined and nomain %} -k nomain 1{% endif %}
