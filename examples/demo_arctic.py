'''
Copyright (C) 2018-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.arctic import FundingArctic, TickerArctic, TradeArctic
from krypton_cryptofeed.defines import FUNDING, TICKER, TRADES
from krypton_cryptofeed.exchanges import Bitfinex, Bitmex, Coinbase


def main():
    f = FeedHandler()
    f.add_feed(Bitmex(channels=[TRADES, FUNDING], symbols=['BTC-USD-PERP'], callbacks={TRADES: TradeArctic('cryptofeed-test'), FUNDING: FundingArctic('cryptofeed-test')}))
    f.add_feed(Bitfinex(channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeArctic('cryptofeed-test')}))
    f.add_feed(Coinbase(channels=[TICKER], symbols=['BTC-USD'], callbacks={TICKER: TickerArctic('cryptofeed-test')}))
    f.run()


if __name__ == '__main__':
    main()
