# Range-Scalp Bot

*Updated Mon Oct 19 19:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24434 | 21264 | 3170 (31) | 0 | $-7174.01 | -4.7% |
| **+10¢** | 18369 | 14708 | 3661 (46) | 0 | $-6402.25 | -5.5% |
| **+15¢** | 15381 | 11439 | 3942 (69) | 0 | $-5776.44 | -6.0% |
| **+20¢** | 13611 | 9484 | 4127 (87) | 0 | $-5176.73 | -6.1% |
| **+10¢ (15¢ stop)** | 30040 | 29988 | 52 (30) | 0 | $-11366.41 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 19:13 | +10 stop | DOGE | DOWN | 0.69 | 0.94 | 2.25 |
| 10-19 19:13 | +20 | DOGE | DOWN | 0.69 | 0.94 | 2.25 |
| 10-19 19:13 | +15 | DOGE | DOWN | 0.69 | 0.94 | 2.25 |
| 10-19 19:13 | +10 | DOGE | DOWN | 0.69 | 0.94 | 2.25 |
| 10-19 19:13 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-19 19:07 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-19 19:06 | +10 stop | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-19 19:06 | +5 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 19:05 | +10 stop | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 10-19 19:05 | +10 stop | BTC | DOWN | 0.57 | 0.77 | 1.69 |
| 10-19 19:05 | +10 stop | NEAR | DOWN | 0.54 | 0.71 | 1.37 |
| 10-19 19:05 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-19 19:05 | +10 stop | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-19 19:05 | +20 | ZEC | DOWN | 0.60 | 0.84 | 2.13 |
| 10-19 19:05 | +15 | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-19 19:05 | +10 | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-19 19:05 | +5 | ZEC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-19 19:05 | +10 stop | DOGE | UP | 0.65 | 0.48 | -2.04 |
| 10-19 19:04 | +10 stop | DOGE | UP | 0.53 | 0.67 | 1.06 |
| 10-19 19:04 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 10-19 19:04 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-19 19:04 | +15 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 10-19 19:04 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-19 19:04 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 10-19 19:04 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.94 |
| 10-19 19:04 | +10 | NEAR | DOWN | 0.68 | 0.86 | 1.55 |
| 10-19 19:04 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 10-19 19:04 | +10 stop | BNB | DOWN | 0.64 | 0.46 | -2.19 |
| 10-19 19:04 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-19 19:04 | +10 | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 10-19 19:04 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 19:03 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 10-19 19:03 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-19 19:03 | +15 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-19 19:03 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 19:03 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 19:02 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 10-19 19:02 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 19:02 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 10-19 19:02 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
