from odoo import models, fields


class Department(models.Model):
    _name = "mylab.department"
    name = fields.Char()
    num_of_machines = fields.Integer()
    machine_ids = fields.One2many('mylab.machine','department_id' , string="Machines")
