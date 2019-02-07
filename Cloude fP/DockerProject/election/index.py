from flask import Flask, request, render_template, redirect
import json
from flaskext.mysql import MySQL
from cryptography.fernet import Fernet

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'ninja'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'mydata'
app.config['MYSQL_DATABASE_HOST'] = 'database'
mysql.init_app(app)


@app.route('/<userid>', methods=['POST', 'GET'])
def getelection(userid):
  # if (request.method != 'POST' and request.method != 'GET'):
        conversion = "select ElH_id , Cndidate  from ElectionD where ElectionD.ElH_id not in (select User_Election.ElH_id  from User_Election where User_Election.user_id = %s)"
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute(conversion, [request.args.get('userid')])
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        data = cursor.fetchall()
        if data is None:
            result = "no election exist"
        else:
            json_data=[]
            for result in data:
                json_data.append(dict(zip(row_headers,result)))
            result = json.dumps(json_data)
        try:
                visits = redis.incr("counter")
            except RedisError:
                visits = "<i>cannot connect to Redis, counter disabled</i>"

            html = "<h3>Hello {name}!</h3>" \
                   "<b>Hostname:</b> {hostname}<br/>" \
                   "<b>Visits:</b> {visits}"
            visit html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

        return render_template('index.html', result=result, visit=visit)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
