# this will work if pasted directly to the console
$var = @'
copyEvens([3, 2, 4, 5, 8], 2) → [2, 4]+[1, 2, 3]	X	
copyEvens([3, 2, 4, 5, 8], 3) → [2, 4, 8]+	[1, 2, 3]	X	
copyEvens([6, 1, 2, 4, 5, 8], 3) → [6, 2, 4]+	[1, 2, 3]	X	
copyEvens([6, 1, 2, 4, 5, 8], 4) → [6, 2, 4, 8]+	[1, 2, 3]	X	
copyEvens([3, 1, 4, 1, 5], 1) → [4]+	[1, 2, 3]	X	
copyEvens([2], 1) → [2]+	[1, 2, 3]	X	
copyEvens([6, 2, 4, 8], 2) → [6, 2]+	[1, 2, 3]	X	
copyEvens([6, 2, 4, 8], 3) → [6, 2, 4]+	[1, 2, 3]	X	
copyEvens([6, 2, 4, 8], 4) → [6, 2, 4, 8]+	[1, 2, 3]	X	
copyEvens([1, 8, 4], 1) → [8]+	[1, 2, 3	X	
copyEvens([1, 8, 4], 2) → [8, 4]+	[1, 2, 3]	X	
copyEvens([2, 8, 4], 2) → [2, 8]+	[1, 2, 3]	
'@

# if the result is expected to be a string
foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1]
    "if $($query) != `"$($result)`" :print('$($query) not `"$($result)`"')" | Write-output
}

# if the result is expected to be an array, remember to add to the data + as a delimiter
foreach ($line in $var.split("`n"))
{
    $query = $line.Split([char]8594)[0]
    $result = $line.Split([char]8594)[1].split("+")[0]
    "if $($query) != $($result) :print('$($query) not $($result)')" | Write-output
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