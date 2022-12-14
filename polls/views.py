from django.http import HttpResponse
import json
# Create your views here.
users = {
    "name": "SR",
    "gender": "male"
}
user_json=json.dumps(users)
class Views:
    def index(request):
        return HttpResponse(user_json)