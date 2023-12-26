@rem Set JAVA_EXE to java.exe in the allure folder
set "JAVA_EXE=java.exe"

if not exist "%JAVA_EXE%" (
    echo.
    echo ERROR: Could not find java.exe in the allure folder: %DIRNAME%
    echo.
    echo Please make sure the java.exe is present in the specified location.
    goto fail
)

@rem Setup the command line
set CLASSPATH=%DIRNAME%allure-commandline-2.24.1.jar

@rem Execute allure
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %ALLURE_OPTS% -classpath "%CLASSPATH%" io.qameta.allure.CommandLine %*

:end
@rem End local scope for the variables with windows NT shell
if %ERRORLEVEL% equ 0 goto mainEnd

:fail
rem Set variable ALLURE_EXIT_CONSOLE if you need the Script return code instead of
rem the cmd.exe /c return code!
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% equ 0 set EXIT_CODE=1
if not "%ALLURE_EXIT_CONSOLE%"=="" exit %EXIT_CODE%
exit /b %EXIT_CODE%

:mainEnd
if "%OS%"=="Windows_NT" endlocal
