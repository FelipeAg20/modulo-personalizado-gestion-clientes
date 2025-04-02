{
    'name': 'Gestión de Empleados Personalizada',
    'version': '1.0',
    'author': 'Andres Felipe Agiuilar Ruiz',
    'summary': 'Gestión de empleados con fotos de perfil',
    'description': 'Un módulo para administrar empleados con la opción de cambiar la foto de perfil.',
    'category': 'Human Resources',
    'depends': ['base'],  # Dependencias mínimas
    'data': [
        'security/ir.model.access.csv',  # Permisos de acceso
        'views/hr_employee_custom_views.xml',  # Vistas personalizadas
    ],
    'installable': True,
    'application': True,
}
