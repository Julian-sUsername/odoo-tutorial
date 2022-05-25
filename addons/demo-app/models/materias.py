from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Materias(models.Model):
    _name = 'materias'
    _description = 'materias description'

    # Fields
    code = fields.Char()
    name = fields.Char()
    credits = fields.Integer()
    note1 = fields.Float()
    note2 = fields.Float()
    note3 = fields.Float()
    media = fields.Float(store=True)
    product = fields.Float(store=True, compute="_compute_product", invisible=True)
    sum_product = fields.Float(compute="_compute_sum_product")
    

    @api.onchange("note3", "note1", "note2")
    def _onchange_notes(self):
        if self.note1 > 0 and self.note2 > 0 and self.note3 > 0:
            self.media = (
                (self.note1+self.note2+self.note3)/3.0)

    @api.constrains("note3", "note1", "note2")
    def _check_notes(self):
        for note in self:
            if (self.note1 < 0 or self.note2 < 0 or self.note3 < 0):
                raise ValidationError(
                    "el valor de las notas debe ser mayor a 0"
                )

    @api.depends("credits", "media")
    def _compute_product(self):
        for record in self:
            record.product = record.credits * record.media

    

    @api.depends("product")
    def _compute_sum_product(self):
        products = []
        for record in self:
            products.append(record.product)
            record.sum_product = sum(products)
         