from flask import Flask
from flask_restplus import Api,Resource,fields

app = Flask(__name__)
api = Api(app)

#model을 사용해 데이터를 관리한다. 
a_language = api.model('Language',{'language' : fields.String('The languages')})
languages = []
python = {'languages' : 'Python', 'id' : 1}
languages.append(python)

@api.route('/language')
class Language(Resource):

    #model에 있는 language값만 보여주고, id는 보여주지 않는다.
    @api.marshal_with(a_language,envelope='the_data')
    def get(self):
        return languages
    
    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)