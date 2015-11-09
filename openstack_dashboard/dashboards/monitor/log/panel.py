from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.monitor import dashboard


class Log(horizon.Panel):
    name = _("Log")
    slug = "log"


dashboard.Monitor.register(Log)
