#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: login feature

  Background: setup steps for login feature
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login page

  @hrmNavigate
  Scenario: Validate navigation to OrangeHRM
    Then User should see page title as OrangeHRM

  @hrmLogin
  Scenario: Login as admin
    When User enter valied ID,valied password and click Login button
    Then User should navigate to Dash board menu

  @loginDDT
  Scenario Outline: Validate login to OrangeHRM site with Parameters
    When User enter username: "<username>", password: "<password>" and click Login button
    Then User should navigate to Dash board menu

    Examples: 
      | username | password  | expected_url    |
      | Admin    | admin123  | dashboard/index |
      | admin    | admin1234 | auth/login      |
      | admin1   | admin123  | auth/login      |
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |
