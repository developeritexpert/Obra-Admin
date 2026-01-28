from django import forms

from catalog.models import (
    Image,
    ImageProduct,
    ImageVariant,
    MaterialProduct,
    FinishProduct,
    BorderProduct,
    StyleProduct,
    StyleVariant,
    FinishVariant,
)


# -------------------------
# Base Image
# -------------------------

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image_url"]


# -------------------------
# Image Relations
# -------------------------

class ImageProductForm(forms.ModelForm):
    class Meta:
        model = ImageProduct
        fields = ["image", "product"]


class ImageVariantForm(forms.ModelForm):
    class Meta:
        model = ImageVariant
        fields = ["image", "variant"]


# -------------------------
# Product Attribute Relations
# -------------------------

class MaterialProductForm(forms.ModelForm):
    class Meta:
        model = MaterialProduct
        fields = ["material", "product"]


class FinishProductForm(forms.ModelForm):
    class Meta:
        model = FinishProduct
        fields = ["finish", "product"]


class BorderProductForm(forms.ModelForm):
    class Meta:
        model = BorderProduct
        fields = ["border", "product"]


class StyleProductForm(forms.ModelForm):
    class Meta:
        model = StyleProduct
        fields = ["style", "product"]


# -------------------------
# Variant Attribute Relations
# -------------------------

class StyleVariantForm(forms.ModelForm):
    class Meta:
        model = StyleVariant
        fields = ["style", "variant"]


class FinishVariantForm(forms.ModelForm):
    class Meta:
        model = FinishVariant
        fields = ["finish", "variant"]
