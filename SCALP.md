# Range-Scalp Bot

*Updated Fri Oct 30 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40730 | 35547 | 5183 (51) | 5 | $-11399.96 | -4.4% |
| **+10¢** | 30344 | 24351 | 5993 (74) | 8 | $-10157.51 | -5.3% |
| **+15¢** | 25369 | 18917 | 6452 (101) | 8 | $-9190.88 | -5.8% |
| **+20¢** | 22517 | 15754 | 6763 (131) | 7 | $-8114.53 | -5.7% |
| **+10¢ (15¢ stop)** | 49668 | 49598 | 70 (37) | 0 | $-18790.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 12:12 | +10 stop | XRP | UP | 0.53 | 0.14 | -4.17 |
| 10-30 12:12 | +10 | XRP | UP | 0.51 | 0.70 | 1.57 |
| 10-30 12:12 | +5 | XRP | UP | 0.51 | 0.70 | 1.57 |
| 10-30 12:11 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-30 12:11 | +20 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 10-30 12:11 | +15 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 10-30 12:11 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-30 12:11 | +5 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-30 12:10 | +10 stop | HYPE | UP | 0.68 | 0.86 | 1.55 |
| 10-30 12:10 | +5 | HYPE | UP | 0.68 | 0.86 | 1.55 |
| 10-30 12:09 | +5 | ETH | DOWN | 0.47 | 0.54 | 0.34 |
| 10-30 12:09 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-30 12:09 | +5 | DOGE | UP | 0.55 | 0.63 | 0.45 |
| 10-30 12:09 | +10 stop | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 10-30 12:07 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-30 12:07 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-30 12:07 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-30 12:07 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.15 |
| 10-30 12:07 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-30 12:07 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-30 12:07 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-30 12:07 | +5 | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 10-30 12:07 | +10 stop | BNB | UP | 0.60 | 0.84 | 2.09 |
| 10-30 12:06 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-30 12:05 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-30 12:05 | +5 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 12:05 | +10 stop | ETH | DOWN | 0.61 | 0.34 | -3.03 |
| 10-30 12:05 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-30 12:05 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 10-30 12:05 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-30 12:05 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-30 12:05 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 12:05 | +10 stop | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:05 | +10 | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:05 | +5 | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:04 | +10 stop | DOGE | DOWN | 0.57 | 0.38 | -2.25 |
| 10-30 12:04 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-30 12:04 | +10 stop | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-30 12:04 | +5 | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-30 12:04 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
