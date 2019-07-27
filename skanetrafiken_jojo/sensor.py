"""
Get Jojo card balance from Skånetrafiken website.
"""
import logging

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_NAME, CONF_SCAN_INTERVAL, STATE_UNKNOWN)
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

CONF_CARD_NUMBER = 'card_number'
CONF_CARD_CVC = 'card_cvc'

DEFAULT_NAME = 'Jojo'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_CARD_NUMBER): cv.string,
    vol.Required(CONF_CARD_CVC): cv.string,
    vol.Required(CONF_SCAN_INTERVAL, default=3600): cv.time_period,
})


def setup_platform(_hass, config, add_entities, _discovery_info=None):
    name = config.get(CONF_NAME)
    card_number = config.get(CONF_CARD_NUMBER)
    card_cvc = config.get(CONF_CARD_CVC)
    add_entities([JojoSensor(name, card_number, card_cvc)], True)
    return True


class JojoSensor(Entity):

    def __init__(self, name, card_number, card_cvc):
        self._name = name
        self._card_number = card_number
        self._card_cvc = card_cvc
        self._state = STATE_UNKNOWN

    @property
    def name(self):
        return self._name

    @property
    def unit_of_measurement(self):
        return 'kr'

    @property
    def state(self):
        return self._state

    def update(self):
        import mechanicalsoup

        browser = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'html5lib'},
            raise_on_404=True,
        )
        try:
            _LOGGER.info("Updating Jojo balance for card %s", self._card_number)
            browser.open("https://www.skanetrafiken.se/e-tjanster/se-saldo-och-ladda-kort1/")
            browser.select_form('form#view-balance-and-charge-card-directly-form')
            browser['request.CardNumber'] = self._card_number
            browser['request.Cvc'] = self._card_cvc
            browser.submit_selected()
            balance = browser.get_current_page().select(".balance")
            if balance:
                balance = balance[0].string
                balance = balance.strip().split(' ')[0].replace(',', '.')
                self._state = balance
            else:
                self._state = STATE_UNKNOWN
        finally:
            browser.close()
