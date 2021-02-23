from django.http import HttpResponse


def homepage(request):
    return HttpResponse("""
    <h1>Woohoo!</h1>
    <p>Everything is setup correctly. Congratulations! It's all downhill from here.<p>
    """)