from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route("/stock/<code>")
def get_stock(code):
    return send_from_directory("csv_files/", code+".csv")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', threaded=True)




#pip install virtualenv
#USING google drive API  
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  
