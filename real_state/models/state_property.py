from odoo import api, models, fields
from odoo.exceptions import ValidationError

# Modelo de propeidades 
class state_property(models.Model):
    _name = 'state_property'
    _description = 'Propiedades inmobilirias'
    _order = 'sequence'

    name = fields.Char(string="Nombre", required=True)
    ofertas = fields.One2many(
    comodel_name='state_ofert',
    inverse_name='property_id',
    string='Ofertas'
    )
    
    manager_id = fields.Many2one('state_manager', string="Manager asignado")
    
    addres = fields.Char(string="Direccion", required=True)
    description = fields.Text(string="Descripción")
    postal_code = fields.Char(string="Código Postal", required=True)
    date_disponibilidad = fields.Date(string="Fecha de Disponibilidad")
    esperado_precio = fields.Float(string="Precio Esperado", required=True)
    venta_precio = fields.Float(string="Precio de Venta", required=True)
    dormitorios = fields.Integer(string="Dormitorios")
    living = fields.Boolean(string='Sala de estar', default=False)
    living_area = fields.Float(string="Área de Sala", default=False)
    living_area_uom = fields.Many2one('uom.uom', string='Unidad de medida de área', domain="[('category_id.name', '=', 'Surface')]")
    fachadas = fields.Integer(string="Número de Fachadas")
    garaje = fields.Boolean(string="Garaje")
    sequence = fields.Integer(string="Sequence", default=10)
    jardin = fields.Boolean(string="Jardín", default=False)
    jardin_area = fields.Float(string="Area del Jardin")
    jardin_uom_area = fields.Many2one('uom.uom', string="Unidad de medida de área", domain="[('category_id.name', '=', 'Surface')]")
    garden_orientacion = fields.Selection(
        selection=[
            ('norte', 'Norte'),
            ('sur', 'Sur'),
            ('este', 'Este'),
            ('oeste', 'Oeste')
        ], 
        string="Orientación del Jardín"
    )
    estado_disp = fields.Selection(
        string='Disponibilidad', 
        selection=[
            ('available', 'Disponible'),
            ('available_rent', 'Disponible Renta'),
            ('sold', 'Vendida')
        ],
        default='available',
    )



    _sql_constraints = [
        ("check_venta_precio", "CHECK(venta_precio >= 0)", "El precio de venta no puede ser negativo."),
        ("check_esperado_precio", "CHECK(esperado_precio >= 0)", "El precio esperado no puede ser negativo."),
        ("check_jardin_area", "CHECK(jardin_area >= 0)", "El área del jardín no puede ser negativa."),
        ("unique_name", "UNIQUE(name)", "El nombre de la propiedad debe ser único."),
    ]



    @api.constrains('jardin', 'jardin_area')
    def _check_validation_jardin(self):
        for record in self:
            if not record.jardin and record.jardin_area > 0:
                raise ValidationError('No se puede asignar area de jardin si la propiedad no tiene un jardin al que asignarle una propiedad.')
            

    
    @api.constrains('living', 'living_area')
    def _check_validation_living(self):
        for record in self:
            if not record.living and record.living_area > 0:
                raise ValidationError('No se puede asignar area de Sala si la propiedad no tiene una sala a la que asignarle una propiedad.')