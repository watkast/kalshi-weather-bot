# Range-Scalp Bot

*Updated Sun Oct 11 11:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11874 | 10244 | 1630 (24) | 2 | $-3968.62 | -5.3% |
| **+10¢** | 9007 | 7110 | 1897 (37) | 2 | $-3789.60 | -6.7% |
| **+15¢** | 7588 | 5577 | 2011 (54) | 2 | $-3227.04 | -6.8% |
| **+20¢** | 6763 | 4672 | 2091 (67) | 2 | $-2697.55 | -6.4% |
| **+10¢ (15¢ stop)** | 14611 | 14570 | 41 (25) | 1 | $-5773.03 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 11:41 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-11 11:40 | +10 stop | NEAR | UP | 0.41 | 0.57 | 1.25 |
| 10-11 11:39 | +10 stop | NEAR | DOWN | 0.68 | 0.44 | -2.74 |
| 10-11 11:39 | +10 stop | BNB | UP | 0.58 | 0.76 | 1.49 |
| 10-11 11:39 | +10 | BNB | UP | 0.58 | 0.76 | 1.49 |
| 10-11 11:39 | +5 | BNB | UP | 0.58 | 0.67 | 0.56 |
| 10-11 11:38 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.89 |
| 10-11 11:36 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 10-11 11:35 | +10 stop | ZEC | DOWN | 0.51 | 0.66 | 1.16 |
| 10-11 11:35 | +10 stop | BNB | UP | 0.65 | 0.76 | 0.81 |
| 10-11 11:35 | +20 | BNB | UP | 0.65 | 0.91 | 2.34 |
| 10-11 11:35 | +15 | BNB | UP | 0.65 | 0.80 | 1.22 |
| 10-11 11:35 | +10 | BNB | UP | 0.65 | 0.76 | 0.81 |
| 10-11 11:35 | +5 | BNB | UP | 0.65 | 0.76 | 0.81 |
| 10-11 11:34 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 10-11 11:34 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.73 |
| 10-11 11:33 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-11 11:33 | +10 stop | XRP | UP | 0.51 | 0.73 | 1.85 |
| 10-11 11:33 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-11 11:33 | +10 stop | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-11 11:33 | +10 stop | XRP | DOWN | 0.44 | 0.55 | 0.74 |
| 10-11 11:33 | +10 stop | BNB | DOWN | 0.40 | 0.61 | 1.72 |
| 10-11 11:33 | +10 stop | ZEC | UP | 0.53 | 0.34 | -2.24 |
| 10-11 11:33 | +20 | ZEC | UP | 0.53 | 0.81 | 2.51 |
| 10-11 11:33 | +15 | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 10-11 11:33 | +10 | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 10-11 11:33 | +5 | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 10-11 11:32 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.81 |
| 10-11 11:32 | +10 stop | SOL | UP | 0.59 | 0.72 | 0.98 |
| 10-11 11:32 | +20 | SOL | UP | 0.59 | 0.88 | 2.65 |
| 10-11 11:32 | +15 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-11 11:32 | +10 | SOL | UP | 0.59 | 0.72 | 0.98 |
| 10-11 11:32 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 10-11 11:32 | +10 stop | DOGE | UP | 0.64 | 0.45 | -2.25 |
| 10-11 11:32 | +20 | DOGE | UP | 0.64 | 0.88 | 2.15 |
| 10-11 11:32 | +15 | DOGE | UP | 0.64 | 0.88 | 2.15 |
| 10-11 11:32 | +10 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-11 11:32 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 10-11 11:31 | +5 | XRP | UP | 0.63 | 0.73 | 0.69 |
| 10-11 11:31 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
