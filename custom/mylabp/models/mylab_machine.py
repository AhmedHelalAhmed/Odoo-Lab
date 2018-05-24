from odoo import models, fields


class MyLabMachine(models.Model):
    _name = "mylab.machine"
    name = fields.Char()
    description = fields.Text()
    price = fields.Float()
    image = fields.Binary()
    is_accepted = fields.Boolean(string="Is Accepted")
    department_id = fields.Many2one('mylab.department', string="Department")
    user_id = fields.Many2one('res.users', string='Approved By',readonly=True,  default=lambda self: self.env.uid)
    histories_ids = fields.One2many('mylab.history','machine_id', string='History')

