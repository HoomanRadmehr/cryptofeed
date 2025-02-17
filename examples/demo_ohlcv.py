'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.aggregate import OHLCV
from krypton_cryptofeed.defines import TRADES
from krypton_cryptofeed.exchanges import Coinbase


async def ohlcv(data):
    print(data)


def main():
    f = FeedHandler()
    f.add_feed(Coinbase(symbols=['BTC-USD', 'ETH-USD', 'BCH-USD'], channels=[TRADES], callbacks={TRADES: OHLCV(ohlcv, window=10)}))

    f.run()


if __name__ == '__main__':
    main()
