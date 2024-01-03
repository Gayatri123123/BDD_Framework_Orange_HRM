call ./Scripts/activate.bat
call behave -f allure_behave.formatter:AllureFormatter -o Reports\allure_result
call allure generate Reports\allure_result -o Reports\allure_report --clean
