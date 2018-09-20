from django.shortcuts import render
from django.views import View

class IndexView(View):

	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})


class MovieDetailView(View):

	template_name = 'movie_detail.html'


	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})