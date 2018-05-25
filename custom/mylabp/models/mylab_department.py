from odoo import models, fields


class MyLabDepartment(models.Model):
    _name = "mylab.department"
    name = fields.Char()
    num_of_machines = fields.Integer()
    machines_ids = fields.One2many('mylab.machine','department_id' , string="Machines")
