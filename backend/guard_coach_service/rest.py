from flask import Blueprint

from guard_coach_service.activities.coachActivities import CoachActivities
from guard_coach_service.activities.folksActivities import FolksActivities

api: Blueprint = Blueprint('coach', __name__, url_prefix = '/coach')

folks_activities: FolksActivities = FolksActivities()
api.route('/folks', methods=['GET'])(folks_activities.get_folks)
api.route('/folks/<folk_name>', methods=['GET'])(folks_activities.get_folk_photos)
api.route('/folks/<folk_name>', methods=['POST'])(folks_activities.create_folks)

coach_activities: CoachActivities = CoachActivities()
api.route('/train', methods=['GET'])(coach_activities.train) # TODO: change to POST