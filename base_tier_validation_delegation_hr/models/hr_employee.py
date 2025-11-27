# Copyright 2025 360ERP (<https://www.360erp.com>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    tier_on_holiday = fields.Boolean(
        string="On Holiday (Tier Validation)",
        related="user_id.on_holiday",
        readonly=False,
        help="If checked, tier validations will be delegated to the replacer.",
    )

    tier_holiday_start_date = fields.Date(
        string="Holiday Start Date",
        related="user_id.holiday_start_date",
        readonly=False,
    )

    tier_holiday_end_date = fields.Date(
        string="Holiday End Date", related="user_id.holiday_end_date", readonly=False
    )

    tier_validation_replacer_id = fields.Many2one(
        comodel_name="res.users",
        string="Tier Validation Replacer",
        related="user_id.validation_replacer_id",
        readonly=False,
        help="The user who will receive validation requests while this employee is on holiday.",
    )
