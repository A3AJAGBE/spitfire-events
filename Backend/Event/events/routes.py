from flask import Blueprint, request, jsonify
from Event.models import Event
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated, query_all
)
from Event import db
from datetime import datetime, date
# from bson import json_util
import json


# import datetime

events = Blueprint("events", __name__, url_prefix="/events")#url_prefix includes /events before all endpoints in blueprint


@events.route("/api/events", methods=["POST"])
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
    
    date1 = datetime.strptime(start_date, '%Y-%m-%d')
    date2 = datetime.strptime(end_date, '%Y-%m-%d')

    start_time = datetime.strptime(start_time,'%H:%M:%S')
    end_time = datetime.strptime(end_time,'%H:%M:%S')


    event = Event(title=title,description=description,location=location,start_date=start_date,
                start_time=start_time,end_date=end_date,end_time=end_time,thumbnail=thumbnail,creator=creator)
    event.insert()   
    # try:
    #     event.insert()
    # except:
    #     return {"message": "An error occurred craeting the event."}, 400
    # return jsonify({
    #     'msg': "Event Created",
    #     'event': result }), 201 
    result = format(event)
    print(type(result))   
    return jsonify(result), 201
    # print(type(result))   
    # return jsonify(result), 201


@events.route("/api/events", methods=["GET"])
def all_event():

    event = query_all(Event)
    if not event:
        return {"msg": "No event found."}, 400
    events = format(event)   
    return jsonify(events), 200
    
    # return jsonify({
    #     'msg': "All Events",
    #     'event': events }), 200
    # return jsonify(events), 200


@events.route("/api/events/<id>", methods=["GET"])
def event(id):

    event = query_one_filtered(Event).first()
    if event is None:
        return ({"msg": "Event not found"}), 404
    result =  event.format()
    return jsonify(result), 201

    # return json.dumps(result, default=default)
    # return jsonify({
    #     'msg': "Event Details",
    #     'event': result }), 200   


@events.route("/api/events/<int:id>", methods=["PUT"])
def update_event(id):

    event = query_one_filtered(Event)
    if not event:
        return ({"msg": "Event not found"}), 404













