import os
import numpy as np #used for numerical analysis
from flask import Flask,request,render_template # Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.
#render_template- used for rendering the html pages
from tensorflow.keras.models import load_model #to load our trained model
from tensorflow.keras.preprocessing import image



app=Flask(__name__)#our flask app
model=load_model(r'E:\SI-GuidedProject-8229-1641631325-cd3324a3921c6d1cb2d3eeb384d57cad1e98efe4\Training\maleria.h5')#loading the model

@app.route("/") #default route
def about():
    return render_template("about.html")#rendering html page

@app.route("/about") #route about page
def home():
    return render_template("about.html")#rendering html page

@app.route("/info") # route for info page
def information():
    return render_template("info.html")#rendering html page

@app.route("/upload") # route for uploads
def test():
    return render_template("index6.html")#rendering html page

@app.route("/predict",methods=["GET","POST"]) #route for our prediction
def upload():
    if request.method=='POST':
        f=request.files['file'] #requesting the file
        print(f)
        basepath=os.path.dirname('__file__')#storing the file directory
        print(basepath)
        filepath=os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
        f.save(filepath)#saving the file
        print(filepath)
        
        img=image.load_img(filepath,target_size=(64,64)) #load and reshaping the image
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        pred=model.predict(x)
        print("prediction",pred)#printing the prediction
        if(pred==1):#checking the results
            result="Uninfected"
        else:
            result="Infected"
        return result#resturing the result
    return None

#port = int(os.getenv("PORT"))
if __name__=="__main__":
    app.run(debug=False)#running our app
    #app.run(host='0.0.0.0', port=8000,debug=False)
            
            