# Range-Scalp Bot

*Updated Fri Nov 06 00:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48918 | 42625 | 6293 (75) | 2 | $-13899.09 | -4.5% |
| **+10¢** | 36516 | 29199 | 7317 (101) | 3 | $-12780.07 | -5.6% |
| **+15¢** | 30588 | 22708 | 7880 (130) | 3 | $-11662.69 | -6.1% |
| **+20¢** | 27179 | 18920 | 8259 (170) | 5 | $-10331.57 | -6.1% |
| **+10¢ (15¢ stop)** | 59642 | 59547 | 95 (57) | 3 | $-22099.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 00:18 | +5 | ZEC | UP | 0.71 | open |  |
| 11-06 00:18 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-06 00:18 | +20 | BTC | UP | 0.69 | open |  |
| 11-06 00:18 | +15 | BTC | UP | 0.69 | open |  |
| 11-06 00:18 | +10 | BTC | UP | 0.69 | open |  |
| 11-06 00:18 | +5 | BTC | UP | 0.69 | open |  |
| 11-06 00:16 | +10 stop | ETH | UP | 0.66 | open |  |
| 11-06 00:16 | +20 | ETH | UP | 0.67 | open |  |
| 11-06 00:16 | +15 | ETH | UP | 0.66 | open |  |
| 11-06 00:16 | +10 | ETH | UP | 0.66 | open |  |
| 11-06 00:16 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 11-06 00:16 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-06 00:16 | +20 | ZEC | UP | 0.71 | open |  |
| 11-06 00:16 | +15 | ZEC | UP | 0.71 | open |  |
| 11-06 00:16 | +10 | ZEC | UP | 0.71 | open |  |
| 11-06 00:16 | +5 | ZEC | UP | 0.70 | 0.75 | 0.21 |
| 11-06 00:16 | +10 stop | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-06 00:16 | +20 | DOGE | UP | 0.68 | open |  |
| 11-06 00:16 | +15 | DOGE | UP | 0.68 | 0.83 | 1.24 |
| 11-06 00:16 | +10 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-06 00:16 | +5 | DOGE | UP | 0.68 | 0.75 | 0.40 |
| 11-06 00:15 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-06 00:15 | +20 | HYPE | UP | 0.68 | open |  |
| 11-06 00:15 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-06 00:15 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-06 00:15 | +5 | HYPE | UP | 0.67 | 0.75 | 0.50 |
| 11-06 00:08 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-06 00:08 | +10 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-06 00:07 | +5 | ETH | UP | 0.64 | 0.70 | 0.28 |
| 11-06 00:06 | +10 stop | BTC | UP | 0.71 | 0.88 | 1.47 |
| 11-06 00:06 | +20 | BTC | UP | 0.71 | 0.91 | 1.83 |
| 11-06 00:06 | +15 | BTC | UP | 0.71 | 0.88 | 1.47 |
| 11-06 00:06 | +10 | BTC | UP | 0.71 | 0.88 | 1.47 |
| 11-06 00:06 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 11-06 00:06 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-06 00:06 | +15 | ETH | UP | 0.57 | 0.79 | 1.90 |
| 11-06 00:06 | +10 | ETH | UP | 0.57 | 0.68 | 0.76 |
| 11-06 00:06 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 11-06 00:02 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-06 00:02 | +20 | BTC | UP | 0.63 | 0.84 | 1.83 |
