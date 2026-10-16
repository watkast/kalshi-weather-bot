# Range-Scalp Bot

*Updated Fri Oct 16 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18915 | 16436 | 2479 (28) | 1 | $-5703.51 | -4.8% |
| **+10¢** | 14242 | 11372 | 2870 (40) | 2 | $-5186.03 | -5.8% |
| **+15¢** | 11932 | 8845 | 3087 (59) | 2 | $-4679.42 | -6.2% |
| **+20¢** | 10595 | 7364 | 3231 (78) | 2 | $-4110.77 | -6.2% |
| **+10¢ (15¢ stop)** | 23259 | 23209 | 50 (29) | 0 | $-8979.79 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 07:59 | +10 stop | BNB | UP | 0.31 | 0.58 | 2.40 |
| 10-16 07:59 | +15 | BNB | UP | 0.30 | 0.58 | 2.47 |
| 10-16 07:59 | +10 | BNB | UP | 0.29 | 0.58 | 2.57 |
| 10-16 07:59 | +5 | BNB | UP | 0.29 | 0.58 | 2.57 |
| 10-16 07:58 | +10 stop | HYPE | UP | 0.49 | 0.19 | -3.29 |
| 10-16 07:56 | +10 | ETH | UP | 0.70 | 0.87 | 1.47 |
| 10-16 07:56 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 10-16 07:55 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 10-16 07:55 | +10 stop | HYPE | DOWN | 0.56 | 0.32 | -2.72 |
| 10-16 07:55 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.31 |
| 10-16 07:54 | +10 stop | XRP | DOWN | 0.65 | 0.47 | -2.14 |
| 10-16 07:54 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-16 07:54 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-16 07:54 | +10 stop | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-16 07:54 | +10 | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-16 07:54 | +5 | BTC | UP | 0.65 | 0.74 | 0.60 |
| 10-16 07:54 | +5 | ZEC | UP | 0.64 | 0.75 | 0.79 |
| 10-16 07:54 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-16 07:54 | +20 | ETH | UP | 0.55 | 0.78 | 1.99 |
| 10-16 07:54 | +15 | ETH | UP | 0.55 | 0.78 | 1.99 |
| 10-16 07:54 | +10 | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-16 07:54 | +5 | ETH | UP | 0.55 | 0.63 | 0.45 |
| 10-16 07:53 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 07:53 | +5 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 07:53 | +10 stop | XRP | DOWN | 0.55 | 0.68 | 0.96 |
| 10-16 07:53 | +15 | XRP | DOWN | 0.55 | open |  |
| 10-16 07:53 | +10 | XRP | DOWN | 0.55 | 0.68 | 0.96 |
| 10-16 07:53 | +5 | XRP | DOWN | 0.55 | 0.68 | 0.96 |
| 10-16 07:53 | +10 stop | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-16 07:53 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-16 07:53 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-16 07:53 | +10 | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-16 07:53 | +5 | ZEC | UP | 0.62 | 0.70 | 0.45 |
| 10-16 07:53 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 07:53 | +10 stop | BTC | UP | 0.58 | 0.70 | 0.87 |
| 10-16 07:53 | +20 | BTC | UP | 0.58 | 0.78 | 1.69 |
| 10-16 07:53 | +15 | BTC | UP | 0.58 | 0.74 | 1.28 |
| 10-16 07:53 | +10 | BTC | UP | 0.58 | 0.70 | 0.87 |
| 10-16 07:53 | +5 | BTC | UP | 0.58 | 0.70 | 0.87 |
| 10-16 07:52 | +10 stop | DOGE | DOWN | 0.47 | 0.57 | 0.64 |
