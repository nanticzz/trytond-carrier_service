# This file is part carrier_service module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['CarrierService', 'Carrier']


class CarrierService(ModelSQL, ModelView):
    'CarrierService'
    __name__ = 'carrier.service'
    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code', required=True)
    carrier = fields.Many2One('carrier', 'Carrier', required=True)
    default = fields.Boolean('Default', help='Default service carrier')


class Carrier:
    __metaclass__ = PoolMeta
    __name__ = 'carrier'
    services = fields.One2Many('carrier.service', 'carrier', 'Services')
