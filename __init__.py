# This file is part carrier_service module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from .carrier import *

def register():
    Pool.register(
        CarrierService,
        Carrier,
        module='carrier_service', type_='model')
