from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

dict = {'reverse': 'prueba',  'lengt':'', 'vowels':'', 'consonant':'', 'updown':''}

app = Flask(__name__)
#with open('data.json') as json_file:
#    my_json = json.load(json_file)
    
#@app.route('/ind')
#def index():
#    template = env.get_template('index.html')
#    return template.render(my_data=my_json['data'], headers=my_json['headers'])

@app.route('/')
@app.route('/crear', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        _name = request.form['name']
        print ({_name})
        return redirect(url_for("form"))
    name = "prueba"
    template = env.get_template('form.html')
    return template.render()

if __name__ == '__main__':
    app.run(debug=True)