from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def abalone_sex():
    '''Hello world function'''
    sex_pred = 'press_submit'
    data = 'Before submit'
    PATH_MODEL = './models/model_saved.sav'
    saved_model = joblib.load(PATH_MODEL)
    if request.method == 'POST':
        # data = {'length': [request.form['length']],
        #         'diameter': [request.form['diameter']],
        #         'height': [request.form['height']],
        #         'whole_weight': [request.form['whole_weight']],
        #         'shucked_weight': [request.form['shucked_weight']],
        #         'viscera_weight': [request.form['viscera_weight']],
        #         'shell_weight': [request.form['shell_weight']],
        #         'rings':[request.form['rings']]}
        data = eval(request.form["text_data"])
        X = pd.DataFrame.from_dict(data)
        sex_pred = saved_model.predict(X)
    return render_template('index2.html', sex_pred=sex_pred,data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
