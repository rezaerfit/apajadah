# from crypt import methods
from operator import mod
from flask import Flask, request
from flask import Flask, render_template
import joblib
# import sklearn
# from sklearn.neighbors import KNeighborsClassifier
import numpy as np
app = Flask(__name__)

@app.route("/" , methods=['POST','get'])
def index():
    if request.method == 'POST':
        model = joblib.load('tensi_joblib')
        sistolik = float(request.form['sistolik'])
        diastolik = float(request.form['diastolik'])
        
        datas = np.array([[sistolik,diastolik]]) 
        
        isTensi = model.predict(datas)
        (datas)
        return render_template ('hasil.html', finalData = isTensi)
    else:
        return render_template ('index.html')

if __name__ == "__main__":
    app.run(debug=True)
