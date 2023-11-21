from odoo import models, fields, api

class BranchOffice(models.Model):
    _name = 'data.branchoffice'
    _description= 'Data kantor cabang Bank BCA'

    name = fields.Char(string="Nama kantor cabang", required=True)
    code = fields.Char(string="Kode cabang", required=True)
    address = fields.Char(string="Alamat", required=True)
    city = fields.Selection(selection=[
        ('0', 'Jember'),
        ('1', 'Malang'),
        ('2', 'Mojokerto'),
        ('3', 'Probolinggo'),
        ('4', 'Surabaya')
    ], required=True)
    province = fields.Selection(selection=[
        ('0', 'Jawa Timur')
    ], required=True)
    country = fields.Selection(selection=[
        ('0', 'Indonesia')
    ], required=True)
    postal_zip = fields.Integer(string="Kode pos", required=True)