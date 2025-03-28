# Basic Frontend And Backend

## Problem 1

### Basic Understanding

> As there is no description of average calculator problem, i asume it is from backend task

i will be using flask for creating backend as time is constrant

i am using basic controller based folder structure which consist of controller module and main file

> Considing window size as static value which is 10

as we are getting token refreshed every time we are fetching token again on every api call

upon understangding the problem it is not clear by provided that what to send in windowCurrstate, so we asume to send number that we are fetching from server

we used plain text file as we have resource constrant

sample response of our api

`{
  "avg": 75.53333333333333,
  "numbers": [
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107
  ],
  "windowCurrstate": [
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107
  ],
  "windowPrevState": "[43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]"
}`
