# Range-Scalp Bot

*Updated Fri Oct 16 16:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19520 | 16960 | 2560 (29) | 1 | $-5899.91 | -4.8% |
| **+10¢** | 14717 | 11760 | 2957 (41) | 1 | $-5304.54 | -5.7% |
| **+15¢** | 12317 | 9137 | 3180 (60) | 0 | $-4795.19 | -6.2% |
| **+20¢** | 10929 | 7597 | 3332 (79) | 0 | $-4256.71 | -6.2% |
| **+10¢ (15¢ stop)** | 24014 | 23964 | 50 (29) | 0 | $-9200.94 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 16:41 | +10 stop | NEAR | DOWN | 0.56 | 0.83 | 2.42 |
| 10-16 16:41 | +10 stop | SOL | DOWN | 0.50 | 0.64 | 1.05 |
| 10-16 16:40 | +10 stop | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-16 16:39 | +10 stop | DOGE | UP | 0.55 | 0.66 | 0.76 |
| 10-16 16:39 | +10 stop | BNB | UP | 0.61 | 0.37 | -2.74 |
| 10-16 16:37 | +10 stop | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-16 16:37 | +10 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-16 16:37 | +5 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-16 16:37 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.05 |
| 10-16 16:37 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-16 16:37 | +15 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-16 16:37 | +10 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-16 16:37 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.48 |
| 10-16 16:37 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 10-16 16:37 | +10 | NEAR | UP | 0.64 | open |  |
| 10-16 16:37 | +5 | NEAR | UP | 0.64 | open |  |
| 10-16 16:37 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-16 16:37 | +10 stop | DOGE | DOWN | 0.66 | 0.33 | -3.62 |
| 10-16 16:37 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-16 16:37 | +10 | DOGE | DOWN | 0.66 | 0.83 | 1.45 |
| 10-16 16:37 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.52 |
| 10-16 16:37 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-16 16:37 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-16 16:37 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-16 16:36 | +10 stop | NEAR | DOWN | 0.35 | 0.56 | 1.76 |
| 10-16 16:36 | +10 | NEAR | DOWN | 0.35 | 0.56 | 1.76 |
| 10-16 16:36 | +5 | NEAR | DOWN | 0.35 | 0.56 | 1.76 |
| 10-16 16:36 | +10 stop | ZEC | UP | 0.57 | 0.71 | 1.04 |
| 10-16 16:36 | +10 | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 10-16 16:36 | +5 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 10-16 16:34 | +10 stop | HYPE | DOWN | 0.59 | 0.77 | 1.46 |
| 10-16 16:34 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.90 |
| 10-16 16:34 | +10 stop | SOL | DOWN | 0.64 | 0.40 | -2.74 |
| 10-16 16:34 | +10 stop | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-16 16:34 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-16 16:34 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-16 16:33 | +10 stop | HYPE | UP | 0.64 | 0.46 | -2.15 |
| 10-16 16:33 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 10-16 16:33 | +10 stop | XRP | UP | 0.49 | 0.34 | -1.84 |
| 10-16 16:33 | +10 stop | BNB | UP | 0.59 | 0.42 | -2.05 |
