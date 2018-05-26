from odoo import models, fields, api


class MyLabDepartment(models.Model):
    _name = "mylab.department"
    name = fields.Char()
    machines_ids = fields.One2many('mylab.machine', 'department_id', string="Machines")

    # This is an other way and better than the handle in machine models
    @api.multi
    def _calc_machines(self):
        for record in self:
            record.num_of_machines = len(record.machines_ids)

    num_of_machines = fields.Integer(compute=_calc_machines)
