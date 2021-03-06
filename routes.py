from resources.user import UserResource
from resources.item import ItemResource
from resources.group import GroupResource, GroupMembersResource
from resources.auth import Signup, Login
from resources.confirmation import EmailConfirmation
from resources.list import ListResource, ListItemResource
from resources.invitation import InviteMemberResource


def initialize_routes(api):
     api.add_resource(Signup, '/api/auth/signup')
     api.add_resource(Login, '/api/auth/login')
     api.add_resource(UserResource, '/api/users')
     api.add_resource(ItemResource, '/api/items')
     api.add_resource(GroupResource, '/api/groups')
     api.add_resource(GroupMembersResource, '/api/groups/<int:group_id>/members')
     api.add_resource(EmailConfirmation, '/api/confirm-email/<string:token>')
     api.add_resource(ListResource, '/api/lists')
     api.add_resource(ListItemResource, '/api/lists/<int:list_id>/items')
     api.add_resource(InviteMemberResource, '/api/groups/<int:group_id>/invite')
