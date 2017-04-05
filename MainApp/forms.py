# -*- coding: utf-8 -*-
from django import forms


class MatrixForm(forms.Form):
    matrix_a = forms.CharField(widget=forms.Textarea)
    matrix_b = forms.CharField(widget=forms.Textarea)


class GenerateForm(forms.Form):
    a_raw_num = forms.CharField(max_length=20, label='Raw number for matrix A')
    a_col_num = forms.CharField(max_length=20, label='Column number for matrix A')
