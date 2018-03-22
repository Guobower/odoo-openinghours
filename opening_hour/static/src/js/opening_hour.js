odoo.define('stock_lot_barcode.barcode_incoming_outgoing', function (require) {
    "use strict";
    
    var core = require('web.core');
    var Session = require('web.session');
    
    var _t = core._t;
    $(document).ready(function(){
        Session.rpc('/opening_hour/opening_hour').then(function(result) {
            //todo: get result to call action
            console.log(result)
        });
    })
})    