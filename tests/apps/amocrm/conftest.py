import pytest


@pytest.fixture(autouse=True)
def _settings_amocrm(settings):
    settings.AMOCRM_BASE_URL = "https://test.amocrm.ru"
    settings.AMOCRM_REDIRECT_URL = "https://test-education.ru"
    settings.AMOCRM_INTEGRATION_ID = "4815162342"
    settings.AMOCRM_CLIENT_SECRET = "top-secret-007"
    settings.AMOCRM_AUTHORIZATION_CODE = "1337yep"


@pytest.fixture(autouse=True)
def _disable_automatic_amocrm_updating(mocker):
    mocker.patch("apps.orders.services.order_paid_setter.OrderPaidSetter.update_amocrm", return_value=None)


@pytest.fixture
def amocrm_user(mixer, user):
    return mixer.blend("amocrm.AmoCRMUser", user=user, customer_id=4444, contact_id=5555)


@pytest.fixture
def amocrm_course(mixer, course):
    return mixer.blend("amocrm.AmoCRMCourse", course=course, amocrm_id=999111)


@pytest.fixture
def _amocrm_groups(factory, mixer):
    factory.group(slug="popug")
    group_with_amo = factory.group(slug="hehe")
    mixer.blend("amocrm.AmoCRMProductGroup", amocrm_id=333, group=group_with_amo)
