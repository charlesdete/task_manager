from unfold.sites import UnfoldAdminSite

class TaskManagerAdminSite(UnfoldAdminSite):
    site_header = "Task Manager Admin"
    site_title = "Task Manager Admin"
    index_title = "Dashboard"

admin_site = TaskManagerAdminSite(name="admin")
