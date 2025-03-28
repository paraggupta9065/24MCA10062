> [!CAUTION]
> At last this error came at 1 pm so we were not able to put screenshort we were instructed to work till 1:30

{
"message": "given email is not registered"
}

> [!CAUTION]
> Unable to get proper idea of solution from docs as result we wasted time \n
> [!IMPORTANT]
> Potential improvement
>
> Use of database in backend \n
> Use of redux thunk in frontend \n
> better searching and sorting \n

# Basic Frontend And Backend

I tried my best to complete calculater backend is completed, social media backend is completed but react is not fully completed, i have used proper folder structure in it

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

# Social media Frontend And Backend

## Problem 2 Backend

I am using same approtch for backend as above

Respose for api 1
`
{
  "posts": [
    {
      "content": "Post about vampire",
      "id": 260,
      "userid": 10
    },
    {
      "content": "Post about kite",
      "id": 118,
      "userid": 10
    },
    {
      "content": "Post about lamp",
      "id": 140,
      "userid": 10
    },
    {
      "content": "Post about mountain",
      "id": 634,
      "userid": 10
    },
    {
      "content": "Post about elephant",
      "id": 633,
      "userid": 10
    }
  ]
}`

Respose for api 2
`[
    {
        "content": "Post about mountain",
        "id": 634,
        "userid": 10
    },
    {
        "content": "Post about elephant",
        "id": 633,
        "userid": 10
    },
    {
        "content": "Post about vampire",
        "id": 260,
        "userid": 10
    },
    {
        "content": "Post about kite",
        "id": 118,
        "userid": 10
    },
    {
        "content": "Post about lamp",
        "id": 140,
        "userid": 10
    }
]`

## Problem 2 Frontend

I will use react with vite
<img width="1440" alt="Screenshot 2025-03-28 at 1 10 19 PM" src="https://github.com/user-attachments/assets/b8cb913f-0151-4bac-a2fa-2b0fe9df4bba" />

> [!NOTE]
> I took refrence from flask docs, stackoverflow, github issues and react
