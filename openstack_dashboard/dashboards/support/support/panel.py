from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.support import dashboard


class Support(horizon.Panel):
    name = _("Support")
    slug = "support"


dashboard.Support.register(Support)
