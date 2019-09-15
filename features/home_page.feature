@smoke


  Feature:  Navigating to github page and searching for this repo

#    Background: Navigating to github page and searching for this repo

    Scenario: search this repository in Github
      Given I navigate to github
      Then I type python+behave
      And I hit enter
      Then I see the results
      And I select python+behave
