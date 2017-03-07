$mystring=@"
:: This example shows how to create and execute a batch file from a powershell context/file
::

:: Set up Build Script Constants
:: This is the path to the source control sandbox
SET BUILD_ROOT=F:\ci-build\maven-appd-data_jdk2\workspace
:: The next 3 parameters will be combined to do the compilation
:: Note: Not all parameters need to be populated
:: This is the path to the compiler/build tool to run
SET BUILD_COMMAND=E:\Program Files\apache-maven-3.3.1\bin\mvn.cmd
:: This is the build file to be used....e.g POM.xml
SET BUILD_SCRIPT=
:: These are the build targets to be used
SET BUILD_PARAMS=
::SET BUILD_TYPE=
ECHO .
ECHO ###################################
ECHO Done!
"@

$mystring >> output.bat
invoke-expression '& "output.bat"' 