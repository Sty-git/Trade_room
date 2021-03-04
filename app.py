import os
from flask import Flask, render_template, url_for, request, send_from_directory

from data_extract import final_list

app = Flask(__name__)



@app.route('/')
def index():

    return render_template("home.html", final_list=final_list)

@app.route('/data_ex')
def data_ex():

    return render_template("table.html", final_list=final_list)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


if __name__ == "__main__":
    app.run(debug=True)