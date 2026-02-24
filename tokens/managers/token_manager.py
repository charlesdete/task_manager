from base.services import ServiceBase
from models import Token

class TokenManager(ServiceBase):
    manager = Token.objects