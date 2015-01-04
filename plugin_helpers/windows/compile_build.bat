@echo off

:: Set msbuild.exe's path
set MSBUILD=C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild

:: Set the passed variables
set BRANCHNAME=%1

:: Validate the given branch name
if not exist %SOURCEPYTHONDIR%\src\makefiles\branch\%BRANCHNAME%.cmake (

    echo Invalid branch '%BRANCHNAME%'.
    exit 1
)

:: Store the branch's repo directory
set BRANCHDIR=%SOURCEPYTHONDIR%\src\hl2sdk\%BRANCHNAME%

:: Create the branch's repo if it doesn't exist
if not exist %BRANCHDIR% (
    mkdir %BRANCHDIR%
    git clone https://github.com/alliedmodders/hl2sdk.git %BRANCHDIR%
)

:: Navigate to the branch's repo directory
cd %BRANCHDIR%

:: Force checkout to checkout the specified branch and remove previous patches
git checkout -f %BRANCHNAME%

:: Exit if an error was encountered
if %errorlevel% gtr 0 exit

:: Pull any new changes to the branch
git pull

:: Exit if an error was encountered
if %errorlevel% gtr 0 exit

:: Store the patches directory for the branch
set PATCHDIR=%SOURCEPYTHONDIR%\src\patches\%BRANCHNAME%

:: Copy the patches to the branch
if exist %PATCHDIR% xcopy %PATCHDIR% %BRANCHDIR% /y/s

:: Navigate to the main src directory
cd %SOURCEPYTHONDIR%\src

:: Store the build directory for the branch
set BUILDDIR=%SOURCEPYTHONDIR%\src\Builds\%BRANCHNAME%

:: Create the build directory if it doesn't exist
if not exist %BUILDDIR% mkdir %BUILDDIR%

:: Create the solution for the build
cmake . -B%BUILDDIR% -G"Visual Studio 10" -DBRANCH=%BRANCHNAME%

:: Build the binaries
%MSBUILD% %BUILDDIR%\source-python.sln /p:Configuration=Release /p:DebugSymbols=false /p:DebugType=None
