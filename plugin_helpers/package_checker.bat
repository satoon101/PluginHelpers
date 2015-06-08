@echo off

set STARTDIR="%CD%"

echo ============================================
echo Checking packages for PEP8 standards:
echo ============================================
echo.
python -m pep8 --count --benchmark %STARTDIR%\packages

echo.
echo.
echo ==============================================
echo Checking packages for PEP257 standards:
echo ==============================================
echo.

python -m pep257 %STARTDIR%\packages

echo.
echo.
echo ============================================
echo Checking packages for unused imports:
echo ============================================
echo.

python -m pyflakes %STARTDIR%\packages

echo.
echo.
echo =====================================
echo Checking packages with PyLint:
echo =====================================
echo.

setlocal
set PYTHONPATH=.\packages
python -m pylint %STARTDIR%\packages --rcfile %STARTDIR%\tools\.pylintrc
endlocal

echo.
echo.
)
pause
