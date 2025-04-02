from odoo import models, fields  # type: ignore


class EmployeeCustom(models.Model):
    _name = 'hr.employee.custom'
    _description = 'Empleados Personalizados'

    name = fields.Char(string='Nombre', required=True)
    job_position = fields.Char(string='Cargo')
    department = fields.Char(string='Departamento')
    photo = fields.Image(string='Foto de Perfil')
    salary = fields.Float(string='Salario')
    hire_date = fields.Date(string='Fecha de Contratación')
    active = fields.Boolean(string='Activo', default=True)
