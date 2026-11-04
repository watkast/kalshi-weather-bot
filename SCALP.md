# Range-Scalp Bot

*Updated Wed Nov 04 17:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47280 | 41169 | 6111 (72) | 0 | $-13633.80 | -4.6% |
| **+10¢** | 35322 | 28232 | 7090 (97) | 0 | $-12472.36 | -5.6% |
| **+15¢** | 29578 | 21945 | 7633 (125) | 0 | $-11437.10 | -6.2% |
| **+20¢** | 26278 | 18284 | 7994 (165) | 2 | $-10094.53 | -6.1% |
| **+10¢ (15¢ stop)** | 57629 | 57536 | 93 (56) | 0 | $-21491.41 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 17:04 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 17:04 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-04 17:04 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 17:04 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 17:04 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 17:04 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-04 17:03 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-04 17:02 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-04 17:02 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-04 17:02 | +10 stop | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-04 17:02 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-04 17:02 | +15 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-04 17:02 | +10 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-04 17:02 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-04 17:02 | +5 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 11-04 17:02 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 17:02 | +20 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-04 17:02 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-04 17:02 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 17:02 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 11-04 17:01 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 17:01 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-04 17:01 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-04 17:01 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 17:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-04 17:01 | +10 stop | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-04 17:01 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-04 17:01 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-04 17:01 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-04 17:01 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-04 17:01 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 17:01 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-04 17:01 | +15 | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-04 17:01 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 17:01 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 17:01 | +10 stop | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-04 17:01 | +20 | XRP | DOWN | 0.64 | 0.88 | 2.15 |
| 11-04 17:01 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-04 17:01 | +10 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-04 17:01 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
