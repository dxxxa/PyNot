@Echo Off
cls
	Set "Folder=%CD%"
	FOR /F "usebackq delims=" %%i In (`2^>nul Dir "%Folder%" /S /B /A:D^|Sort /R`) DO >nul 2>&1 Rd "%%i"
Pause
Exit /B