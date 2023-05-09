from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .utils import *
from .models import ShortenedUrl

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

@api_view(["POST"])
def encodeURL(request):
    try:
        full_url = request.data.get("full_url")

        # Check if the full URL already exists in the ShortenedUrl table
        existing_entry = ShortenedUrl.objects.filter(full_url=full_url).first()
        if existing_entry:
            short_url = encode_url(existing_entry.short_code)
        else:
            # Generate a new short code for the URL
            short_code = generate_short_code()

            # Check for unique short URL, regenerate code until unique one is made
            while ShortenedUrl.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()

            # Create a new entry in the ShortenedUrl table
            shortened_url = ShortenedUrl.objects.create(full_url=full_url, short_code=short_code)
            short_url = encode_url(shortened_url.short_code)

        return JsonResponse({'short_url': short_url})

    # Error handling
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'success': False})

@api_view(["POST"])
def decodeURL(request):
    try:
        # Gets data from POST, extracts code from URL
        short_url = request.data.get("short_url")
        short_code = short_url.split('/')[-1]
        
        # Checks database for full url
        instance = ShortenedUrl.objects.get(short_code=short_code)
        return JsonResponse({'full_url': instance.full_url})
    
    # Error handling
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'success': False})