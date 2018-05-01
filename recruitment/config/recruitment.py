from frappe import _


def get_data():
    return [
        {
            "module_name": "Recruitment",
            "color": "grey",
            "icon": "fa fa-star",
            "type": "module",
            "label": _("Recruitment"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Candidate",
                    "icon": "fa fa-star",
                    "label": _("Candidate"),
                    "description": _("VHRS Candidate Database"),
                },
                {
                    "type": "doctype",
                    "name": "Interview",
                    "label": _("Interview"),
                    "description": _("Interviews for Projects"),
                },

                {
                    "type": "doctype",
                    "name": "Associate",
                    "label": _("Associate"),
                    "description": _("VHRS Associate Database"),
                    "hide_count": False
                }
            ]
        }
    ]
