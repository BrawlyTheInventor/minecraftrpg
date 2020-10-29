from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)

@app.route('/chatpost', methods=['POST'])
def endpoint():
    input_json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    print ('data from client:', input_json)
    returninput = str(input_json)
    
    myfile = "/home/pi/templates/Mclatestchat.txt"

    with open(myfile, "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(returninput)
        f.truncate()
    dictToReturn = {'':''}
    return jsonify(dictToReturn)
@app.route('/returnchat', methods=['GET'])
def returnchat():
    return render_template('Mclatestchat.txt')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
