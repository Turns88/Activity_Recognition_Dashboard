from flask import Blueprint, render_template, current_app, url_for, request, redirect
from datetime import datetime, timedelta, timezone
from dateutil import parser
# Define the blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
@mainbp.route('/<string:submitted_date>')
def index(submitted_date=None):
    # Access the db from the app's config
    db = current_app.config['db']
    collectionData = db.activity_summary  # Access the collection 'har'
    if submitted_date is not None:
        activityData = [
        {key: value for key, value in item.items() if key != '_id' and key != 'Timestamp'}
        for item in collectionData.find(
        {"Timestamp": submitted_date}
        )] 
    else:
        activityData = [
        {key: value for key, value in item.items() if key != '_id' and key != 'Timestamp'}
        for item in collectionData.find()
        ]

    if len(activityData) >= 1:
        activities = list(activityData[0].keys())
        durations = list(activityData[0].values())

    else:

        activities = []
        durations = []

    activities_and_durations = zip(activities, durations)
    activity_dicts = [{'activity': activity, 'duration': duration} for activity, duration in activities_and_durations]
    return render_template('index.html', activities_and_durations=activities_and_durations , activity_dicts=activity_dicts)
@mainbp.route('/search', methods=['POST'])
def find():
    print('Method type:', request.method)
    submitted_date = request.form.get('submitted_date')
    if submitted_date:
        return redirect(url_for('main.index', submitted_date=submitted_date))
    return redirect(url_for('main.index'))  # Redirect or handle as needed
