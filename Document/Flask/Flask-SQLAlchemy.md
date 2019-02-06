## Flask-SQLAlchemy 사용하기

파이썬에서 연결 가능한 데이터베이스는 모두 Flask에서도 이용할 수 있다.

데이터베이스는 데이터를 저장하고 다루는 방식에 따라서 크게 `RDBMS(관계형 데이터베이스)`와 `NoSQL(비관계형 데이터베이스)`로 나누어진다.

이 중 RDBMS는 데이터를 질의, 입력, 수정, 삭제 등 조작을 할 때 SQL이라는 언어를 사용한다.
따라서 개발을 할 때 이 SQL을 사용해야한다.

또한 데이터베이스에 따라 사용하는 SQL문이 다르기 때문에, 이 또한 염두에 두어야 한다.

또 다른 단점으로는, 관계가 복잡해지면 SQL문도 복잡해지는 경우가 있다.

만약 SQL문 대신 프로그램 언어만으로 데이터베이스를 조작할 수 있다면, 개발이 더 간편해지지 않을까?

이러한 고민에서 ORM(Object-Relational Mapping , 객제 관계 매핑) 기술에 기반한 SQLAlchemy 라이브러리가 배포되었다.

```
SQLAlchemy는 관계형 데이터베이스를 프로그램에서 쉽게 조작하고 사용할 수 있도록 도와주는 라이브러리다. 
```

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://[username]:[password]@[hostname]/[database]'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id',db.Integer,primary_key=True)
	data = db.Column('data',db.Unicode)

	def __init__(self, id, data):
		self.id = id
		self.data = data
```

이렇게 간단하게, 객체와 연결해서 데이터베이스를 조작할 수 있다.

```
>>> from alchemy import Example
>>> examples = Example.query.all()
>>> for ex in examples:
...     print(ex.data)
```
내 DB에 있는 data를 읽어와 출력해준다.

```
>>> from alchemy import db
>>> new_ex = Example(3, 'good girl')
>>> db.session.add(new_ex)
>>> db.session.commit()
```
db객체를 이용해 간단하게 객체를 만들어 DB에 넣어보았다.

```
>>> delete_this = Example.query.filter_by(id=2).first()
>>> db.session.delete(delete_this)
>>> db.session.commit()
```
id가 2인 객체를 삭제해보았다.

```
>>> update_this = Example.query.filter_by(id=3).first()
>>> update_this.data = 'updated!'
>>>db.session.commit()
```
id가 3인 객체의 data를 수정해보았다.

쿼리문에 전혀 신경을 쓰지 않아도 된다!
객체를 python 문법으로 마음껏 조작할 수 있다!