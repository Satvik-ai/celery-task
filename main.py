# from  workers import celery_app
from workers import create_celery_app
import task
from flask import Flask,request,jsonify
from celery.result import AsyncResult

app = Flask(__name__)

# cel_app = celery_app
cel_app = create_celery_app(app)

# command to run the celery app :- celery -A main:cel_app worker -l INFO --pool=solo

@app.post('/sum')
def sum():
    a = request.json['a']
    b = request.json['b']
    ans = task.sum.delay(a,b)
    return jsonify(ans.id)

@app.get('/get-sum/<id>')
def get_sum(id):
    s = AsyncResult(id)
    res = {
        "Ready": s.ready(), # This methpd will tell weather task execution is complete or not
        "Result": s.result if s.ready() else None
    }
    return res


if __name__ == "__main__":
    app.run(debug=True)