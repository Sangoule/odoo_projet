from odoo import models, fields, api

class inherited(models.Model):
     _inherited='res.partner'
     ismember = fields.Boolean('est membre')