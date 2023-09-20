from flask import Blueprint, request, jsonify
from Event.models import Users, Events
from Event.utils import (
    query_one_filtered
)


events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint


@events.route("/", methods=["POST"])
def add_provider():
    return


# Get events based on event id
@events.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event = query_one_filtered(table=Events, id=event_id)
        return jsonify(event.format()), 200
    except Exception as error:
        if not event:
            return jsonify({"error": "Event not found"}), 404
        else:
            return jsonify({
                "error": "An error occured",
                "error_message": error
                }), 404


@events.route("/<id>", methods=["DELETE"])
def delete_event(id):
    try:
        del_event = query_one_filtered(table=Events, id=id)

        if del_event:
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 204
    except Exception as error:
        return jsonify(error={"Not Found": "Event not found"}), 404

