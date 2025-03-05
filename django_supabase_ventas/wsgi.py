# django_supabase_ventas/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Configurar el módulo de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_supabase_ventas.settings')

# Obtener la aplicación WSGI de Django
application = get_wsgi_application()

# Definir `app` para que Vercel lo reconozca
app = application