from django.contrib import admin
from .models import Employees
from .models import ClientBuy
from .models import ClientSell
from .models import Property
from .models import SelledProperty


admin.site.register(Employees)
admin.site.register(ClientBuy)
admin.site.register(ClientSell)
admin.site.register(Property)
admin.site.register(SelledProperty)

