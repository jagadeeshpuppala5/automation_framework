Feature: Login Functionality

  Scenario: Verify login with valid credentials
    Given user launches the application
    When user enters valid email and password
    Then user should be logged in successfully

