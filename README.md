# Flask-and-api
A web API using flask and Python ,

request method-POST,

#check method Process

goto Postman enter the url with/login,

method post

output in JSON format,

goto body and select raw input and enter username and password in JSON,

send request

Test Cases:

Case 1
Input: 
{    "username": "vaibhav",
     "password": "abcd12"
}
Output
{    "status": 200,
     "msg": "Success"
}

Case 2
Input: 
{    "username": "vaibhav",
     "password": "abcd"
}
Output
{    "status": 201,
     "msg": "Failure: password should be of length 6"
}

Case 3
Input: 
{    "username": "vaibhav",
     "password": "abcdef"
}
Output
{    "status": 202,
     "msg": "Failure: password to have 1 character and 1 number"
}

Case 4
Input: 
{    "username": "1234",
     "password": "abcd12"
}
Output
{    "status": 203,
     "msg": "Failure: only characters allowed in username"
}
