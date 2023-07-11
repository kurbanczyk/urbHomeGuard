from flask import Blueprint

from guard_coach_service.activities.folksActivities import FolksActivities

api: Blueprint = Blueprint('coach', __name__, url_prefix = '/coach')

activities = FolksActivities()
api.route('/folks', methods=['GET'])(activities.get_folks)
api.route('/folks', methods=['POST'])(activities.create_folks)