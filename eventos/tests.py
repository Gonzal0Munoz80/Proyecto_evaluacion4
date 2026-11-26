from django.test import TestCase
from decimal import Decimal
from django.contrib.admin.sites import AdminSite
from django.utils.formats import number_format

from .admin import EventosAdmin
from .models import eventos


class EventosAdminTests(TestCase):
    def test_price_is_formatted_as_pesos_in_admin(self):
        event = eventos(valor=Decimal('1234'))
        admin_view = EventosAdmin(eventos, AdminSite())

        self.assertEqual(
            admin_view.valor_en_pesos(event),
            f"$ {number_format(Decimal('1234'), use_l10n=True, force_grouping=True)}",
        )
