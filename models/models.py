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

class Parking(models.Model):
    _name = "practice_mod.parking"
    _description = "Allows to define parking caracteristics"

    #default search descriptive field
    name = fields.Char(string = 'Direction')
    spots = fields.Integer(string = 'Spots')

class Car(models.Model):
    _name = "practice_mod.car"
    _description = "allows to define the car's caracteristics"

    name = fields.Char(string = 'Plate', size = 7)
    model_car = fields.Char(string = 'Model')
    built_date = fields.Date(string = 'Construction Date')
    consumption_gas = fields.Float(string='Gas Consumption', digits=(4, 1), default=0.0, help='Media of consumption 100km')
    #store=True is not convenient in this case
    years = fields.Integer(string = 'Years', compute = '_get_years')
    description = fields.Text(string = 'Description')

    @api.depends('built_date')
    def _get_years(self):
        for car in self:
            car.years = 0

class Maintenance(models.Model):
    _name = 'practice_mod.maintenance'
    _description = 'Allows to define maintenance routine'
    _order = 'date'

    #name = fields.Char()
    maintenance_date = fields.Date(string = 'Date', default = fields.date.today())
    maintenance_type = fields.Selection(string='Type', selection=[('w','wash'),('c','check'),('m','mechanics'),('p','painting')], default='w')
    maintenance_price = fields.Float(string='Price', digits=(8, 2), help='Maintenace total price')

