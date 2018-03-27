# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import datetime,pytz

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

    @api.model
    def create(self, values):
        if values['day'] != 'date':
            bussiness_times = self.env['opening_hour.opening_hour'].search([('day','=',values['day'])])
            for bussiness_time in bussiness_times:
                if bussiness_time.closing_hour > values['opening_hour']:
                    raise exceptions.ValidationError(_("Opening hour must be bigger than closing hour"))

        return super(OpeningHour, self).create(values)

    @api.multi
    def set_opening_hour(self):
        event = 'Bussiness is open'
        calendar = self.env['calendar.event']
        days = ['mon','tue','wed','thu','fri','sat','sun']
        today = days[datetime.datetime.today().weekday()]
        opening_hour = self.env['opening_hour.opening_hour']
        bt_regs = opening_hour.search([('day','=',str(today))])
        curdate = datetime.datetime.now().strftime("%Y-%m-%d")
        check_bio = calendar.search([('name','=',event)])
        for bussiness_time in bt_regs:
            event_exist = calendar.search([('name','=',event),
            ('bussiness_time_event','=',True),
            ('start','=',self.create_time(bussiness_time.opening_hour)),
            ('stop','=',self.create_time(bussiness_time.closing_hour))])
            if not event_exist:
                new_event = calendar.create({
                    'name':event,
                    'bussiness_time_event':True,
                    'start':self.create_time(bussiness_time.opening_hour),
                    'stop':self.create_time(bussiness_time.closing_hour)
                })
        return {"status":"ok"}

    def create_time(self, hour):
        now = datetime.datetime.now()
        curdate = now.strftime("%Y-%m-%d")
        tm = int(hour)
        if tm<10:
            tm = '0'+str(tm)
        mnt = int((hour % 1)*60)
        if mnt>59:
            mnt = 59
        if mnt < 10:
            mnt = '0'+str(mnt)
        local = pytz.timezone ("Asia/Jakarta")
        o_dt = '%s %s:%s:00' % (curdate,tm,mnt)
        naive = datetime.datetime.strptime (o_dt, "%Y-%m-%d %H:%M:%S")
        local_dt = local.localize(naive, is_dst=None)
        utc_dt = local_dt.astimezone (pytz.utc)
        return utc_dt.strftime("%Y-%m-%d %H:%M:%S")

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    bussiness_time_event = fields.Boolean('Bussiness Time Event')
