from odoo import models, fields, api

class Asset(models.Model):
    _name = 'data.asset'
    _description= 'Data rekening nasabah'

    asset_name = fields.Char(string="Nama aset", required=True)
    type = fields.Selection(selection=[
        ('0', 'Properti'),
        ('1', 'Investasi'),
        ('2', 'Portofolio investasi'),
        ('3', 'Koleksi'),
        ('4', 'Aset tetap'),
        ('5', 'Aset keuangan'),
        ('6', 'Aset lainnya'),
    ], required=True)
    asset_value = fields.Float(string="Nilai aset", required=True)
    date_acquired = fields.Date(string="Tanggal perolehan", required=True)
    