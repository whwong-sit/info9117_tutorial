Feature: User Login
  As a System Owner
  I want to be able to identify users to
  personalize the platform's services to each user

  Scenario: Existing user
    Given at the login screen
    When an existing user submits correct username and password
    Then the system should identify the user
    And refer the user to the personalized main screen