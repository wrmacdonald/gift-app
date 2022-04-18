import logging
import os
from flask import Flask
from flask_restful import Api
from database.database import init_db, drop_db
from resources.user import UserResource
from resources.item import ItemResource
from resources.group import GroupResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/api/users')
api.add_resource(ItemResource, '/api/items')
api.add_resource(GroupResource, '/api/groups')
# api.add_resource(ListResource, '/api/lists')
# api.add_resource(GroupMembersResource, 'api/group/<group_id:int>/members')
# api.add_resource(InviteMemberResource, '/api/groups/<group_id:int>/InviteMembers')
# api.add_resource(ListItemResource, '/api/lists/<list_id:int>/items')
# ActivateResource
# AuthenticateResource


def main():
    drop_db()
    init_db()

    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())







