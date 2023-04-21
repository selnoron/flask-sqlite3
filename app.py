# flask
import flask 
from services.interface import DB, User
import names 
import random as rd


db: DB = DB()

for _ in range(50):
    user = User(
        login=f'{names.get_first_name()}',
        password=f'{rd.randint(1000, 5000)}',
        os_version=rd.choice(["Windows10", "MAC OS", "LINUX", "MS DOS"])
    )
    result_regictration = db.registrate_user(data=user)

result_users = db.get_all_users()

app: flask.app.Flask = flask.Flask(__name__) 

@app.route('/', methods=['POST', 'GET']) 
def get_users() -> str: 
    sorted_users = sorted(result_users, key=lambda user: user[1])
    print(sorted_users)
    return flask.render_template(
        'index.html',
        users=sorted_users
    )

if __name__ == '__main__': 
    app.run( 
        host='localhost', 
        port=8080, 
        debug=True 
    )


