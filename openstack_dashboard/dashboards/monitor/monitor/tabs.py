from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import messages
from horizon import tabs

from openstack_dashboard.api import keystone
from openstack_dashboard.api import network
from openstack_dashboard.api import nova

from .alarm.tables import AlarmTable
from .combination_alarm.tables import CombinationAlarmTable
from .monitor_indicators.tables import MonitorIndicatorsTable

class MonitorIndicatorsTab(tabs.TableTab):
    table_classes = (MonitorIndicatorsTable,)
    name = _("Monitor Indicators")
    slug = "monitor_indicators_tab"
    template_name = "horizon/common/_detail_table.html"
    
    def get_monitorin_dicators_data(self):
       monitor_indicators=[]
       return monitor_indicators 
    
class AlarmTab(tabs.TableTab):
    table_classes = (AlarmTable,)
    name = _("Alarm")
    slug = "alarm_tab"
    template_name = "horizon/common/_detail_table.html"
    def get_alarm_data(self):
      alarm=[]
      return alarm 

class CombinationAlarmTab(tabs.TableTab):
    table_classes = (CombinationAlarmTable,)
    name = _("Combination Alarm")
    slug = "combination_alarm_tab"
    template_name = "horizon/common/_detail_table.html"
    def get_combination_alarm_data(self):
       combination_alarm=[]
       return combination_alarm 
    



class MonitorTabs(tabs.TabGroup):
    slug = "monitor_tabs"
    tabs = (MonitorIndicatorsTab, AlarmTab, CombinationAlarmTab)
    sticky = True
