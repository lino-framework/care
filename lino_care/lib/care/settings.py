# -*- coding: UTF-8 -*-
# Copyright 2014-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""
Base Django settings for Lino Care applications.

"""

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_care import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Care"
    description = SETUP_INFO['description']
    version = SETUP_INFO['version']
    url = SETUP_INFO['url']

    demo_fixtures = ['std', 'demo', 'demo2']
                     # 'linotickets',
                     # 'tractickets', 'luc']

    # project_model = 'tickets.Project'
    # project_model = 'deploy.Milestone'
    textfield_format = 'plain'
    # textfield_format = 'html'
    user_types_module = 'lino_care.lib.care.user_types'
    workflows_module = 'lino_care.lib.care.workflows'
    obj2text_template = "**{0}**"
    custom_layouts_module = 'lino_care.lib.care.layouts'

    default_build_method = 'appyodt'

    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'

    # TODO: move migrator to lino_care.projects.team
    migration_class = 'lino_care.lib.care.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_care"

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps` for Lino
        Care.

        """
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.extjs'
        # yield 'lino.modlib.bootstrap3'
        # yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino_care.lib.contacts'
        yield 'lino.modlib.comments'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.phones'
        yield 'lino.modlib.checkdata'
        # yield 'lino_care.lib.users'
        # yield 'lino_care.lib.cal'
        # yield 'lino_xl.lib.extensible'
        # yield 'lino_care.lib.courses'
        # yield 'lino_care.lib.products'

        # yield 'lino_care.lib.topics'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_care.lib.tickets'
        yield 'lino_xl.lib.skills'
        #yield 'lino_xl.lib.deploy'
        # yield 'lino_care.lib.working'
        # yield 'lino_xl.lib.lists'
        # yield 'lino_xl.lib.blogs'

        #yield 'lino.modlib.changes'
        #yield 'lino.modlib.notify'
        #yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino.modlib.export_excel'
        # yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.smtpd'
        # yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.dashboard'

        # yield 'lino.modlib.awesomeuploader'

        yield 'lino_care.lib.care'
        # yield 'lino_xl.lib.inbox'
        # yield 'lino_xl.lib.mailbox'
        # yield 'lino_xl.lib.meetings'


    # def setup_plugins(self):
    #     super(Site, self).setup_plugins()
    #     # self.plugins.comments.configure(
    #     #     commentable_model='tickets.Ticket')
    #     self.plugins.skills.configure(
    #         demander_model=None)
        # self.plugins.tickets.configure(
        #     site_model='cal.Room',
        #     milestone_model='courses.Course')

    def get_default_required(self, **kw):
        # overrides the default behaviour which would add
        # `auth=True`. In Lino Care everybody can see everything.
        return kw


# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'
