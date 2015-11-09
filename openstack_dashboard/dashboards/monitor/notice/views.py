import logging
from django.utils.translation import ugettext_lazy as _
from horizon import tables
from openstack_dashboard.dashboards.monitor.notice import tables as project_tables
from horizon import views


class Notice:
    def __init__(self,id,name,description,totalinvite,time):
        self.id = id
        self.name = name
        self.description = description
        self.totalinvite = totalinvite
        self.time = time


class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class =  project_tables.NoticeTable
    template_name = 'monitor/notice/index.html'
    
    def get_data(self):
         resource=[]
         return resource
