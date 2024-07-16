from django.shortcuts import render
from django.views import View
from app_1.cryptography.crypto_files import folder_path


class IndexView(View):
    def get(self, request):
        path_to_crypto = folder_path
        context = {
            'path_to_crypto': path_to_crypto,
        }
        
        return render(request, 'index/index.html', context)

