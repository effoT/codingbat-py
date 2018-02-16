# this will work if set directly to the console
$var = @'
starOut("ab*cd") → "ad"	"ad"	OK	
starOut("ab**cd") → "ad"	"ad"	OK	
starOut("sm*eilly") → "silly"	"ad"	X	
starOut("sm*eil*ly") → "siy"	"ad"	X	
starOut("sm**eil*ly") → "siy"	"ad"	X	
starOut("sm***eil*ly") → "siy"	"ad"	X	
starOut("stringy*") → "string"	"ad"	X	
starOut("*stringy") → "tringy"	"ad"	X	
starOut("*str*in*gy") → "ty"	"ad"	X	
starOut("abc") → "abc"	"ad"	X	
starOut("a*bc") → "c"	"ad"	X	
starOut("ab") → "ab"	"ad"	X	
starOut("a*b") → ""	"ad"	X	
starOut("a") → "a"	"ad"	X	
starOut("a*") → ""	"ad"	X	
starOut("*a") → ""	"ad"	X	
starOut("*") → ""	"ad"	X	
starOut("") → ""
'@


foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1].split('"')[1]
    "if $($query) != `"$($result)`" :print('$($query) not `"$($result)`"')" | Write-output
}