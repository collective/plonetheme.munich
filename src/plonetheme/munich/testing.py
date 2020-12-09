# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import plonetheme.munich


class PlonethemeMunichLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.munich)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.munich:default')


PLONETHEME_MUNICH_FIXTURE = PlonethemeMunichLayer()


PLONETHEME_MUNICH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_MUNICH_FIXTURE,),
    name='PlonethemeMunichLayer:IntegrationTesting',
)


PLONETHEME_MUNICH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_MUNICH_FIXTURE,),
    name='PlonethemeMunichLayer:FunctionalTesting',
)


PLONETHEME_MUNICH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_MUNICH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeMunichLayer:AcceptanceTesting',
)
