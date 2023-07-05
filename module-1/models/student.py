# -*- coding: utf-8 -*-

from odoo import fields, models


class Student(models.Model):
    _name = 'student'
    _description = 'student'

    name = fields.Char(required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male')
    height = fields.Float()
    image = fields.Image(attachment=True)
