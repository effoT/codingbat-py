# this will work if set directly to the console
$var = @'
sumNumbers("abc123xyz") → 123	3	X	
sumNumbers("aa11b33") → 44	3	X	
sumNumbers("7 11") → 18	3	X	
sumNumbers("Chocolate") → 0 3	X	
sumNumbers("5hoco1a1e") → 7	3	X	
sumNumbers("5$$1;;1!!") → 7	3	X	
sumNumbers("a1234bb11") → 1245	3	X	
sumNumbers("") → 0	3	X	
sumNumbers("a22bbb3") → 25	3
'@

# if the result is expected to be a string
foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1].split('"')[1]
    "if $($query) != `"$($result)`" :print('$($query) not `"$($result)`"')" | Write-output
}

#if the result is expected to be a num (currently supports only one digit)
foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1].substring(1,1)
    "if $($query) != $($result) :print('$($query) not $($result)')" | Write-output
}

#if the result is expected to be boolean
foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1].split('"')[1]
    if ($line.Split([char]8594)[1].trim() -like "false*")
    {
        $result = "False"
    }
    elseif($line.Split([char]8594)[1].trim() -like "true*") 
    {
        $result = "True"
    }
    "if $($query) != $($result) :print('$($query) not $($result)')" | Write-output
    
}