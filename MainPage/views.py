from django.shortcuts import render

#below function loads the landingpage html

def landing_view(request):
    image_list = [
        '../media/venue_images/Ahluwalia_PLC_58.jpg',
        '../media/venue_images/Arora-Gandhi_20.jpg',
        '../media/venue_images/Bal_Baral_and_Majumdar_15.jpg',
    ]
    return render(request, 'MainPage/landingpage.html', {'images': image_list})

