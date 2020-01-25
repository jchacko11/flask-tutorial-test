from flask import Flask, jsonify

users = {}
def addUser(userId, first, last, status, target, assassin):
    users[userId] = [first, last, status, target, assassin]

def getTarget(userId):
    return users[userId][3]

def getName(userId):
    return users[userId][0] + " " + users[userId][1]

def getStatus(userId):
    return users[userId][2]

def getAssassin(userId):
    return users[userId][4]

addUser(2321, "Anna", "Kolodziejcyk", "Active", "Lauren", "Jonathan")
print(users)
print(getTarget(2321))
print(getName(2321))
print(getStatus(2321))
print(getAssassin(2321))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Wor1ld!'


@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name

'''
@app.route("/users", method=["GET"])              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return jsonify(users)          # which returns "hello + name
'''

@app.route("/users", methods=["GET"])
def list_todo():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

