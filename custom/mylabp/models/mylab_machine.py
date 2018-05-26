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
