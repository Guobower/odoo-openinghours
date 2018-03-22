# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class OpeningHour(models.Model):
    _name = 'opening_hour.opening_hour'

    name = fields.Char()
    day = fields.Selection([ ('date', 'Date Selection'),
    ('sun', 'Sunday'),
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday')])
    opening_hour = fields.Float(text='Opening Hour')
    closing_hour = fields.Float(text='Closing Hour')
    date = fields.Date(attrs={'invisible'})

    @api.model
    def create(self, values):
        if values['day'] != 'date':
            oh = self.env['opening_hour.opening_hour'].search([('day','=',values['day'])])
            if oh:
                raise exceptions.ValidationError(_("Rule already exist!"))
        return super(OpeningHour, self).create(values)
        
    # @api.onchange('day')
    # def onchange_day(self):
    #     if not self.name:
    #         self.name = self.day


