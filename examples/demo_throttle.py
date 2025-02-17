'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from datetime import datetime as dt

from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.aggregate import Throttle
from krypton_cryptofeed.defines import L2_BOOK
from krypton_cryptofeed.exchanges import Coinbase


async def callback(data, receipt):
    print(f"Book received at {dt.utcfromtimestamp(receipt).strftime('%Y-%m-%d %H:%M:%S')} UTC - {data}")


def main():
    f = FeedHandler()
    f.add_feed(Coinbase(symbols=['BTC-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: Throttle(callback, window=10)}))

    f.run()


if __name__ == '__main__':
    main()
