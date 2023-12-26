Feature: Login functionality


  Scenario Outline: Login with multiple parameters
    Given I lauched browser chrome
    When I open orange HRM page
    And Enter username "<username>" and password "<password>" fields
    And clicks on Login
    Then user should get logged into Dashboard Page of HRM

    Examples:
      |username|password |
      |  Admin |admin123 |
      |  Admin |admin1234|
