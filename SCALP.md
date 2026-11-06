# Range-Scalp Bot

*Updated Fri Nov 06 04:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49201 | 42873 | 6328 (75) | 2 | $-13946.87 | -4.5% |
| **+10¢** | 36739 | 29384 | 7355 (101) | 3 | $-12790.48 | -5.5% |
| **+15¢** | 30770 | 22852 | 7918 (130) | 6 | $-11657.20 | -6.0% |
| **+20¢** | 27350 | 19051 | 8299 (170) | 8 | $-10306.18 | -6.0% |
| **+10¢ (15¢ stop)** | 59997 | 59902 | 95 (57) | 1 | $-22219.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 04:53 | +10 stop | BTC | DOWN | 0.52 | 0.25 | -3.02 |
| 11-06 04:53 | +10 stop | XRP | DOWN | 0.48 | 0.30 | -2.18 |
| 11-06 04:53 | +20 | XRP | DOWN | 0.48 | open |  |
| 11-06 04:53 | +15 | XRP | DOWN | 0.48 | open |  |
| 11-06 04:53 | +10 | XRP | DOWN | 0.48 | open |  |
| 11-06 04:53 | +5 | XRP | DOWN | 0.48 | 0.55 | 0.29 |
| 11-06 04:53 | +10 stop | ZEC | DOWN | 0.49 | open |  |
| 11-06 04:53 | +5 | ZEC | DOWN | 0.48 | 0.56 | 0.44 |
| 11-06 04:52 | +10 stop | HYPE | UP | 0.71 | 0.50 | -2.43 |
| 11-06 04:52 | +15 | HYPE | UP | 0.71 | open |  |
| 11-06 04:52 | +10 | HYPE | UP | 0.71 | 0.85 | 1.16 |
| 11-06 04:52 | +5 | HYPE | UP | 0.71 | 0.85 | 1.16 |
| 11-06 04:52 | +10 stop | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-06 04:52 | +20 | SOL | UP | 0.65 | open |  |
| 11-06 04:52 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-06 04:52 | +10 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-06 04:52 | +5 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-06 04:52 | +10 stop | NEAR | UP | 0.67 | 0.50 | -2.04 |
| 11-06 04:52 | +20 | NEAR | UP | 0.67 | open |  |
| 11-06 04:52 | +15 | NEAR | UP | 0.67 | open |  |
| 11-06 04:52 | +10 | NEAR | UP | 0.67 | open |  |
| 11-06 04:52 | +5 | NEAR | UP | 0.67 | open |  |
| 11-06 04:52 | +10 stop | BTC | DOWN | 0.51 | 0.65 | 1.06 |
| 11-06 04:51 | +5 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-06 04:50 | +5 | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-06 04:50 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 11-06 04:47 | +5 | BTC | UP | 0.71 | open |  |
| 11-06 04:46 | +10 stop | BTC | UP | 0.64 | 0.49 | -1.85 |
| 11-06 04:46 | +20 | BTC | UP | 0.64 | open |  |
| 11-06 04:46 | +15 | BTC | UP | 0.64 | open |  |
| 11-06 04:46 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-06 04:46 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-06 04:46 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-06 04:46 | +20 | SOL | UP | 0.61 | 0.82 | 1.82 |
| 11-06 04:46 | +15 | SOL | UP | 0.61 | 0.79 | 1.51 |
| 11-06 04:46 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-06 04:46 | +5 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-06 04:46 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-06 04:46 | +20 | DOGE | UP | 0.65 | 0.86 | 1.85 |
| 11-06 04:46 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
