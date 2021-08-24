# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE
{%- if noapi is not defined or not noapi %}

"""
{{package}} package
"""

from .{{ package | replace('-', '_') }} import sum_numbers
{%- endif %}
