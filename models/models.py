# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class practice_mod(models.Model):
#     _name = 'practice_mod.practice_mod'
#     _description = 'practice_mod.practice_mod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class parking(models.Model):
    _name = "practice_mod.parking"
    _description = "Allows to define parking caracteristics"

    #default search descriptive field
    name = fields.Char(string = 'Direction')
    spots = fields.Integer()
    car_ids = fields.One2Many()