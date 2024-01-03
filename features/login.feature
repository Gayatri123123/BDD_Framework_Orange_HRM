Feature: Login functionality

  Background: Common steps
    Given I lauched the browser
    When I open orange HRM Homepage

  @Dashboard
  Scenario: Login with valid credentials
    When Enter username "Admin" and password "admin123"
    When clicks on Login button
    Then user should get logged into dashboard page

  @Adminpage
  Scenario: Login with valid credentials for admin page
    When Enter username "Admin" and password "admin123"
    When clicks on Login button
    When click on Admin button
    Then highlight the System users

  @Invalid
  Scenario:Login with Invalid credentials
    When Enter Invalid username "abc" and password "abc123"
    And clicks on Login button
    Then user should get proper error message
