#import the Flask class from the flask package
from flask import Flask

#create application object
app = Flask(__name__)

#use decorators to link the function to URL
@app.route("/")
@app.route("/hello")

#define the view using function which returns string
def hello_world():
  return "Hello World from Madhu first Flask Test"

#start the development server using the run() method
if __name__ == "__main__":
  app.run()
