
Feature: Reelly off plan page functionalities


  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open the main page
    When User logs in with "shaminasoukath10@gmail.com" and "Sh@minatest2025"
    And Click on “off plan” at the left side menu
    Then Verify the right page opens
    And  Verify each product on this page contains a title and a visible picture