from odoo import models, fields

class StateManager(models.Model):
    _name = "state_manager"
    _description = "Managers Real State"
    _order = "sequence"

    name = fields.Char(string="Nombre del Manager", required=True)
    
    property_ids = fields.One2many("state_property", "manager_id", string="Propiedades a cargo")
    agent_ids = fields.One2many("state_agent", inverse_name="manager_id", string='Agentes a cargo')

    fecha_in = fields.Date(string="Fecha de Ingreso", required=True)
    document = fields.Integer(string="Identificación", required=True)
    office = fields.Char(string="Oficina de Vinculación", required=True)
    contact = fields.Char(string="Número de Contacto", required=True)
    usuario_emp = fields.Char(string="Nombre de Usuario", required=True)
    password = fields.Char(string="Contraseña", required=True)
