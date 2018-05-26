from odoo import models, fields


class MyLabHistory(models.Model):
    _name = "mylab.history"
    user_id = fields.Many2one('res.users', string='By', default=lambda self: self.env.uid)
    machine_id = fields.Many2one('mylab.machine', string='Machine')
    date = fields.Date(string='Date', default=fields.Date.today())
    description = fields.Text()