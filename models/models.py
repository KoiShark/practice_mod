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
    name = fields.Char(string='Address', required=True)
    spots = fields.Integer(string='Spots', required=True)

    #table relations
    car_id = fields.One2many(
        comodel_name='practice_mod.car',
        inverse_name='parking_id', string='Cars list')

    #table relations
    car_id = fields.One2many(
        comodel_name='practice_mod.car',
        inverse_name='parking_id', string='Cars list')

class Car(models.Model):
    _name = "practice_mod.car"
    _description = "Allows to define the car's caracteristics"

    name = fields.Char(
        string='Plate', size=7, required=True)
    model_car = fields.Char(string='Model', required=True)
    built_date = fields.Date(string='Construction Date')
    consumption_gas = fields.Float(
        string='Gas Consumption',
        digits=(4, 1), default=0.0,
        help='Media of consumption 100km')
    damaged = fields.Boolean(string='Damaged', default=False)
    #store=True is not convenient in this case
    years = fields.Integer(string = 'Years', compute = '_get_years')
    description = fields.Text(string = 'Description')

    #inverse_name to parking with relational field Many2one
    parking_id = fields.Many2one(
        comodel_name='practice_mod.parking',
        string='Parking_id',
        required=True)

    #relation Many2many with maintenance
    maintenance_ids = fields.Many2many(
        comodel_name='practice_mod.maintenance', string='Maintenance_ids')

    @api.depends('built_date')
    def _get_years(self):
        #TO-DO: pending on
        for car in self:
            car.years = 0

class Maintenance(models.Model):
    _name = 'practice_mod.maintenance'
    _description = 'Allows to define maintenance routine'
    _order = 'maintenance_date'

    #name = fields.Char()
    maintenance_date = fields.Date(string='Date', required=True, default=fields.date.today())
    maintenance_type = fields.Selection(
        string='Type',
        selection=[('w','wash'),('c','check'),('m','mechanics'),('p','painting')],
        default='w')
    maintenance_price = fields.Float(
        string='Price', digits=(8, 2),
        help='Maintenance total price')

    #backwards relation to maintenance_ids in car
    car_ids = fields.Many2many(comodel_name='practice_mod.car', string='Cars_ids')
