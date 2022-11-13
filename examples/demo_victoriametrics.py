'''
Copyright (C) 2018-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.victoriametrics import TradeVictoriaMetrics, TickerVictoriaMetrics, BookVictoriaMetrics, CandlesVictoriaMetrics
from krypton_cryptofeed.defines import TRADES, TICKER, L2_BOOK, CANDLES
from krypton_cryptofeed.exchanges import Coinbase, Binance


def main():
    addr = 'tcp://localhost'
    port = 8189

    f = FeedHandler()
    f.add_feed(Coinbase(channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeVictoriaMetrics(addr, port, 'demo-trades')}))
    f.add_feed(Coinbase(channels=[TICKER], symbols=['BTC-USD'], callbacks={TICKER: TickerVictoriaMetrics(addr, port, 'demo-tickers')}))
    f.add_feed(Coinbase(channels=[L2_BOOK], symbols=['BTC-USD'], callbacks={L2_BOOK: BookVictoriaMetrics(addr, port, 'demo-book')}))
    f.add_feed(Binance(channels=[CANDLES], symbols=['BTC-USDT'], callbacks={CANDLES: CandlesVictoriaMetrics(addr, port, 'demo-candles')}))

    f.run()


if __name__ == '__main__':
    main()
