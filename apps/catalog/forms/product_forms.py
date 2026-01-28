from django import forms
from django.forms import inlineformset_factory

from catalog.models import (
    Product,
    Variant,
    ImageProduct,
    StyleProduct,
)

from apps.catalog.forms.variant_forms import VariantForm
from apps.catalog.forms.relation_forms import (
    ImageProductForm,
    StyleProductForm,
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "sku",
            "description",
            "base_price",
            "box_price",
            "no_of_pieces_per_box",
            "thickness",
            "weight",
            "width",
            "height",
            "length",
            "unit_type",
            "in_stock",
            "status",
            "diagram_url",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "status": forms.Select(),
            "unit_type": forms.Select(),
        }


# -------------------------
# Inline Formsets (Product)
# -------------------------

ProductVariantFormSet = inlineformset_factory(
    Product,
    Variant,
    form=VariantForm,
    extra=1,
    can_delete=True,
)

ProductImageFormSet = inlineformset_factory(
    Product,
    ImageProduct,
    form=ImageProductForm,
    extra=1,
    can_delete=True,
)

ProductStyleFormSet = inlineformset_factory(
    Product,
    StyleProduct,
    form=StyleProductForm,
    extra=1,
    can_delete=True,
)
