from flask import Flask, render_template, request
from flask.ext.mysqldb import MySQL
import os

app = Flask(__name__, template_folder='views')
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
mysql.init_app(app)


@app.route("/", methods=['POST', 'GET'])
def main():
	cur = mysql.connection.cursor()

	if request.method == 'POST':
		if request.form['op'] == 'add':
			newTask = request.form['newTask']
			cur.execute('''INSERT INTO oneNorth.Task (task) VALUES (%s)''',(newTask,))
			mysql.connection.commit()
			message = "Task added sucessfully"
			print message

		elif request.form['op'] == 'delete':
			deleteTask = request.form['deleteTask']
			cur = mysql.connection.cursor()
			cur.execute('''DELETE FROM oneNorth.Task where task = %s''',(deleteTask,))
			mysql.connection.commit()
			message = "Task deleted sucessfully"
			print message

		elif request.form['op'] == 'edit':
				editTask = request.form['editTask']
				editTaskid = request.form['editTaskid']
				cur = mysql.connection.cursor()
				cur.execute('''UPDATE oneNorth.Task SET task = %s WHERE taskid = %s''',(editTask, editTaskid))
				mysql.connection.commit()
				message = "Task edited sucessfully"
				print message
	cur.execute('''SELECT task, taskid FROM oneNorth.Task''')
	tasks = cur.fetchall()
	return render_template("index.html", tasks = tasks)



if __name__ == "__main__":

    app.run()