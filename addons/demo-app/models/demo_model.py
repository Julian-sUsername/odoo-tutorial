from email.policy import default
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import date


class DemoModel(models.Model):
    _name = "demo.model"
    _description = "app description"
    _order = "name asc"
    _sql_constraints = [
        ('document_unique',
         'unique(document)',
         'Choose another value for document, it has to be unique!')
    ]
    

    # Fields
    document = fields.Char()
    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection(selection=[('m', 'male'), ('f', 'female')])
    birthday = fields.Date(default=date.today())
    days_from_legal_age = fields.Integer()
    materias_ids = fields.Many2many("materias")

    

    @api.onchange("birthday")
    def _onchange_birthday(self):
        self.days_from_legal_age = (
            date.today() - ((self.birthday) + relativedelta(years=18))).days
