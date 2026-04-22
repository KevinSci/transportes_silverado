from django.core.exceptions import ValidationError
from home.models import Asset
from django.db.models import Q

def create_asset_controller(data):
    asset_type = data.get('asset_type')
    number = data.get('number')

    if Asset.objects.filter(number=number).exists():
        raise ValidationError("El número de activo ya existe.")

    asset_params = {
        'asset_type': asset_type,
        'number': number,
        'observations': data.get('observations'),
    }

    if asset_type == 'tracto':
        asset_params.update({
            'brand': data.get('brand'),
            'model_name': data.get('model_name'),
            'transmission': data.get('transmission'),
            'operator': data.get('operator'),
            'operator_number': data.get('operator_number'),
            'engine': data.get('engine'),
        })
    else:
        asset_params.update({
            'plates': data.get('plates'),
            'dimensions': data.get('dimensions'),
            'state': data.get('state'),
            'condition': data.get('condition'),
        })

    return Asset.objects.create(**asset_params)

def show_assets_controller(data):
    pass
