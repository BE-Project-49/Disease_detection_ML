from flask import  request
from flask import render_template
from flask import current_app as app
import os
from flask import flash, request, redirect, url_for, jsonify, make_response
from werkzeug.utils import secure_filename
from requests import get

@app.route("/", methods=["GET"])
def index():  
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("index.html",img=full_filename)
	
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config.get('ALLOWED_EXTENSIONS')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print("Uploading image")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fpath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #pred= get_predictions(filename)
            base=request.base_url
            base=base[:base.index('/',7)]

            result=get(base+"/api/predict/"+filename).json()
            print(result)
            response = make_response(
                jsonify(
                    {"PredictedClass": result['predicted_class'],"imagesrc":filename}

                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
           #return render_template("index2.html",img=fpath,prediction=result["predicted_class"])
            return response
            
        
    return redirect(url_for('index'))

from application.model import classify_img
def get_predictions(filename):
    print("Get predictions")
    op=classify_img(filename)
    print(op)
    return op