from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",  # MSO: home
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    
   {
        "title": _("Turlar"),
        "separator": True,
        "items": [
            {
                "title": _("Banner"),
                "icon": "image",  # bannerga mos - reklama/rasm
                "link": reverse_lazy("admin:api_bannermodel_changelist"),
            },
            {
                "title": _("Hotel"),
                "icon": "hotel",  # hotel uchun to‘g‘ridan-to‘g‘ri icon bor
                "link": reverse_lazy("admin:api_hotelmodel_changelist"),
            },
            {
                "title": _("Sanatorya"),
                "icon": "spa",  # hotel uchun to‘g‘ridan-to‘g‘ri icon bor
                "link": reverse_lazy("admin:api_sanatorymodel_changelist"),
            },
            {
                "title": _("Turlar"),
                "icon": "travel_explore",  # sayohat uchun mos icon
                "link": reverse_lazy("admin:api_tourmodel_changelist"),
            },
            {
                "title": _("Blog"),
                "icon": "article",  # blog/matn uchun article icon mos
                "link": reverse_lazy("admin:api_blogmodel_changelist"),
            },
        ],
    }

]
