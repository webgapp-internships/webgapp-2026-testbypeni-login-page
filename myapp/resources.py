from import_export import resources
from .models import Forms

class FormsResource(resources.ModelResource):
    class Meta:
        model = Forms
        # include only specific fields (if you don’t want all)
        fields = (
            'id',
            'full_name',
            'email',
            'phone',
            'dob',
            'gender',
            'message',
            'agree_terms',
            'created_at',
        )
        export_order = (
            'id',
            'full_name',
            'email',
            'phone',
            'dob',
            'gender',
            'message',
            'agree_terms',
            'created_at',
        )
