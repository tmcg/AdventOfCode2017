# pip install nose2
# $env:PythonPath = 'src'
$tr_cmd = 'nose2'
$tr_parm = @('--fail-fast')

if ($args[0] -ne $null) {
  $tr_parm += @('--plugin','nose2.plugins.attrib','-A',$args[0])
}

&$tr_cmd $tr_parm;