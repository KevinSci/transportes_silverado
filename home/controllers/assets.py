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

def show_assets_controller(search_query: str = None):
    assets = Asset.objects.all().order_by('-created_at')
    
    if search_query:
        assets = assets.filter(
            Q(number__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(operator__icontains=search_query) |
            Q(plates__icontains=search_query)
        )
    return assets

def delete_asset_controller(asset_id: int):
    try:
        asset_to_delete = Asset.objects.get(id=asset_id)
        asset_to_delete.delete()
        return True
    except Asset.DoesNotExist:
        raise ValidationError("El activo no existe.")

def edit_asset_controller(asset_id: int, data):
    try:
        asset = Asset.objects.get(id=asset_id)
        
        # Validar si el número económico cambió y si el nuevo ya existe
        number = data.get('number')
        if number and number != asset.number:
            if Asset.objects.filter(number=number).exists():
                raise ValidationError("El número de activo ya existe en el sistema.")
            asset.number = number

        asset.observations = data.get('observations')

        # Actualizamos solo los datos correspondientes a su tipo
        if asset.asset_type == 'tracto':
            asset.brand = data.get('brand')
            asset.model_name = data.get('model_name')
            asset.transmission = data.get('transmission')
            asset.operator = data.get('operator')
            asset.operator_number = data.get('operator_number')
            asset.engine = data.get('engine')
        elif asset.asset_type == 'caja':
            asset.plates = data.get('plates')
            asset.dimensions = data.get('dimensions')
            asset.state = data.get('state')
            asset.condition = data.get('condition')

        asset.save()
        return asset
    except Asset.DoesNotExist:
        raise ValidationError("El activo no existe.")