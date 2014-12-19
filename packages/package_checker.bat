@echo off

set STARTDIR="%CD%"

for /D %%i in (*.*) do (

    echo ============================================
    echo Checking %%~ni for PEP8 standards:
    echo ============================================
    echo.

    python -m pep8 --count --benchmark %STARTDIR%\%%~ni

    echo.
    echo.
    echo ==============================================
    echo Checking %%~ni for PEP257 standards:
    echo ==============================================
    echo.

    python -m pep257 %STARTDIR%\%%~ni

    echo.
    echo.
    echo ============================================
    echo Checking %%~ni for unused imports:
    echo ============================================
    echo.

    python -m pyflakes %STARTDIR%\%%~ni

    echo.
    echo.
    echo =====================================
    echo Checking %%~ni with PyLint:
    echo =====================================
    echo.

    python -m pylint --rcfile ../.pylintrc %STARTDIR%\%%~ni --const-rgx="(([A-Z_][A-Z0-9_]*)|([a-z_][a-z0-9_]*)|(__.*__))$" --msg-template="{msg_id}:{line:3d},{column:2d}: {msg} ({symbol})"

    echo.
    echo.
)
pause