from base.services import ServiceBase
from ..serializer import FileSerializer
from ..models import File

class FileServices(ServiceBase):
    manager = File.objects

    @staticmethod
    def UploadFile (data):
        serializer =  FileSerializer(data = data)
        if serializer.is_valid():
            fileToUpload = ServiceBase.create(**serializer)
            fileToUpload.save()
            return {"success":True, "fileToUpload":fileToUpload, "error":None}
        
        return {"success": False, "fileToUpload":False, "error":serializer.errors}
    
    @staticmethod
    def deleteFile(file_id):
        try:  
             
            file = ServiceBase.delete(pk= file_id)
            serialized = FileSerializer(file).data
            return{'success':False, 'deleted_task':serialized,'error':{'details':'Task does not exist'}}
        except File.DoesNotExist:
        
            return {
                "success": False,
                "deleted_task": None,
                "errors": {"detail": "File does not exist"}
            }
        

    @staticmethod
    def getFile(file_id):
        try:  
             
            file = ServiceBase.get(pk= file_id)
            serialized = FileSerializer(file).data
            return{'success':False, 'fetched file':serialized,'error':{'details':'file does not exist'}}
        except File.DoesNotExist:
        
            return {
                "success": False,
                "fetched_file": None,
                "errors": {"detail": "Task does not exist"}
            }
        

    @staticmethod
    def updateFile(file_id,data):
        try:
          file = ServiceBase.get(pk= file_id)
        except File.DoesNotExist:
          return{'success': False, 'getData':None,'error':{'details': 'File not found'} }

        updateData = FileSerializer(file, data = data, partial = True) #partial = True allows partial updates
        
        if updateData.is_valid():

          new_updated = ServiceBase.update(updateData)
          new_updated.save()
        
          return{'success': True, 'new_updated':FileSerializer(new_updated).data, 'error':None}
        return{'success':False, 'savedUpdate':None, 'error':updateData.errors}
