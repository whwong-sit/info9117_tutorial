Feature: Hello World
  As a Visitor
  I want to be greeted by a welcome message
  when I visit the landing page

  Scenario: Visit Main Page
    Given The system is running
    When a Visitor visits the landing page
    Then a welcome message is returned to the Visitor