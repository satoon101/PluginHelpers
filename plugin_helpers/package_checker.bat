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

python -m pylint --rcfile .pylintrc %STARTDIR%\packages --const-rgx="(([A-Z_][A-Z0-9_]*)|([a-z_][a-z0-9_]*)|(__.*__))$" --msg-template="{msg_id}:{line:3d},{column:2d}: {msg} ({symbol})"

echo.
echo.
)
pause