# Range-Scalp Bot

*Updated Sat Oct 10 18:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10758 | 9273 | 1485 (22) | 2 | $-3680.66 | -5.4% |
| **+10¢** | 8146 | 6416 | 1730 (36) | 2 | $-3514.62 | -6.8% |
| **+15¢** | 6870 | 5040 | 1830 (52) | 3 | $-2967.86 | -6.9% |
| **+20¢** | 6108 | 4201 | 1907 (66) | 3 | $-2534.06 | -6.6% |
| **+10¢ (15¢ stop)** | 13233 | 13192 | 41 (25) | 0 | $-5293.43 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 18:58 | +10 stop | SOL | UP | 0.64 | 0.09 | -5.71 |
| 10-10 18:57 | +10 stop | BNB | UP | 0.69 | 0.46 | -2.63 |
| 10-10 18:57 | +10 stop | SOL | DOWN | 0.70 | 0.50 | -2.33 |
| 10-10 18:56 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-10 18:56 | +10 stop | BTC | DOWN | 0.62 | 0.46 | -1.95 |
| 10-10 18:56 | +10 stop | DOGE | DOWN | 0.60 | 0.41 | -2.24 |
| 10-10 18:56 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-10 18:55 | +10 stop | BNB | DOWN | 0.54 | 0.37 | -2.05 |
| 10-10 18:55 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 10-10 18:54 | +10 stop | DOGE | UP | 0.56 | 0.38 | -2.12 |
| 10-10 18:54 | +10 stop | BNB | UP | 0.64 | 0.45 | -2.25 |
| 10-10 18:53 | +10 stop | SOL | UP | 0.60 | 0.30 | -3.32 |
| 10-10 18:53 | +10 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-10 18:53 | +5 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-10 18:53 | +10 stop | DOGE | UP | 0.69 | 0.52 | -2.03 |
| 10-10 18:53 | +15 | DOGE | UP | 0.69 | 0.90 | 1.90 |
| 10-10 18:53 | +10 | DOGE | UP | 0.69 | 0.90 | 1.90 |
| 10-10 18:53 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 10-10 18:53 | +10 stop | NEAR | UP | 0.69 | 0.90 | 1.89 |
| 10-10 18:52 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 10-10 18:52 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-10 18:51 | +10 stop | HYPE | UP | 0.68 | 0.53 | -1.88 |
| 10-10 18:50 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-10 18:50 | +15 | SOL | UP | 0.64 | open |  |
| 10-10 18:50 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-10 18:50 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 10-10 18:50 | +5 | BTC | UP | 0.56 | 0.67 | 0.76 |
| 10-10 18:50 | +10 stop | NEAR | UP | 0.53 | 0.64 | 0.75 |
| 10-10 18:50 | +10 stop | DOGE | UP | 0.62 | 0.85 | 2.04 |
| 10-10 18:50 | +15 | DOGE | UP | 0.62 | 0.85 | 2.04 |
| 10-10 18:50 | +10 | DOGE | UP | 0.62 | 0.85 | 2.04 |
| 10-10 18:50 | +5 | DOGE | UP | 0.62 | 0.69 | 0.38 |
| 10-10 18:47 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-10 18:47 | +10 stop | BTC | UP | 0.64 | 0.42 | -2.55 |
| 10-10 18:47 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-10 18:46 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-10 18:46 | +20 | SOL | UP | 0.67 | open |  |
| 10-10 18:46 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-10 18:46 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-10 18:46 | +5 | SOL | UP | 0.67 | 0.79 | 0.92 |
