
get-childitem .\*.pyc -recurse | foreach-object { remove-item $_.FullName }
