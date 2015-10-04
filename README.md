# ToDoApplication
To Do Web Application in Python Flask <br><br>
To Run:<br>
Open a virtual environment with virtualenv venv --distribute <br> source venv/bin/activate <br>
pip install -r requirements.txt <br>
pip install mysql-python <br>
If mysql fails need to install mysql first: <br>
<ul>
<li>On linux this should fix the problem: apt-get install build-essential python-dev libmysqlclient-dev </li>
<li>On Mac or Windows read here. <a href="http://mysql-python.blogspot.com/2012/11/is-mysqldb-hard-to-install.html">here</a> </li>
<li>On My Mac I ran brew install mysql and then had to run sudo chown -R $(whoami) /usr/local/ because the link failed. Then I had to run brew link mysql. FINALLY pip install mysql-python worked just fine. :)</li>
</ul>
run with python app.py
