from odoo import models, fields, api

class Account(models.Model):
    _name = 'data.account'
    _description= 'Data rekening nasabah'

    account_number = fields.Char(string="Nomor rekening", required=True)
    type = fields.Selection(selection=[
        ('0', 'Tahapan BCA'),
        ('1', 'Tahapan Xpresi'),
        ('2', 'Tahapan Gold'),
        ('3', 'Tahapan Berjangka'),
        ('4', 'Tahapan Berjangka SiMuda'),
        ('5', 'Simpanan Pelajar'),
        ('6', 'Tapres BCA'),
        ('7', 'TabunganKu'),
        ('8', 'LAKU'),
        ('9', 'BCA Dollar')
    ], required=True)
    balance = fields.Float(string="Saldo", required=True)
    account_holder = fields.Many2one('data.customerpersonal', string="Pemegang rekening")