from django import forms

from catalog.models import Product, Version


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control', 'form-check-input'
            field.widget.attrs['current_version'] = 'form-check-input'


class ProductForm(FormMixin, forms.ModelForm):
    an_invalid = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['product_name', 'title', 'image_preview', 'category', 'purchase_price', 'is_published']

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        if cleaned_data.lower() in self.an_invalid:
            raise forms.ValidationError(f'Не допустимое слово - {cleaned_data}')
        return cleaned_data

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        if cleaned_data.lower() in self.an_invalid:
            raise forms.ValidationError(f'Не допустимое слово - {cleaned_data}')
        return cleaned_data


class ProductModeratorForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published', 'title', 'category']


class VersionForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'current_version']
