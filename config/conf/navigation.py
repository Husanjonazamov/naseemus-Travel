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
        "title": _("Foydalanuvchilar"),
        "separator": True,
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "icon": "group",  # MSO: group
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
        ],
    },
    {
        "title": _("E'lonlar"),
        "separator": True,
        "items": [
            {
                "title": _("Elonlar"),
                "icon": "campaign",
                "link": reverse_lazy("admin:api_listingmodel_changelist"),
            },
            {
                "title": _("Elon Tarifi"),
                "icon": "description",  # MSO: description (yoki 'article')
                "link": reverse_lazy("admin:api_postingtypemodel_changelist"),
            },
            {
                "title": _("Avzalliklar"),
                "icon": "star",  # MSO: star (yoki 'grade', 'local_fire_department')
                "link": reverse_lazy("admin:api_featuremodel_changelist"),
            },
        ],
    },
]
