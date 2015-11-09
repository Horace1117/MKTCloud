from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import horizon

from openstack_dashboard.dashboards.admin import dashboard


class LoadBalancer(horizon.Panel):
    name = _("Load Balancers")
    slug = "loadbalancers"
    permissions = ('openstack.services.network',)


if getattr(settings, 'OPENSTACK_QUANTUM_NETWORK', {}).get('enable_lb', False):
    dashboard.Admin.register(LoadBalancer)
