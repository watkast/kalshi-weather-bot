# Range-Scalp Bot

*Updated Sat Oct 24 06:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31622 | 27568 | 4054 (40) | 0 | $-9065.10 | -4.6% |
| **+10¢** | 23638 | 18954 | 4684 (58) | 3 | $-8053.94 | -5.4% |
| **+15¢** | 19788 | 14751 | 5037 (81) | 3 | $-7206.22 | -5.8% |
| **+20¢** | 17531 | 12258 | 5273 (103) | 3 | $-6393.84 | -5.8% |
| **+10¢ (15¢ stop)** | 38809 | 38750 | 59 (32) | 2 | $-14846.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 06:45 | +10 stop | ZEC | UP | 0.49 | open |  |
| 10-24 06:45 | +20 | ZEC | UP | 0.49 | open |  |
| 10-24 06:45 | +15 | ZEC | UP | 0.49 | open |  |
| 10-24 06:45 | +10 | ZEC | UP | 0.50 | open |  |
| 10-24 06:45 | +5 | ZEC | UP | 0.50 | 0.55 | 0.14 |
| 10-24 06:45 | +10 stop | DOGE | UP | 0.49 | open |  |
| 10-24 06:45 | +20 | DOGE | UP | 0.49 | open |  |
| 10-24 06:45 | +15 | DOGE | UP | 0.49 | open |  |
| 10-24 06:45 | +10 | DOGE | UP | 0.49 | open |  |
| 10-24 06:45 | +5 | DOGE | UP | 0.49 | 0.57 | 0.44 |
| 10-24 06:45 | +10 stop | SOL | UP | 0.50 | 0.61 | 0.75 |
| 10-24 06:45 | +20 | SOL | UP | 0.49 | open |  |
| 10-24 06:45 | +15 | SOL | UP | 0.51 | open |  |
| 10-24 06:45 | +10 | SOL | UP | 0.52 | open |  |
| 10-24 06:45 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 10-24 06:43 | +10 stop | BTC | UP | 0.62 | 0.24 | -4.10 |
| 10-24 06:43 | +20 | BTC | UP | 0.63 | no | -6.47 |
| 10-24 06:43 | +15 | BTC | UP | 0.63 | no | -6.47 |
| 10-24 06:43 | +10 | BTC | UP | 0.63 | no | -6.47 |
| 10-24 06:43 | +5 | BTC | UP | 0.63 | 0.71 | 0.48 |
| 10-24 06:41 | +10 stop | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 10-24 06:41 | +15 | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 10-24 06:41 | +10 | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 10-24 06:41 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 10-24 06:41 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-24 06:41 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 10-24 06:40 | +10 stop | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 10-24 06:40 | +10 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 10-24 06:40 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-24 06:40 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
| 10-24 06:40 | +5 | BTC | UP | 0.44 | 0.60 | 1.25 |
| 10-24 06:39 | +10 stop | ZEC | UP | 0.67 | 0.44 | -2.64 |
| 10-24 06:39 | +10 stop | BTC | UP | 0.60 | 0.43 | -2.05 |
| 10-24 06:39 | +10 stop | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-24 06:39 | +10 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-24 06:39 | +5 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-24 06:39 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 10-24 06:39 | +5 | BNB | UP | 0.63 | 0.75 | 0.89 |
| 10-24 06:38 | +10 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 10-24 06:38 | +10 stop | ZEC | DOWN | 0.66 | 0.34 | -3.52 |
