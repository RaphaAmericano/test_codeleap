
# Back-end Challenge - CodeLeap

Base endpoint https://test-codeleap.onrender.com


## Get Posts

### Request

`GET /carrers`

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [{
	    "id": 7,
	    "username": "Raphael",
	    "title": "Testando",
	    "content": "Testando o conteudo",
	    "created_datetime": "2024-12-06T16:03:25.864499Z"
	 
    },
    {
	    "id": 8,"
	    username": "Joao",
	    "title": "Vida dos animais",
	    "content": "Uma história sobre a vida dos animais.",
	    "created_datetime": "2024-12-06T16:05:42.095913Z"
    }]

## Create a post

### Request

`POST /carrers`

    {
	    "username":"Raphael",
	    "title":"Testando",
	    "content": "Testando o conteudo"
    }

### Response

      {
   	    "username":"Raphael",
   	    "title":"Testando",
   	    "content": "Testando o conteudo"
       }


## Update Post

`PATCH /careers/:id`

    {
	    "title":"Vida dos cachorros", 
	    "content": "Uma história sobre a vida dos cachorros no campo."
    }

### Response

    {
    "title":"Vida dos cachorros", 
    "content": "Uma história sobre a vida dos cachorros no campo."
    }


## Delete a Post

### Request

`DELETE /careers/:id`

### Response
	{}

