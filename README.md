#mongodb

{username: "jorge", name="Jorge", email="xxx"}
{"username": "richard", name="Jorge", email="xxx"}
{"username": "jorge", name="Jorge", email="xxx"}
{"username": "jorge", name="Jorge", email="xxx"}


systemLog:
   destination: file
   path: "/home/ubuntu/log/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: false
   dbPath: "/home/ubuntu/data"
processManagement:
   fork: true
net:
   bindIp: 0.0.0.0
   port: 27017
   http:
      enabled: true
      RESTInterfaceEnabled: true
 
hoang d vo07/12/2019
db.test.insert({name: "Hoang", last_name: "Vo"})
WriteResult({ "nInserted" : 1 })
sudo apt-get install -y mongodb
db.test.find()
db.test.createIndex({ last_name: 1})
db.test.find({ age: {$lt: 40} })
db.test.find({ name: "Al", last_name: "machine"})
db.test.update({name: "Danthes"}, { $set : {last_name: "matthew"} })
python:
$ virtualenv -p python3 venv
 
hoang d vo07/12/2019
pip install -r requirements.txt
 
hoang d vo07/15/2019
Attachment file type: acrobat
mongodb_instruction.pdf
2.26 MB
 
hoang d voToday at 1:00 AM
python manage.py shell
from user.models import User
user = User(username="jorge", password="test", email="jorge@fromzero.io", first_name="jorge", last_name="Escobar")
user
<User: User object>

user.username
user.save()
user.id

Using 'user.id' after 'user.save()'

