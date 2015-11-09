import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard import api

class AlarmTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    description = tables.Column("description", verbose_name=_("Description"))

    def sanitize_id(self, obj_id):
        return get_int_or_uuid(obj_id)
    
    class Meta:
        name = "alarm"
        verbose_name = _("Alarm")
       