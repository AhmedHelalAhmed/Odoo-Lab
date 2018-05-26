from odoo import models, fields


class MyLabTag(models.Model):
    _name = "mylab.tag"
    name = fields.Char()


