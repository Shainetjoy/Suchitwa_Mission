from smApp.models import PlasticCollectionSchedule
from datetime import date, timedelta

def global_context(request):
    user_id = request.session['user_id'] 
    today = date.today()
    start_date = today 
    end_date = today + timedelta(days=2) 
    filtered_data = PlasticCollectionSchedule.objects.filter(date__range=(start_date, end_date), user=user_id)
    print(filtered_data)
    context = {
        'filtered_data':filtered_data,
        'count':filtered_data.count()
    }
    return context