# language: en
# author: Hernan Malave

Feature: User submits multiple forms to demonstrate automation skills

  As a candidate,
  I want to submit multiple user data forms automatically
  So that I can demonstrate my automation capabilities in filling forms efficiently

  Scenario: user submits multiple forms
    Given user open url
    When user sends 50 forms
    Then user ends the challenge
