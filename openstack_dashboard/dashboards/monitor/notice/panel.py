from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.monitor import dashboard


class Notice(horizon.Panel):
    name = _("Notice")
    slug = "notice"


dashboard.Monitor.register(Notice)
