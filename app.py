from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
bootstrap = Bootstrap4(app)


video_stream = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html',home=True)

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

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")