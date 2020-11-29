Feature: Retirement Age
  Calculate my retirement age.

    Scenario Outline: test birth years and months
    Given year of birth of "<y>" and month of "<m>"
    When user presses the return key
    Then user will receive message Your full retirement age is "<n>"

    Examples: Amounts
      | y  | m | n |
      | 1999| 8 | 67  |
      |1937 | 1 | 65  |
      | 1938  | 2 | 65 2  |
      | 1939  | 3 | 65 4  |
      | 1940  | 4 | 65 6  |
      | 1941  | 5 | 65 8  |
      | 1942  | 6 | 65 10 |
      | 1943  | 7 | 66    |
      | 1955  | 8 | 66 2  |
      | 1956  | 9 | 66 4  |
      | 1957  | 10 | 66 6 |
      | 1958  | 11 | 66 8 |
      | 1959  | 12 | 66 10 |
      | 1960  | 1 | 67    |
      | 2019  | 8 | 67    |


  Scenario: Birth date below 1900
    Given year of birth of 1899
    When user presses the return key
    Then user receives message Please enter valid year

  Scenario: Birth date above 2019
    Given year of birth of 2020
    When user presses the return key
    Then user receives message Please enter valid year

  Scenario: Testing if user enters month below 1 or above 12
	Given year of birth of 1970 AND birth month of 0
	When user presses the return key
	Then user will receive message Please enter a valid month

  Scenario: Testing to see if year counts up when birth month plus retirmenet month equals new year
	Given year of birth of 1940 AND a birth month of July
	When user presses the return key
	Then user will receive message Your full retirement age is 65 and 6 months, this will be in January of 2006
