'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.callback import OrderInfoCallback
from krypton_cryptofeed.defines import OKX, ORDER_INFO


async def order(oi, receipt_timestamp):
    print(f"Order update received at {receipt_timestamp}: {oi}")


def main():

    path_to_config = 'config.yaml'
    f = FeedHandler(config=path_to_config)
    f.add_feed(OKX,
               channels=[ORDER_INFO],
               symbols=["ETH-USDT-PERP", "BTC-USDT-PERP"],
               callbacks={ORDER_INFO: OrderInfoCallback(order)},
               timeout=-1)
    f.run()


if __name__ == "__main__":
    main()
