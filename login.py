from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    json_content = request.get_json()
    username = json_content.get('username')
    password = json_content.get('password')

    response_code = 0
    response_msg = ""


    if len(password) < 6:
        response_code = 201
        response_msg = "Failure: password should be of length 6"

    elif password.isalpha():
        response_code = 202
        response_msg = "Failure: password to have 1 character and 1 number"

    elif not username.isalpha():
        response_code = 203
        response_msg = "Failure: only characters allowed in username"
    else:
        response_code = 200
        response_msg = "Success"

    return {
        "status": response_code,
        "msg": response_msg
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
