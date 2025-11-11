@echo OFF
SETLOCAL
cls

if "%1%" == "" (
	set PYTHONDIR=%SystemDrive%\Python27
) else (
	set PYTHONDIR=%1%
)

if "%PYTHONPATH%" == "" (
	set PYTHONPATH=.
)

set PYTHONPATH=%PYTHONPATH%;..

echo Running tests using %PYTHONDIR%
%PYTHONDIR%\python.exe -m unittest discover -p "test_*.py"


set UNITTEST_EC=%ERRORLEVEL%
echo Finished running tests!


REM ---------------------------------------------------------------------------
:exit_door
exit /B %UNITTEST_EC%