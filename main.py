# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, Response, render_template, request, session, url_for, redirect
from google.cloud import datastore
from datetime import datetime
import os


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

#datastore_client = datastore.Client()
#tulokset = []
#for i in datastore_client.query(kind="Tulokset").fetch():
#    tulokset.append({
#        "nimi": i['nimi']
#    })

#print(tulokset)

# Main page
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('lomake.html')

# Page for 100m race
@app.route('/100m', methods=['POST', 'GET'])
def kisat():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("100.html", nimet=osallistujat)

# Page for long jump race
@app.route('/pituus', methods=['POST', 'GET'])
def pituus():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("pituus.html", nimet=osallistujat)

# Page for high jump race
@app.route('/korkeus', methods=['POST', 'GET'])
def korkeus():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("korkeus.html", nimet=osallistujat)

# Page for shot put race
@app.route('/kuula', methods=['POST', 'GET'])
def kuula():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("kuula.html", nimet=osallistujat)

# Page for discus race
@app.route('/kiekko', methods=['POST', 'GET'])
def kiekko():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("kiekko.html", nimet=osallistujat)

# Page for javelin race
@app.route('/keihas', methods=['POST', 'GET'])
def keihas():
    datastore_client = datastore.Client()
    osallistujat = []
    for i in datastore_client.query(kind="Kesäkisat").fetch():
        osallistujat.append({
            "nimi": i['Nimi']
        })
    return render_template("keihas.html", nimet=osallistujat)

# Route to save participants
@app.route('/save', methods=['POST'])
def tallenna():
    datastore_client = datastore.Client()
    data = request.get_json()
    print(data['nimi'])
    kind = "Kesäkisat"
    name = datetime.now()
    name = name.strftime('%Y-%m-%d-%H:%M:%S')
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['Nimi'] = data['nimi']
    datastore_client.put(task)
    return redirect('/')

# Route to save 100m results
@app.route('/savetulos', methods=['POST'])
def save_tulokset():
    datastore_client = datastore.Client()
    data = request.get_json()
    print(data)
    #pituus = len(data['nimi'])
    kind = "100m"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)

    return kisat()

# Route to save long jump results
@app.route('/savepituus', methods=['POST'])
def save_tulokset_pituus():
    datastore_client = datastore.Client()
    data = request.get_json()
    print(data)
    #pituus = len(data['nimi'])
    kind = "Pituus"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)

    return kisat()

# Route to save high jmup results
@app.route('/savekorkeus', methods=['POST'])
def save_tulokset_korkeus():
    datastore_client = datastore.Client()
    data = request.get_json()
    kind = "Korkeus"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)

    return kisat()

# Route to save shot put results
@app.route('/savekuula', methods=['POST'])
def save_tulokset_kuula():
    datastore_client = datastore.Client()
    data = request.get_json()
    kind = "Kuula"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)
    return kisat()

# Route to save discus throw results
@app.route('/savekiekko', methods=['POST'])
def save_tulokset_kiekko():
    datastore_client = datastore.Client()
    data = request.get_json()
    kind = "Kiekko"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)
    return kisat()

# Route to save javelin throw results
@app.route('/savekeihas', methods=['POST'])
def save_tulokset_keihas():
    datastore_client = datastore.Client()
    data = request.get_json()
    kind = "Keihäs"
    name = 1
    task_key = datastore_client.key(kind, name)
    task = datastore.Entity(key=task_key)
    task['nimi'] = data['nimi']
    task['sija'] = data['sijoitus']
    
    datastore_client.put(task)
    return kisat()

# Route to results. For every sport and end results
@app.route('/tulokset')
def tulokset():
    datastore_client = datastore.Client()
    tulokset = []
    for i in datastore_client.query(kind="100m").fetch():
        tulokset.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    pituus = []
    for i in datastore_client.query(kind="Pituus").fetch():
        pituus.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    korkeus = []
    for i in datastore_client.query(kind="Korkeus").fetch():
        korkeus.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    kuula = []
    for i in datastore_client.query(kind="Kuula").fetch():
        kuula.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    kiekko = []
    for i in datastore_client.query(kind="Kiekko").fetch():
        kiekko.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    keihas = []
    for i in datastore_client.query(kind="Keihäs").fetch():
        keihas.append({
            "nimi": i['nimi'],
            "sijoitus": i['sija']
        })
    return render_template('tulokset.html', tulokset=tulokset, pituus=pituus, korkeus=korkeus,kuula=kuula,kiekko=kiekko,keihas=keihas)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
