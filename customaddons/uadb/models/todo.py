from odoo import models, fields, api


class uadb(models.Model):
     _name = 'to.do'
    

     name = fields.Char(string="Titre")
     desc= fields.Text(string="Description")
     #is_done = fields.Boolean(compute="_value_pc", store=True)
     is_done=fields.Boolean("est_fait")
     member = fields.Many2many('res.partner','membre')