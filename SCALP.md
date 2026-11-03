# Range-Scalp Bot

*Updated Tue Nov 03 21:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46368 | 40372 | 5996 (72) | 1 | $-13361.46 | -4.6% |
| **+10¢** | 34615 | 27668 | 6947 (96) | 1 | $-12217.82 | -5.6% |
| **+15¢** | 28977 | 21506 | 7471 (124) | 2 | $-11164.68 | -6.1% |
| **+20¢** | 25740 | 17910 | 7830 (164) | 5 | $-9882.54 | -6.1% |
| **+10¢ (15¢ stop)** | 56555 | 56462 | 93 (56) | 1 | $-21203.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 21:32 | +5 | XRP | UP | 0.68 | 0.75 | 0.45 |
| 11-03 21:32 | +5 | HYPE | UP | 0.60 | 0.74 | 1.05 |
| 11-03 21:32 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-03 21:32 | +10 | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-03 21:32 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 11-03 21:32 | +10 stop | ETH | UP | 0.52 | 0.63 | 0.75 |
| 11-03 21:32 | +20 | ETH | UP | 0.52 | 0.77 | 2.19 |
| 11-03 21:32 | +15 | ETH | UP | 0.52 | 0.67 | 1.16 |
| 11-03 21:32 | +10 | ETH | UP | 0.52 | 0.63 | 0.75 |
| 11-03 21:32 | +5 | ETH | UP | 0.52 | 0.59 | 0.35 |
| 11-03 21:32 | +5 | DOGE | UP | 0.67 | 0.73 | 0.30 |
| 11-03 21:32 | +20 | ZEC | UP | 0.68 | open |  |
| 11-03 21:32 | +15 | ZEC | UP | 0.68 | open |  |
| 11-03 21:32 | +10 | ZEC | UP | 0.68 | open |  |
| 11-03 21:32 | +5 | ZEC | UP | 0.68 | open |  |
| 11-03 21:31 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 11-03 21:31 | +20 | DOGE | UP | 0.71 | open |  |
| 11-03 21:31 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 11-03 21:31 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 11-03 21:31 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-03 21:31 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-03 21:31 | +20 | BTC | UP | 0.63 | open |  |
| 11-03 21:31 | +15 | BTC | UP | 0.63 | open |  |
| 11-03 21:31 | +10 | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-03 21:31 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 11-03 21:31 | +10 stop | XRP | UP | 0.60 | 0.75 | 1.19 |
| 11-03 21:31 | +20 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-03 21:31 | +15 | XRP | UP | 0.60 | 0.75 | 1.19 |
| 11-03 21:31 | +10 | XRP | UP | 0.60 | 0.75 | 1.19 |
| 11-03 21:31 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 11-03 21:31 | +10 stop | HYPE | UP | 0.60 | 0.74 | 1.05 |
| 11-03 21:31 | +20 | HYPE | UP | 0.58 | open |  |
| 11-03 21:31 | +15 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 11-03 21:31 | +10 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 11-03 21:31 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
| 11-03 21:31 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-03 21:31 | +20 | NEAR | UP | 0.60 | 0.81 | 1.82 |
| 11-03 21:31 | +15 | NEAR | UP | 0.60 | 0.75 | 1.19 |
| 11-03 21:31 | +10 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-03 21:31 | +5 | NEAR | UP | 0.60 | 0.70 | 0.68 |
