from flask import Flask, jsonify
from .rfid import read

app=Flask(__name__)

@app.route('/json_test')
def hellow_json():
    f = open("read_data.txt", 'r')
    id=f.readline()
    while id=='':
        id=f.readline()
    text=f.readline()
    f.close()
    data = {'id' : id, 'text':text}
    return jsonify(data)

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port = "8080")