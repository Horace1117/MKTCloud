import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)

class NoticeTable(tables.DataTable):
    id = tables.Column("id",verbose_name=_("ID"))
    name = tables.Column("name",verbose_name=_("Name"))
    description = tables.Column("description",verbose_name=_("Description"))
    totalinvite = tables.Column("totalinvite",verbose_name=_("TotalInvite"))
    time = tables.Column("time",verbose_name=_("Time"))
  
    class Meta:
      name = "notice"
      verbose_name = _("Notice")    