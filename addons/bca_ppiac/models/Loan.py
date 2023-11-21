from odoo import models, fields, api

class Loan(models.Model):
    _name = 'data.loan'
    _description= 'Data pinjaman nasabah'

    account_number = fields.Char(string="Nomor rekening", required=True)
    type = fields.Selection(selection=[
        ('0', 'Pinjaman pribadi'),
        ('1', 'Hipotek'),
        ('2', 'Kredit kendaraan'),
        ('3', 'Kredit investasi'),
    ], required=True)
    total_loan = fields.Float(string="Pinjaman", required=True)
    interest = fields.Float(string="Bunga", required=True)
    span = fields.Integer(string="Jangka waktu", required=True)
    loan_date = fields.Date(string="Tanggal pinjaman", required=True)
    