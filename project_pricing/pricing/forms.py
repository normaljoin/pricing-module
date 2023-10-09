from django import forms
from .models import Config, DistanceBaseTier, Week


class DistanceBaseTierAdminForm(forms.ModelForm):
    selected_days = forms.ModelMultipleChoiceField(
        queryset=Week.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = DistanceBaseTier
        fields = '__all__'

    def clean_selected_data(self):
        selected_days = self.cleaned_data['selected_days']
        selected_day_names = [day.day for day in selected_days]
        return selected_day_names

class ConfigAdminForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        is_active = cleaned_data.get('is_active')

        if is_active:
            existing_active_objects = Config.objects.filter(is_active=True)
            if self.instance and self.instance.pk:
                existing_active_objects = existing_active_objects.exclude(pk=self.instance.pk)

            if existing_active_objects.exists():
                raise forms.ValidationError('There can be only one row with is_active=True.')
            


# not working because getting a json error 

# @admin.register(Config)
# class ConfigAdmin(admin.ModelAdmin):
#     def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
#         if not obj.pk:
#             obj.created_by = request.user
#         else:
#             obj.modified_by = request.user
#         super().save_model(request, obj, form, change)
#     list_display = ('name', 'is_active', 'created_by', 'modified_by')

#     def get_form(self, request, obj, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields['created_by'].widget = forms.HiddenInput()
#         form.base_fields['modified_by'].widget = forms.HiddenInput()
#         return form