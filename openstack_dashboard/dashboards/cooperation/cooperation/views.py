import logging
from django.utils.translation import ugettext_lazy as _
from horizon import tables
from openstack_dashboard.dashboards.cooperation.cooperation import tables as project_tables
from horizon import views

LOG = logging.getLogger(__name__)

class Cooperation:
    def __init__(self,id,username,email,roles,restate,time):
        self.id = id
        self.username = username
        self.email = email
        self.roles = roles
        self.restate = restate
        self.time = time

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class =  project_tables.CooperationTable
    template_name = 'cooperation/cooperation/index.html'

    def get_data(self):
        resource=[Cooperation(1,"admin","admin@admin.com","admin","res","2015-10-11")]
        return resource
