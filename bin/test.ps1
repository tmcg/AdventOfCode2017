# pip install nose2
# $env:PythonPath = 'src'
nose2 --fail-fast --plugin nose2.plugins.attrib -A '!slow'
