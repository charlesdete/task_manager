from base.services import ServiceBase
from ..models import User

class UserService(ServiceBase):
    manager = User.objects