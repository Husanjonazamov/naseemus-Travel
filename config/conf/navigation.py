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
                "icon": "campaign",
                "link": reverse_lazy("admin:api_bannermodel_changelist"),
            },
            {
                "title": _("Turlar"),
                "icon": "campaign",
                "link": reverse_lazy("admin:api_tourmodel_changelist"),
            },
            {
                "title": _("Blog"),
                "icon": "description",  # MSO: description (yoki 'article')
                "link": reverse_lazy("admin:api_blogmodel_changelist"),
            },
        ],
    },
]
