from django.shortcuts import render
from django.http import JsonResponse

def home(request):
	return render(request, 'index.html')

def get_data(request):

	data = {
		'male_data': [41, 26, 57, 47, 49, 40, 67, 68, 24, 26],
		'female_data': [62, 39, 67, 33, 58, 67, 50, 48, 21, 30],
		'label_data': ['13-17', '18-24', '25-34', '34-44', '45-54', '55-64'],
	}

	return JsonResponse(data)
