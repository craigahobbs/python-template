# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE
{%- if nodoc is not defined or not nodoc %}

"""
{{package}} package
"""

from .{{ package | replace('-', '_') }} import sum_numbers
{%- endif %}
