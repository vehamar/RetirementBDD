# Created by medic at 11/28/2019
Feature: Retirement Age Calculator
  I want to know at what age I can recieve
  full benefits from Social Security

  Scenario Outline: Calculate retirement age
    Given the user is prompted to enter the birth_year
    When the user enters their "<birth_year>"
    Then the users "<retire_age>" and "<retire_months>" will be returned

    Examples: Retirement Age
      | birth_year  | retire_age  | retire_months  |
      | 1900        | 65          | 0              |
      | 1937        | 65          | 0              |
      | 1938        | 65          | 2              |
      | 1939        | 65          | 4              |
      | 1940        | 65          | 6              |
      | 1941        | 65          | 8              |
      | 1942        | 65          | 10             |
      | 1943        | 66          | 0              |
      | 1955        | 66          | 2              |
      | 1956        | 66          | 4              |
      | 1957        | 66          | 6              |
      | 1958        | 66          | 8              |
      | 1959        | 66          | 10             |
      | 1960        | 67          | 0              |
      | 2019        | 67          | 0              |

