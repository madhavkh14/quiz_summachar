# quiz_summachar

Follow the below instruction to correctly setup and run the project successfully.

## Pre-requisites

<ol>
    <li>Python 3.x installed. Download it from <a href="https://www.python.org/downloads/">here</a>.</li>
    <li> Git CLI installed and setup properly. Get it from <a href="https://git-scm.com/downloads">here</a>.</li>
   </ol>
    
## Cloning project

Run the following command to clone the project

```
git clone https://github.com/madhavkh14/quiz_summachar.git
```


## Setting up the project

- Install the dependencies required for the project. From the root of the project run the following command.

    ```
        pip install -r requirements.txt
    ```
- Now to migrate all the models to database run the following command from root of the project.

    ```
        python manage.py makemigrations
        python manage.py migrate
    ```

    
## Running the project

To run and test the project, run the following command from root of the project.

```
python manage.py runserver
```

## REST API DOCUMENTATION

Documentation of our API endpoints starts here

## To create a quiz

Only Admin can access this API

### Request

`POST http://127.0.0.1:8000/api/quiz/add`

    {
        "title": "This is the first quiz created on this platform",
        "start_time": "2020-03-15T18:30:00Z",
        "end_time": "2021-07-16T00:00:00Z",
        "question": [1]
    }

### Response

    {
        "id": 2,
        "title": "This is the first quiz created on this platform",
        "start_time": "2020-03-15T18:30:00Z",
        "end_time": "2021-07-16T00:00:00Z",
        "question": [
            1
        ]
    }

## To get all the quizs

### Request

`GET http://127.0.0.1:8000/api/quiz`

### Response

    {
        "live": [
            {
                "id": 5,
                "title": "The Physics Quiz",
                "start_time": "2021-07-14T00:00:00Z",
                "end_time": "2021-07-21T00:00:00Z",
                "question": [
                    5,
                    6,
                    7
                ]
            },
            {
                "id": 6,
                "title": "Biology Quiz",
                "start_time": "2021-07-14T06:00:00Z",
                "end_time": "2021-07-24T06:00:00Z",
                "question": [
                    2,
                    4
                ]
            }
        ],
        "past": [
            {
                "id": 1,
                "title": "First Quiz",
                "start_time": "2021-07-14T07:00:00Z",
                "end_time": "2021-07-15T06:00:00Z",
                "question": [
                    1
                ]
            }
        ],
        "upcoming": [
            {
                "id": 4,
                "title": "The Second Quiz of Maths",
                "start_time": "2021-07-23T12:00:00Z",
                "end_time": "2021-07-23T18:00:00Z",
                "question": [
                    3,
                    4
                ]
            }
        ]
    }
    
## To edit/schedule a quiz

### Request

`PUT http://127.0.0.1:8000/api/quiz/<str:pk>/change`

    {
        "title": "Quiz for documentation(rename)",
        "starttime": "2020-03-16T00:00:00+05:30",
        "endtime": "2021-07-16T05:30:00+05:30",
        "question" : []
    }

### Response

    {
        "id": 2,
        "title": "Quiz for documentation(rename)",
        "starttime": "2020-03-16T00:00:00+05:30",
        "endtime": "2021-07-16T05:30:00+05:30",
        "question": []
    }
    

## To delete a quiz

### Request

`DELETE http://127.0.0.1:8000/api/quiz/<str:pk>/delete`

### Response

    {
        "message": "Quiz deleted successfully"
    }

## To create a question

### Request

` #option must be a dictionary with format "<option key>" : "<option value>" enclosed in a list`

`POST http://127.0.0.1:8000/api/question/add`

    {
        "desc": "Seventh",
        "image": null,
        "type": "MCQ",
        "option": [
           {
              "1" : "First",
              "2" : "Third"
           }
        ],
        "text": "2"
    }
    
### Response

      `{
          "id": 7,
          "desc": "Seventh",
          "image": null,
          "type": "MCQ",
          "option": "{'1': 'First', '2': 'Third'}",
          "text": "2"
      }`


## To attempt a quiz

### Request

` #response must be a dictionary with format "<question id>" : "<question response>" enclosed in a list`

`POST http://127.0.0.1:8000/api/quiz/attempt`

    {
        "response": [
           {
              "1" : "A"
           }
         ],
        "quiz": 1
    }
    
### Response

    {
        "id": 1,
        "response": "{'1': 'A'}",
        "quiz": 1,
        "user": 1
    }
    
## To register

### Request

`POST http://127.0.0.1:8000/rest-auth/registration`

    {
        "username": "abc",
        "email": "your email",
        "password1": "password",
        "password2": "password"
    }

### Response

    {
        "key": "09804914c67636b5c679cb3e2c69542411e9d330"
    }

## To login

### Request

`POST http://127.0.0.1:8000/rest-auth/login`
    
    {
        "username": "abc",
        "email": "your email",
        "password": "password"
    }
    
### Response

    {
        "key": "b7543a13964175285750e5f3f107462ef45bcc73"
    }

## To logout

### Request

`POST http://127.0.0.1:8000/rest-auth/logout`

### Response

    {
        "detail": "Successfully logged out."
    }
