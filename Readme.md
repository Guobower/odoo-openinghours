#Odoo Opening hour
This module will create a 'bussiness is open' event based on rule that we set
#### Instalation
- Put opening_hour module into your addons folder that accessible by odoo daemon
or
Just include this path as odoo addon path

 - Restart odoo service
 - This module should appear in apps list, and you can install it
*if the module was not appear in application list, activate developer mode, by typing url [server]/web?debug and back to application menu=> update application list*

#### Setting bussiness hour rule
you can set rule by accessing setting menu -> bussiness hour
add your bussiness hour entry there
#### Accessing via http request
to access today bussiness hour via http request, just point to [server]/opening_hour/opening_hour/
