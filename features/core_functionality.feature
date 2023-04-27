Feature: Core Functionality


  Scenario: Creating a Video with No Inputs
    Given a Settings file is in an expected location
    When we run the application
    Then A video consisting of only Intro and Outro is created

  Scenario: Modifying the Settings File Generates a Different Output
    Given a Settings file is in an expected location
    When we alter the settings file
    And we run the application
    Then A video consisting of a new Intro and Outro is created
