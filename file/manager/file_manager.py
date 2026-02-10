from base.services import ServiceBase
from ..models import File

class FileManager(ServiceBase):
    manager = File.objects