# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.tools.translate import _
from odoo.exceptions import ValidationError

class ESRestCompany(models.Model):
    _inherit = 'res.company'

    msj_facturas = fields.Text(help="Mensaje General")
    tipo_imp = fields.Selection([("papel", "Papel"), ("pantalla", "Pantalla")], string="Modalidad de Impresion", 
        help=" * 'Papel' mandara el documento a la impresora especificada en el parametro de sistema: impresora.\n"
             " * 'Pantalla' muestra el documento en pantalla como un archivo PDF.\n", required=True, default='pantalla')