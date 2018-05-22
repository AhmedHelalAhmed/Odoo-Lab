from odoo import models, fields

class Machine(models.Model):
    _name="mylab.machine"
    name = fields.Char()
    description = fields.Text()
    price = fields.Float()
 