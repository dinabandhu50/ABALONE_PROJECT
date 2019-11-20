from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])

def abalone_sex():
    '''Hello world function'''
    if request.method == 'POST':
        length = request.form['length']
        diameter = request.form['diameter']
        height = request.form['height']
        whole_weight = request.form['whole_weight']
        shucked_weight = request.form['shucked_weight']
        viscera_weight = request.form['viscera_weight']
        shell_weight = request.form['shell_weight']      
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
