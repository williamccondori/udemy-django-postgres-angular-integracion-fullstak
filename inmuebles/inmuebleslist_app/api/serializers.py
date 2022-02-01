from dataclasses import field
from rest_framework import serializers

from inmuebleslist_app.models import Empresa, Edificacion


class EficicacionSerializer(serializers.ModelSerializer):
    # longitud_direccion = serializers.SerializerMethodField()
    
    class Meta:
        model = Edificacion
        fields = "__all__"
        # fields = ['id', 'pais', 'active', 'imagen']
        # exclude = ['id']
        
class EmpresaSerializer(serializers.ModelSerializer):
    # edificaciones = EficicacionSerializer(many=True, read_only=True)
    # edificaciones = serializers.StringRelatedField(many=True)
    # edificaciones = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    edificaciones = serializers.HyperlinkedRelatedField(
        view_name='edificacion-detalle', many=True, read_only=True)
    class Meta:
        model = Empresa
        fields = "__all__"

        
    # def get_longitud_direccion(self, obj):
    #     cantidad_caracteres = len(obj.direccion)
    #     return cantidad_caracteres

    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("La dirección no puede ser igual al país")
    #     return data
    
    # def validate_imagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("La imagen debe tener al menos 2 caracteres")
    #     return data


# def column_logitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("La columna debe tener al menos 2 caracteres")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_logitud])
#     pais = serializers.CharField(validators=[column_logitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("La dirección no puede ser igual al país")
#         return data
    
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("La imagen debe tener al menos 2 caracteres")
#         return data
