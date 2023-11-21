from odoo import models, fields, api

class Correspondence(models.Model):
    _name = 'data.correspondence'
    _description= 'Data korespondensi kantor cabang'

    title = fields.Char(string="Judul dokumen", required=True)
    url = fields.Char(string="URL", required=True)
    date = fields.Date(string="Tanggal rilis", required=True)
    submitted_by = fields.Many2one('data.branchoffice', string="Kantor cabang", required=True)