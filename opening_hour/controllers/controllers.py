# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import datetime,pytz,time
import json
from dateutil import tz
class OpeningHour(http.Controller):
    @http.route('/opening_hour/opening_hour/', type='http', auth='public')
    def get_opening_hours(self, **kw):
        event = request.env['calendar.event']
        b_hours = event.search([
        ('bussiness_time_event','=',True),
        ('start','>',self.utc_time(datetime.datetime.now().strftime("%Y-%m-%d 00:00:01")).strftime("%Y-%m-%d %H:%M:%S")),
        ('start','<',self.utc_time(datetime.datetime.now().strftime("%Y-%m-%d 23:59:59")).strftime("%Y-%m-%d %H:%M:%S"))
        ])
        o = []
        to_zone = tz.tzlocal()
        user_tz = request.env.user.tz or pytz.utc
        for b_hour in b_hours:
            o.append({
            'from':self.local_time(b_hour.start).strftime("%H:%M:%S"),
            'to':self.local_time(b_hour.stop).strftime("%H:%M:%S")
            })
        return json.dumps(o)

    def utc_time(self,i_dt):
        local = pytz.timezone("Asia/Jakarta")
        naive = datetime.datetime.strptime(i_dt, "%Y-%m-%d %H:%M:%S")
        return local.localize(naive, is_dst=None).astimezone(pytz.utc)

    def local_time(self,i_dt):
        local = pytz.timezone ("Asia/Jakarta")
        naive = datetime.datetime.strptime (i_dt, "%Y-%m-%d %H:%M:%S")
        return pytz.utc.localize(naive, is_dst=None).astimezone(local)
