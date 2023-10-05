## script for generating all (meaningful)possible outputs, wich take  less than $waitingParam (in seconds) to complete
## Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted (use when execution is restricted)

## defines, how long we wait for the exe to finish (in seconds)
$waitingParam = 1200 ##20 min

## path to execution file and output files
$execFile = "..\..\BaccArbeit\bin\main-15-03-23\main.exe"
$outputFiles = "C:\Users\leopo\OneDrive\TuGraz\WS2022\bacc-arbeit\prakt.Teil\all-inst-test-no\"

## lower limit m, d
$m_llim = 20
$d_llim = 3

## upper limit m, d
$m_ulim = 21

try
{
	## iterate through every possible (meaningful) input
	for ($m = $m_llim;$m -lt $m_ulim;$m++)
	{	
		for ($d = $d_llim; $d -lt $m; $d++)
		{
			$breakFlag = 0
			for ($q = ($m-16); $q -gt $d; $q--) ##set q upper limit
			{
				##output file name
				$output_file = "$($m)-$($d)-$($q).txt"
				
				## if the output file already exists, we dont need to generate another one
				if (-not (Test-Path -Path "$($outputFiles)$($output_file)"))
				{
					##process
					$processOptions = @{
						FilePath = $execFile
						## change for different exe inputs
						ArgumentList = "$m $d $q cd $($outputFiles)$($output_file) n n n"
					}
					Write-Host "file $m $d $q"
					$app = Start-Process @processOptions -WindowStyle Hidden -PassThru
					
					## waits till the output file arrives or 20min elapse
					$timer = [Diagnostics.Stopwatch]::StartNew()
					while(($timer.Elapsed.TotalSeconds -lt $waitingParam) -and (-not (Test-Path -Path "$($outputFiles)$($output_file)")))
					{
						Start-Sleep -Seconds 1
						$totalSecs = [math]::Round($timer.Elapsed.TotalSeconds, 0)
						
						Write-Progress -Activity "Waiting $totalSecs / $waitingParam"
					}
					$timer.Stop()
					
					## check, if while loop stopped because of file or elapsed time
					if ($timer.Elapsed.TotalSeconds -gt $waitingParam)
					{
						Stop-Process -Id $app.Id
						Write-Host "too long"
						if ($q -eq ($m - 4)) ##set q upper limit
						{
							if ($d -eq $d_llim)
							{
								Exit
							}
							$breakFlag = 1
							break
						}
						##break
					}
					else
					{
						Write-Host "completed"
					}
				}
			}
			
			if ($breakFlag)
			{
				break
			}
		}
	}
}
## handle exit
finally
{
	Stop-Process -Id $app.Id
    write-host "Gracefully terminating"
}

##misc
##.\..\BaccArbeit\bin\main-15-03-23\main.exe $m $d $q cd $output_file n n y