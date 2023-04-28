##Parse important information of all tests into one file

## Path to txt files
$path_to_files = "C:\Users\leopo\OneDrive\TuGraz\WS2022\bacc-arbeit\prakt.Teil\all-inst-test\"

## Path to output file
$path_to_output = "C:\Users\leopo\OneDrive\TuGraz\WS2022\bacc-arbeit\prakt.Teil\output2.txt"


##iterate through every txt file in directory
Get-ChildItem $path_to_files -Filter *.txt|Foreach-Object{
	$file_data = Get-Content $_.FullName
	$m = $file_data[4] -replace "[^0-9]" , ''
	$d = $file_data[5] -replace "[^0-9]" , ''
	$q = $file_data[14] -replace "[^0-9]" , ''

	$SAT = $file_data[17] -replace "[^0-9]" , ''

	if ([int]$SAT)
	{
		$Reduction = $m - $q
	}
	else
	{
		$Reduction = 0
	}

	$Balls = $file_data[8] -replace "[^0-9]" , ''
	$Adjacents = $file_data[9] -replace "[^0-9]" , ''
	$CNF = $file_data[16] -replace "[^0-9]" , ''
	$time_gen = $file_data[10] -replace "[^0-9.]"
	$time_solver = $file_data[19] -replace "[^0-9.]" , ''

	## build row
	$text = "$($m) & $($d) & $($q) & $($SAT) & $($Reduction) & $($Balls) & $($Adjacents) & $($CNF) & $($time_gen) & $($time_solver) \\"

	Add-Content $path_to_output "$($text)"

	Write-Host $text 
}


<#
$file = "2-1-2.txt"

$file_data = Get-Content -Path "$($path_to_files)$($file)"
$m = $file_data[4] -replace "[^0-9]" , ''
$d = $file_data[5] -replace "[^0-9]" , ''
$q = $file_data[14] -replace "[^0-9]" , ''

$SAT = $file_data[17] -replace "[^0-9]" , ''

if ([int]$SAT)
{
	$Reduction = $m - $q
}
else
{
	$Reduction = 0
}

$Balls = $file_data[8] -replace "[^0-9]" , ''
$Adjacents = $file_data[9] -replace "[^0-9]" , ''
$CNF = $file_data[16] -replace "[^0-9]" , ''
$time_gen = $file_data[10] -replace "[^0-9]" , ''
$time_solver = $file_data[19] -replace "[^0-9]" , ''

## build row
$text = "$($m) & $($d) & $($q) & $($SAT) & $($Reduction) & $($Balls) & $($Adjacents) & $($CNF) & $($time_gen) & $($time_solver) \\"

Add-Content $path_to_output "$($text)"

Write-Host $text
#>