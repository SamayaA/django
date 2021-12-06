import csv
from os import stat

from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from pagination import settings

def index(request):
    return redirect(reverse('bus_stations'))

def form_data():
    '''
    Delete unneccessary data.
    '''
    with open(settings.BUS_STATION_CSV, newline='', encoding='UTF-8') as csvfile:
        information = csv.DictReader(csvfile, delimiter=',')
        bus_stations = []
        for station in information:
            del station["ID"], station["Longitude_WGS84"],\
                station["Latitude_WGS84"], station["AdmArea"],  \
                station["RouteNumbers"], station["StationName"], \
                station["Direction"], station["Pavilion"], station["OperatingOrgName"], \
                station["EntryState"], station["global_id"], station["geoData"]
            bus_stations.append(station)
    return bus_stations

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = form_data()        
    paginator = Paginator(bus_stations, 10)
    current_page = request.GET.get("page", 1)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
