# Range-Scalp Bot

*Updated Sat Oct 03 09:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 538 | 460 | 78 (1) | 7 | $-211.43 | -6.2% |
| **+10¢** | 414 | 328 | 86 (2) | 6 | $-171.81 | -6.5% |
| **+15¢** | 351 | 259 | 92 (3) | 6 | $-160.62 | -7.2% |
| **+20¢** | 303 | 208 | 95 (3) | 8 | $-158.26 | -8.2% |
| **+10¢ (15¢ stop)** | 710 | 709 | 1 (1) | 4 | $-376.42 | -8.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 09:37 | +10 stop | DOGE | UP | 0.67 | open |  |
| 10-03 09:37 | +10 | DOGE | UP | 0.67 | open |  |
| 10-03 09:37 | +5 | DOGE | UP | 0.67 | open |  |
| 10-03 09:37 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-03 09:37 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 10-03 09:37 | +10 stop | XRP | UP | 0.60 | open |  |
| 10-03 09:36 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-03 09:36 | +10 stop | XRP | UP | 0.51 | 0.61 | 0.65 |
| 10-03 09:36 | +10 stop | ZEC | DOWN | 0.51 | 0.35 | -1.89 |
| 10-03 09:36 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 10-03 09:36 | +10 stop | SOL | UP | 0.69 | 0.82 | 1.04 |
| 10-03 09:36 | +10 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 10-03 09:36 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-03 09:35 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.87 |
| 10-03 09:35 | +20 | ETH | DOWN | 0.59 | 0.84 | 2.22 |
| 10-03 09:35 | +15 | ETH | DOWN | 0.59 | 0.84 | 2.22 |
| 10-03 09:35 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.87 |
| 10-03 09:35 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.26 |
| 10-03 09:34 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 10-03 09:34 | +5 | XRP | UP | 0.67 | open |  |
| 10-03 09:34 | +10 stop | HYPE | UP | 0.67 | 0.46 | -2.44 |
| 10-03 09:34 | +10 | HYPE | UP | 0.67 | open |  |
| 10-03 09:34 | +5 | HYPE | UP | 0.67 | open |  |
| 10-03 09:34 | +10 stop | ZEC | UP | 0.68 | 0.53 | -1.84 |
| 10-03 09:34 | +20 | ZEC | UP | 0.68 | open |  |
| 10-03 09:34 | +15 | ZEC | UP | 0.68 | open |  |
| 10-03 09:34 | +10 | ZEC | UP | 0.68 | open |  |
| 10-03 09:34 | +5 | ZEC | UP | 0.68 | open |  |
| 10-03 09:33 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-03 09:33 | +20 | BTC | DOWN | 0.54 | open |  |
| 10-03 09:33 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-03 09:33 | +10 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-03 09:33 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-03 09:33 | +5 | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-03 09:33 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-03 09:33 | +20 | DOGE | UP | 0.68 | open |  |
| 10-03 09:33 | +15 | DOGE | UP | 0.68 | open |  |
| 10-03 09:33 | +10 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-03 09:33 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 10-03 09:32 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
