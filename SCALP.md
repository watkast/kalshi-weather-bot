# Range-Scalp Bot

*Updated Tue Oct 06 20:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5466 | 4740 | 726 (7) | 4 | $-1673.16 | -4.9% |
| **+10¢** | 4172 | 3319 | 853 (12) | 5 | $-1590.58 | -6.1% |
| **+15¢** | 3493 | 2592 | 901 (15) | 7 | $-1380.65 | -6.3% |
| **+20¢** | 3124 | 2188 | 936 (22) | 7 | $-1095.02 | -5.6% |
| **+10¢ (15¢ stop)** | 6670 | 6655 | 15 (9) | 0 | $-2398.40 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 20:55 | +10 stop | DOGE | DOWN | 0.63 | 0.86 | 2.04 |
| 10-06 20:55 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-06 20:54 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-06 20:54 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-06 20:54 | +10 stop | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 20:54 | +10 | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 20:54 | +5 | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 20:53 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 10-06 20:53 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-06 20:53 | +10 stop | ZEC | DOWN | 0.71 | 0.50 | -2.43 |
| 10-06 20:53 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-06 20:53 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 20:53 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-06 20:53 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 20:53 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-06 20:52 | +10 stop | ETH | UP | 0.70 | 0.49 | -2.43 |
| 10-06 20:52 | +10 | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-06 20:52 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.38 |
| 10-06 20:52 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-06 20:52 | +10 stop | HYPE | DOWN | 0.64 | 0.39 | -2.84 |
| 10-06 20:52 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-06 20:52 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-06 20:52 | +10 | HYPE | DOWN | 0.64 | open |  |
| 10-06 20:52 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-06 20:51 | +10 stop | ZEC | DOWN | 0.69 | 0.53 | -1.93 |
| 10-06 20:51 | +10 stop | NEAR | DOWN | 0.52 | 0.69 | 1.37 |
| 10-06 20:51 | +10 | NEAR | DOWN | 0.52 | 0.69 | 1.37 |
| 10-06 20:51 | +5 | NEAR | DOWN | 0.52 | 0.58 | 0.24 |
| 10-06 20:50 | +10 stop | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 10-06 20:50 | +10 | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 10-06 20:50 | +10 stop | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 10-06 20:49 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-06 20:49 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-06 20:49 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-06 20:49 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-06 20:49 | +15 | SOL | UP | 0.50 | 0.66 | 1.26 |
| 10-06 20:49 | +10 stop | BTC | UP | 0.50 | 0.31 | -2.23 |
| 10-06 20:49 | +10 | BTC | UP | 0.50 | open |  |
| 10-06 20:49 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.39 |
| 10-06 20:48 | +10 stop | ZEC | UP | 0.66 | 0.45 | -2.44 |
