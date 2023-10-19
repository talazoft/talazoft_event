from odoo import models, fields


class EventTicket(models.Model):

    _inherit = "event.event.ticket"
    _order = "sequence"

    sequence = fields.Integer(string="Sequence", default=1)
