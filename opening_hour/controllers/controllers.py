# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import datetime,pytz
import json

class OpeningHour(http.Controller):
    @http.route('/opening_hour/opening_hour/', type='http', auth='public')
    def get_opening_hours(self, **kw):
        event = request.env['calendar.event']
        b_hours = event.search([
        ('bussiness_time_event','=',True),
        ('start','>',self.utc_time(datetime.datetime.now().strftime("%Y-%m-%d 00:00:01"))),
        ('start','<',self.utc_time(datetime.datetime.now().strftime("%Y-%m-%d 23:59:59")))
        ])
        for b_hour in b_hours:
            print b_hour.start
        return {'status':'ok'}

    def utc_time(self,i_dt):
        local = pytz.timezone ("Asia/Jakarta")
        naive = datetime.datetime.strptime (i_dt, "%Y-%m-%d %H:%M:%S")
        local_dt = local.localize(naive, is_dst=None)
        utc_dt = local_dt.astimezone (pytz.utc)
        return utc_dt.strftime("%Y-%m-%d %H:%M:%S")
