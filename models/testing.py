from odoo import api, fields, models


class TestingData(models.Model):
    _name = 'hz.testing.data'
    _description = "Hz Testing Data"

    name = fields.Char(required=True, default="i am default")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default="male")


class TestingData2(models.Model):
    _inherit = 'hz.testing.data'

    # TODO : if not female will be append selection
    gender = fields.Selection(selection_add=[
        ('other', 'Other'),
        ('female', )
    ], default="other")


class Testing(models.Model):
    _name = 'hz.testing'
    _description = 'Testing'

    name = fields.Char()

    # TODO : record will be delete
    data_id = fields.Many2one('hz.testing.data')
    cascade_data_id = fields.Many2one('hz.testing.data', ondelete="CASCADE")

    # TODO : record can't delete
    restrict_data_id = fields.Many2one('hz.testing.data', ondelete="RESTRICT")

    # TODO : relationship id will be delete that id will be null and still remain record
    set_null_data_id = fields.Many2one('hz.testing.data', ondelete="set null")
