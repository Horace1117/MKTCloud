from horizon import tabs
from .tabs import MonitorTabs

class IndexView(tabs.TabbedTableView):
    tab_group_class = MonitorTabs
    template_name = 'monitor/monitor/index.html'