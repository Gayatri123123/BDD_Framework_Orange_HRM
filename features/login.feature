Feature: Login functionality

  Background: Common steps
    Given I lauched chrome browser
    When I open orange HRM Homepage
    And Enter username "Admin" and password "admin123"
    And clicks on Login button

  @search
  Scenario: Login with valid credentials
    Then user should get logged in to dashboard page
  @search1
  Scenario: Login with valid credentials
    When click on Admin button
    Then highlight the System users
