from flask import Blueprint, request, jsonify
from Event.models import Event
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated, query_all
)
from Event import db
from datetime import datetime, date


events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint


@events.route("", methods=["POST"])
def create_event():


    title = request.json['title']
    description = request.json['description']
    location = request.json['location']
    start_date = request.json['start_date']
    start_time = request.json['start_time']
    end_date = request.json['end_date']
    end_time = request.json['end_time']
    thumbnail = request.json['thumbnail']
    creator = request.json['creator']
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    start_time = datetime.strptime(start_time,'%H:%M:%S')
    end_time = datetime.strptime(end_time,'%H:%M:%S')


    event = Event(title=title,description=description,location=location,start_date=start_date,
                start_time=start_time,end_date=end_date,end_time=end_time,thumbnail=thumbnail,creator=creator)
    result = format(event)            
    try:
        event.insert()
    except:
        return {"message": "An error occurred creating the event."}, 400
    return jsonify({
        'msg': "Event Created",
        'event': result }), 201 

    # event.insert()   
    # result = format(event)
    # print(type(result))   
    # return jsonify(result), 201
   














