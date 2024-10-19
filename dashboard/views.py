from flask import Blueprint, render_template, current_app, url_for, request, redirect
import json
from datetime import datetime, timedelta, timezone
from dateutil import parser
# Define the blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
@mainbp.route('/<string:submitted_date>')
def index(submitted_date=None):
    # Access the db from the app's config
    db = current_app.config['db']
    collectionData = db.test  # Access the collection 'har'
    specific_date= datetime.now()
    if submitted_date is None:
        specific_date = datetime.now(timezone.utc)
    elif submitted_date is not None:
        new_date = parser.isoparse(submitted_date)
        specific_date = new_date;
    start_of_day = specific_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = specific_date.replace(hour=23, minute=59, second=59, microsecond=999999)

    iso_start_of_day = start_of_day.isoformat()
    iso_end_of_day = end_of_day.isoformat()

    print(f"{iso_start_of_day}")

    # Fetch data from MongoDB  
    activityData = [
        {key: value for key, value in item.items() if key != '_id'}
        for item in collectionData.find({
        'timestamp': {
            '$gte': start_of_day,
            '$lt': end_of_day
        }
    })
    ]
    #testing
    for item in activityData:
        print(item)

    return render_template('index.html', activityData=activityData)

@mainbp.route('/search', methods=['POST'])
def find():
    print('Method type:', request.method)
    
    search_query = request.form.get('search')  
    
    if search_query:
        print(search_query)
        query = "%" + search_query + "%"
        return redirect(url_for('main.index', submitted_date=query))
    return redirect(url_for('main.index'))  # Redirect or handle as needed
