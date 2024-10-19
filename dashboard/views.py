from flask import Blueprint, render_template, current_app
import json
# Define the blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    # Access the db from the app's config
    db = current_app.config['db']
    collectionData = db.test  # Access the collection 'har'
    
    # Fetch data from MongoDB  
    activityData = [
        {key: value for key, value in item.items() if key != '_id'}
        for item in collectionData.find()
    ]
    #testing
    for item in activityData:
        print(item)

    return render_template('index.html', activityData=activityData)
