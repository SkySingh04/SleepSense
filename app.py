from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_bootstrap import Bootstrap4
from graphs import generateGraph
from conclusions import most_Drowsy , fatiguepredictions

app = Flask(__name__)
bootstrap = Bootstrap4(app)


video_stream = VideoCamera()

@app.route('/')
def index():
    with open('location.txt',"r") as f:
        data = f.read()
    with open('mostdrowsy.txt',"r") as f:
        drowsy_data = f.read()
    with open('optimalbreak.txt',"r") as f:
        rest_data = f.read()
    return render_template('index.html',home=True,data=data,drowsy_data=drowsy_data,rest_data=rest_data)

def gen(camera):
    while True:
        #This part of the code ensures we can see ourselves on the website, also prolly responsible for low framerate
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
     return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/data")
def data():
    return render_template("graphs.html")

@app.route("/update")
def update():
    generateGraph()
    most_Drowsy()
    fatiguepredictions()
    with open('location.txt',"r") as f:
        data = f.read()
    with open('mostdrowsy.txt',"r") as f:
        drowsy_data = f.read()
    with open('optimalbreak.txt',"r") as f:
        rest_data = f.read()
    return render_template('index.html',home=True,data=data,drowsy_data=drowsy_data,rest_data=rest_data)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")