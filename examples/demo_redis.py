'''
Copyright (C) 2018-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.redis import BookRedis, BookStream, CandlesRedis, FundingRedis, OpenInterestRedis, TradeRedis
from krypton_cryptofeed.defines import CANDLES, FUNDING, L2_BOOK, OPEN_INTEREST, TRADES
from krypton_cryptofeed.exchanges import Bitfinex, Bitmex, Coinbase, Gemini, Binance


def main():
    config = {'log': {'filename': 'redis-demo.log', 'level': 'INFO'}, 'backend_multiprocessing': True}
    f = FeedHandler(config=config)
    f.add_feed(Bitmex(channels=[TRADES, FUNDING, OPEN_INTEREST], symbols=['BTC-USD-PERP'], callbacks={TRADES: TradeRedis(), FUNDING: FundingRedis(), OPEN_INTEREST: OpenInterestRedis()}))
    f.add_feed(Bitfinex(channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeRedis()}))
    f.add_feed(Coinbase(config=config, channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeRedis()}))
    f.add_feed(Coinbase(channels=[L2_BOOK], symbols=['BTC-USD'], callbacks={L2_BOOK: BookStream()}))
    f.add_feed(Gemini(symbols=['BTC-USD'], callbacks={TRADES: TradeRedis()}))
    f.add_feed(Binance(candle_closed_only=True, symbols=['BTC-USDT'], channels=[CANDLES], callbacks={CANDLES: CandlesRedis(score_key='start')}))
    f.add_feed(Binance(max_depth=10, symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookRedis(snapshots_only=True)}))

    f.run()


if __name__ == '__main__':
    main()
