from django.shortcuts import render
from django.http import HttpResponse
import os

def createkillteam(request):
    if request.method == 'POST':
        killteam_name = request.POST.get('killteam_name')
        player_name = request.POST.get('player_name')
        faction_keyword = request.POST.get('faction_keyword')
        base_name = request.POST.get('base-name') #check variable name
        backstory = request.POST.get('backstory') #check variable name
        
        # Define the file path
        file_path = os.path.join(os.path.dirname(__file__), 'killteamdata.txt')
        
        # Save the data to a text file
        with open(file_path, 'a') as file:
            file.write(f'{killteam_name},\n{player_name},\n{faction_keyword},\n{base_name},\n{backstory}')
        
        return HttpResponse(f'Thank you {player_name}, we have received the submission.')
    
    return render(request, 'createkillteam.html')