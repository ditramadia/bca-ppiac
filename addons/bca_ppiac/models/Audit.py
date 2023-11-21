from odoo import models, fields, api

class Aduit(models.Model):
    _name = 'data.audit'
    _description= 'Data Audit internal dan eksternal kantor cabang'

    title = fields.Char(string="Judul audit", required=True)
    type = fields.Selection(selection=[
        ('0', 'Internal'),
        ('1', 'Eksternal')
    ])
    date = fields.Date(string="Tanggal", required=True)
    report_url = fields.Char(string="URL laporan", required=True)
    submitted_by = fields.Many2one('data.branchoffice', string="Kantor cabang", required=True)