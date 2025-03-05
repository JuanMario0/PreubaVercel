from django_supabase_ventas.settings import supabase

class VentaManager:
    @staticmethod
    def get_all_ventas():
        response = supabase.table('ventas').select('*').execute()
        return response.data

    @staticmethod
    def create_venta(mes, venta):
        response = supabase.table('ventas').insert({
            'mes': mes,
            'venta': venta
        }).execute()
        return response.data