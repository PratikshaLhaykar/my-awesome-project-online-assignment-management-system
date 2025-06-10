from django.template import Library
import datetime
register = Library()

@register.filter(name="checkDateExpire")
def checkDateExpire(submission_date):
    today_date = datetime.datetime.today().date()
    print(submission_date, today_date)
    if today_date > submission_date:
        return False
    return True