from django import forms
from django.forms import inlineformset_factory

from catalog.models import (
    Variant,
    ImageVariant,
    StyleVariant,
    FinishVariant,
)

from apps.catalog.forms.relation_forms import (
    ImageVariantForm,
    StyleVariantForm,
    FinishVariantForm,
)


class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = [
            "product",
            "sku",
            "variant_name",
            "description",
            "base_price",
            "thickness",
            "weight",
            "width",
            "height",
            "length",
            "unit_type",
            "in_stock",
            "colors",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "colors": forms.Textarea(
                attrs={
                    "rows": 2,
                    "placeholder": '["White", "Beige"]',
                }
            ),
        }


# -------------------------
# Inline Formsets (Variant)
# -------------------------

VariantImageFormSet = inlineformset_factory(
    Variant,
    ImageVariant,
    form=ImageVariantForm,
    extra=1,
    can_delete=True,
)

VariantStyleFormSet = inlineformset_factory(
    Variant,
    StyleVariant,
    form=StyleVariantForm,
    extra=1,
    can_delete=True,
)

VariantFinishFormSet = inlineformset_factory(
    Variant,
    FinishVariant,
    form=FinishVariantForm,
    extra=1,
    can_delete=True,
)
