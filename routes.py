from resources.user import UserResource
from resources.item import ItemResource
from resources.group import GroupResource, GroupMembersResource
from resources.auth import Signup, Login
from resources.activate import Activate, SendActivation


def initialize_routes(api):
     api.add_resource(Signup, '/api/auth/signup')
     api.add_resource(Login, '/api/auth/login')
     api.add_resource(UserResource, '/api/users')
     api.add_resource(ItemResource, '/api/items')
     api.add_resource(GroupResource, '/api/groups')
     api.add_resource(GroupMembersResource, '/api/groups/<int:group_id>/members')
     api.add_resource(SendActivation, '/api/activate')
     api.add_resource(Activate, '/api/activate/<string:token>')
     # api.add_resource(ListResource, '/api/lists')
     # api.add_resource(InviteMemberResource, '/api/groups/<group_id:int>/InviteMembers')
     # api.add_resource(ListItemResource, '/api/lists/<list_id:int>/items')
     # ActivateResource