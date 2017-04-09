import numpy as np

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
import time
from .forms import MatrixForm, GenerateForm


class MatrixView(FormView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        kwargs = self.get_form_kwargs()
        form_class = MatrixForm
        data = kwargs.get('data')
        if data and data.get('a_raw_num'):
            form_class = GenerateForm
        return form_class(**kwargs)

    def get_context_data(self, **kwargs):
        kwargs['gen_form'] = GenerateForm()
        kwargs['mult_form'] = GenerateForm()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        start_time = time.time()
        try:
            matrix_a = form.cleaned_data.get('matrix_a')
            matrix_b = form.cleaned_data.get('matrix_b')
            a_raw_num = int(form.cleaned_data.get('a_raw_num', 0))
            a_col_num = int(form.cleaned_data.get('a_col_num', 0))
            if matrix_a and matrix_b:
                a = np.matrix(matrix_a.replace('\n', ';'))
                b = np.matrix(matrix_b.replace('\n', ';'))
            else:
                a = np.matrix(np.ones((a_raw_num, a_col_num), dtype=np.int))
                b = np.matrix(np.ones((a_col_num, a_raw_num), dtype=np.int))
            c = a * b
            res = str(c).replace('\n', ' ')
            print (res)
        except TypeError:
            res = 'Matrix must only contain numbers!'
        except ValueError:
            res = 'Matrix can not be multiplied because of size!'
        return JsonResponse({'matrix_c': res, 'time': (time.time() - start_time)})


    def form_invalid(self, form):
        data = {}
        errors = {key: str(value) for key, value in form.errors.items()}
        data['errors'] = errors
        return JsonResponse(data)
