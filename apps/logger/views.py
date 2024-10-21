from django.views import View
from .models import StatusLog
from django.http import HttpResponse
import logging
from django.utils import timezone 

# Create your views here.

class LoggerView(View): # pragma: no cover
    def get(self, request):
        status_logs = StatusLog.objects.all().order_by('-create_datetime')
        html = '<html><body style="background:black; color:white;"><h1>Logs</h1><ul>'
        # Convert the datetime to the local timezone
        
        for log in status_logs:

            if log.level in [logging.NOTSET, logging.INFO]:
                color = 'green'
            elif log.level in [logging.WARNING, logging.DEBUG]:
                color = 'orange'
            else:
                color = 'red'

            local_time = timezone.localtime(log.create_datetime)
            html += f'''
               <span style="color: {color};"><span style="color:white"></span>{local_time.strftime('%Y-%m-%d %I:%M %p')} - {log.get_level_display().upper()} - {log.msg}</span> <br>
            '''
            if log.trace:
                trace = f"""
                <pre>{log.trace}</pre>
                """
                html += trace
        if not status_logs:
            html += '<li>No logs available.</li>'
        
        html += '</ul></body></html>'
        return HttpResponse(html)