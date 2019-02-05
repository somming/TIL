from flask import Flask, request
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

#Argument Parsing : email, user_name, password 파라미터를 추가하고 파서를 사용해 파라미터를 추출할 수 있다.
class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']
            return {'Email': args['email'], 'UserName': args['user_name'], 'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/user')
api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

'''
curl http://localhost:5000/todo/1 -d "data=Remember the milk" -X PUT
curl http://localhost:5000/todo/1
post방식으로 데이터 보내기 : curl -d "email=dasom@naver.com&user_name=dasom&password=1234" http://localhost:5000/user
'''