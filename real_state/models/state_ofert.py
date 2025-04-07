from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StateOfert(models.Model):
    _name = 'state_ofert'
    _description = 'Oferts model for Propertys'
    _order = 'sequence'

    property_id = fields.Many2one('state_property', string="Propiedad")
    id_oferta = fields.Integer(string='Identicador de la oferta')
    nombre_ofertante = fields.Char(string='Nombre Ofertante', required=True)
    valor_oferta = fields.Float(string='Valor oferta', required=True)
    fecha_oferta = fields.Date(string='Fecha de la Propuesta', required=True)
    
    estado_oferta = fields.Selection(
        string='Estado de la oferta',
        selection=[
            ('pending', 'Pendiente'),
            ('accept', 'Aceptada'),
            ('decline', 'Rechazada')
        ],
        default='pending'
        )
    metodo_pago = fields.Selection([
        ('efectivo', 'Efectivo'),
        ('credito', 'Crédito'),
        ('transferencia', 'Transferencia')
    ], string="Método de pago", required=True)
    contacto_ofertante = fields.Char(string='Telefono de contacto')
    sequence = fields.Integer(string='Sequence', default=10)


    @api.model
    def create(self, vals):
        propiedad = self.env['state_property'].browse(vals.get('property_id'))
        if propiedad.estado_disp == 'sold':
            raise ValidationError('No se puede hacer una oferta a una propiedad ya vendida. ')
        elif propiedad.estado_disp == 'available_rent':
            raise ValidationError('Esta propiedad esta disponible para la renta, No para la venta')
        return super(StateOfert, self).create(vals)     