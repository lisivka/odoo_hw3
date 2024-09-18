import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Patient Visit'

    patient_id = fields.Many2one('res.partner', string='Patient',
                                 required=True,
                                 domain="[('is_patient', '=', True)]")
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                required=True)
    disease_id = fields.Many2one('hr_hospital.disease', string='Main Disease')
    disease_ids = fields.Many2many('hr_hospital.disease',
                                   string='Other Diseases')
    date = fields.Datetime(string='Visit Date', default=fields.Datetime.now,
                           required=True)
    notes = fields.Text(string='Notes about Visit')
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done'),
            ('canceled', 'Canceled'),
            ('expired', 'Expired'),
            ('sheduled', 'Scheduled'),
            ('processed', 'Processed'),
        ], default='sheduled')
