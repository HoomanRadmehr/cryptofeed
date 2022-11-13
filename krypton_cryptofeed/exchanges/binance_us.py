'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
import logging

from krypton_cryptofeed.connection import RestEndpoint, WebsocketEndpoint, Routes
from krypton_cryptofeed.defines import BINANCE_US
from krypton_cryptofeed.exchanges.binance import Binance
from krypton_cryptofeed.exchanges.mixins.binance_rest import BinanceUSRestMixin


LOG = logging.getLogger('feedhandler')


class BinanceUS(Binance, BinanceUSRestMixin):
    id = BINANCE_US
    websocket_endpoints = [WebsocketEndpoint('wss://stream.binance.us:9443')]
    rest_endpoints = [RestEndpoint('https://api.binance.us', routes=Routes('/api/v3/exchangeInfo', l2book='/api/v3/depth?symbol={}&limit={}'))]
