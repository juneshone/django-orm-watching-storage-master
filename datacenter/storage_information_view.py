from datacenter.models import Visit, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(visit.get_duration(), "%H:%M:%S"),
                'is_strange': visit.is_visit_long()
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
