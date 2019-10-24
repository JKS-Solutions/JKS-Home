from flask import render_template
from src import app

import json
import requests

dvs = []

@app.route("/developers")
def devs():
    
    if(len(dvs) < 1):
        baseurl = "https://api.github.com/users/"
        developers = ["EssKayz", "xTooth"]
        
        for x in range(len(developers)):
            dvs.append(json.loads(requests.get(baseurl + developers[x]).text) )
        
    return render_template("developers.html", devs=dvs)