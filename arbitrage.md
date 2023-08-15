## Description

Crypto assets are traded on multiple exchanges. The price of an asset can vary from one exchange to another. This
opens up to arbitrage opportunities. Arbitrage is the process of buying an asset on one exchange and selling it on
another exchange at a higher price. The difference in price is the profit.

In this problem, you are required to write a program that finds arbitrage opportunities in the crypto market and
executes them in a "paper-trading" fashion. The opportunity shall be taken when the profit is greater than a certain
configurable threshold.

The data source you are asked to use is the Coinmarketcap API (https://coinmarketcap.com/api/). You can use the
free tier of the API. Choose a set of liquid assets (e.g. BTC, ETH, USDT) and find arbitrage opportunities between the
most common exchanges (ie: Binance, Coinbase, Kraken, Bitfinex, etc).

For the sake of simplicity and time, you can assume that the following conditions are true:

- the user has unlimited funds
- the user has access to all exchanges
- the user can execute trades instantaneously
- no transaction fees are applied

## Requirements

Build a websocket service that allows the user to specify a threshold and adjust it in real-time. When an arbitrage opportunity is found, the service should notify the user via the websocket onnection with information about the opportunity (asset, exchanges, profit, etc).

Trades should also be stored in a database and exposed via a REST API. The REST API should provide some basic form of authentication and allow the user to query historical trades.
