from odoo import api, fields, models
from odoo.exceptions import ValidationError

# Modelo de agentes
class state_agent(models.Model):
    _name = 'state_agent'
    _description = 'Modelo de agentes inmobiliarios'

    name = fields.Char(string='Nombre del agente', required=True)
    document = fields.Integer(string='Documento', required=True)
    user = fields.Char(string='Usuario de empleado')
    password = fields.Char(string='Contrasena de usuario')
    
    manager_id = fields.Many2one("state_manager", string="Manager asignado")

    @api.model
    def create(self, vals):
        is_manager = self.env.user.has_group('real_state.state_group_manager')
        if not is_manager:
            if 'user' in vals or 'password' in vals:
                raise ValidationError('Solo los managers pueden cambiar las contrasenas')
        return super(state_agent, self).create(vals)


    @api.model
    def write(self, vals):
        is_manager = self.env.user.has_group('real_state.state_group_manager')
        if not is_manager:
            if 'user' in vals or 'password' in vals:
                raise ValidationError('Solo los managers pueden cambiar las contrasenas')
        return super(state_agent, self).write(vals)