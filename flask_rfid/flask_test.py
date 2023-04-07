from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/json_test')
def hello_json():
    f = open("read_data.txt", 'r')
    id=f.readline()
    while id=='':
        id=f.readline()
    id=id.strip()
    text=f.readline().strip()
    f.close()
    f = open("read_data.txt", 'w')
    f.close()
    data = {'id' : id, 'text':text}
    return jsonify(data)

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port = "8080")