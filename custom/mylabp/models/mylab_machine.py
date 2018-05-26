from odoo import models, fields, api


class MyLabMachine(models.Model):
    _name = "mylab.machine"
    name = fields.Char()
    description = fields.Text()
    price = fields.Float()
    image = fields.Binary()
    is_accepted = fields.Boolean(string="Is Accepted")
    department_id = fields.Many2one('mylab.department', string="Department")
    user_id = fields.Many2one('res.users', string='Approved By', default=lambda self: self.env.uid)
    histories_ids = fields.One2many('mylab.history', 'machine_id', string='History')
    tags_ids = fields.Many2many('mylab.tag', string="tags")
    state = fields.Selection([
        ('draft', "Draft"),
        ('approve', "Approved"),
        ('refuse', "Refused"),
    ])

    @api.multi
    def draft(self):
        for record in self:
            record.state = "draft"

    @api.multi
    def approve(self):
        for record in self:
            record.state = "approve"

    @api.multi
    def refuse(self):
        for record in self:
            record.state = "refuse"

    # For increase the number of machine in department model if created
    @api.model
    def create(self, vals):
        new_machine_object = super(MyLabMachine, self).create(vals)
        # To make the number of machine in department models dynamic
        new_machine_object.department_id.num_of_machines = new_machine_object.department_id.num_of_machines + 1
        return new_machine_object

    # For decrease the number of machine in department model if deleted
    @api.multi
    def unlink(self):
        for record in self:
            record.department_id.num_of_machines = record.department_id.num_of_machines - 1
        super(MyLabMachine, self).unlink()

    # For edit if the machine's department change
    @api.multi
    def write(self, vals):
        flag_change_department=False
        for record in self:
            #if the department modified
            if record.department_id != vals.get('department_id'):
                flag_change_department=True
                #decrease the old department
                record.department_id.num_of_machines = record.department_id.num_of_machines - 1
        super(MyLabMachine, self).write(vals)
        # the condition do not matter !!! without the codition the increase works will and not increase again
        # increase the new department
        if flag_change_department:
            for record in self:
                record.department_id.num_of_machines = record.department_id.num_of_machines + 1




