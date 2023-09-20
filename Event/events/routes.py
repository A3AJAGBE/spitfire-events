from flask import Blueprint, request, jsonify
from Event.models import Users, Events
from Event.utils import (
    query_one_filtered,
    query_all
)


events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint



@events.route("/<id>", methods=["DELETE"])
def delete_event(id):
    try:
        del_event = query_one_filtered(table=Events, id=id)

        if del_event:
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 204
    except Exception as error:
        return jsonify(error={"Not Found": "Event not found"}), 404

#Get all events
@events.route("/", methods=["GET"])
def all_events():
    try:
        all_events = query_all(Events)       
        return jsonify(all_events), 200
    
    except Exception as e:
        if not all_events:
            # No events found
            return jsonify({"message": "No events found"}), 404
        else:
            return jsonify({
                "error": "An error occured",
                "error_message": e
                }), 400
