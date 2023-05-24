from django import forms
from .models import Items
class Search(forms.Form):
    box=forms.CharField(label='search box',widget=forms.TextInput(attrs={'placeholder':'Search here... '}),required=False)

    def search(self) -> dict:
        context={}
        box = self.cleaned_data.get('box').lower()
        print(box)
        if Items.objects.filter(restaurant__name=box).exists():
            context['restaurants'] = Items.objects.filter(restaurant__name=box)
        if Items.objects.filter(title=box).exists():
            context['titles'] = Items.objects.filter(title=box)
        if Items.objects.filter(discription=box).exists():
            context['descriptions'] = Items.objects.filter(discription=box)
        if Items.objects.filter(category__tag=box).exists():
            context['categories'] = Items.objects.filter(category__tag=box)
        return context