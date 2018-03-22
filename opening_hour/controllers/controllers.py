# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import datetime

class OpeningHour(http.Controller):
    @http.route('/opening_hour/opening_hour/', type='json', auth='user')
    def index(self, **kw):
        event = 'Bussiness is open'
        calendar = request.env['calendar.event']
        days = ['mon','tue','wed','thu','fri','sat','sun']
        today = days[datetime.datetime.today().weekday()]
        opening_hour = request.env['opening_hour.opening_hour']
        oh_reg = opening_hour.search([('day','=',str(today))])
        oh_special = opening_hour.search([('day','=',datetime.date.today())])
        check_bio = calendar.search([('name','=',event)])
        bussines_time = {
            'opening':0,
            'closing':0
        }
        if not check_bio:
            if oh_special:
                bussines_time = {
                    'opening':oh_special.opening_hour,
                    'closing':oh_special.closing_hour
                }
            else:
                if oh_reg:
                    bussines_time = {
                        'opening':oh_reg.opening_hour,
                        'closing':oh_reg.closing_hour
                    }
            if bussines_time['opening']>0:
                print self.create_time(bussines_time['opening'])
                print self.create_time(bussines_time['closing'])
                opening = calendar.create({
                    'name':event,
                    'start':self.create_time(bussines_time['opening']),
                    'stop':self.create_time(bussines_time['closing'])
                })

        return {"status":"ok"}


    def create_time(self, hour):
        now = datetime.datetime.now()
        curdate = now.strftime("%Y-%m-%d")
        tm = int(hour)-7
        if tm<10:
            tm = '0'+str(tm)
        mnt = int((hour % 1)*60)
        if mnt>59:
            mnt = 59
        if mnt < 10:
            mnt = '0'+str(mnt)
        return '%s %s:%s:00' % (curdate,tm,mnt)
        


#     @http.route('/opening_hour/opening_hour/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opening_hour.listing', {
#             'root': '/opening_hour/opening_hour',
#             'objects': http.request.env['opening_hour.opening_hour'].search([]),
#         })

#     @http.route('/opening_hour/opening_hour/objects/<model("opening_hour.opening_hour"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opening_hour.object', {
#             'object': obj
#         })