# Range-Scalp Bot

*Updated Sun Oct 11 22:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12619 | 10893 | 1726 (25) | 1 | $-4161.52 | -5.2% |
| **+10¢** | 9574 | 7575 | 1999 (37) | 1 | $-3908.32 | -6.5% |
| **+15¢** | 8060 | 5933 | 2127 (55) | 2 | $-3365.47 | -6.7% |
| **+20¢** | 7185 | 4967 | 2218 (69) | 2 | $-2868.67 | -6.4% |
| **+10¢ (15¢ stop)** | 15539 | 15498 | 41 (25) | 1 | $-6067.97 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 22:46 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.93 |
| 10-11 22:46 | +20 | ZEC | UP | 0.67 | open |  |
| 10-11 22:46 | +15 | ZEC | UP | 0.67 | open |  |
| 10-11 22:46 | +10 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-11 22:46 | +5 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-11 22:46 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-11 22:46 | +20 | BNB | UP | 0.61 | open |  |
| 10-11 22:46 | +15 | BNB | UP | 0.61 | open |  |
| 10-11 22:46 | +10 | BNB | UP | 0.61 | open |  |
| 10-11 22:46 | +5 | BNB | UP | 0.61 | open |  |
| 10-11 22:43 | +10 stop | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-11 22:43 | +15 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-11 22:43 | +10 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-11 22:43 | +5 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-11 22:41 | +10 stop | SOL | UP | 0.63 | 0.88 | 2.25 |
| 10-11 22:41 | +10 stop | ETH | DOWN | 0.57 | 0.27 | -3.32 |
| 10-11 22:40 | +10 stop | ETH | DOWN | 0.69 | 0.54 | -1.83 |
| 10-11 22:40 | +10 stop | SOL | UP | 0.57 | 0.68 | 0.74 |
| 10-11 22:40 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 22:38 | +10 stop | XRP | UP | 0.58 | 0.40 | -2.16 |
| 10-11 22:38 | +10 stop | BTC | UP | 0.70 | 0.54 | -1.93 |
| 10-11 22:38 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 10-11 22:36 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 10-11 22:36 | +20 | ZEC | UP | 0.66 | 0.88 | 1.96 |
| 10-11 22:36 | +15 | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 10-11 22:36 | +10 | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 10-11 22:36 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 10-11 22:36 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.73 |
| 10-11 22:36 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-11 22:36 | +10 stop | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 10-11 22:35 | +10 stop | NEAR | UP | 0.66 | 0.83 | 1.44 |
| 10-11 22:35 | +10 | NEAR | UP | 0.66 | 0.83 | 1.44 |
| 10-11 22:35 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 10-11 22:34 | +5 | HYPE | UP | 0.69 | 0.80 | 0.79 |
| 10-11 22:34 | +10 stop | DOGE | UP | 0.69 | 0.52 | -2.03 |
| 10-11 22:34 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 10-11 22:34 | +10 stop | BTC | UP | 0.63 | 0.78 | 1.20 |
| 10-11 22:33 | +10 stop | HYPE | UP | 0.62 | 0.80 | 1.51 |
| 10-11 22:33 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 10-11 22:33 | +5 | SOL | DOWN | 0.58 | yes | -5.98 |
