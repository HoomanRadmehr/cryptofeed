'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from multiprocessing import Process

from krypton_cryptofeed import FeedHandler
from krypton_cryptofeed.backends.rabbitmq import BookRabbit
from krypton_cryptofeed.defines import L2_BOOK
from krypton_cryptofeed.exchanges import Kraken


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())


def receiver(port):
    import pika
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=port))
    channel = connection.channel()
    channel.queue_declare(queue='cryptofeed', durable=True)
    channel.basic_consume(queue='cryptofeed',
                          on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    try:
        p = Process(target=receiver, args=(5672,))

        p.start()

        f = FeedHandler()
        f.add_feed(Kraken(max_depth=2, channels=[L2_BOOK], symbols=['BTC-USD', 'ETH-USD'], callbacks={L2_BOOK: BookRabbit()}))

        f.run()

    finally:
        p.terminate()


if __name__ == '__main__':
    main()
