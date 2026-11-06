# Range-Scalp Bot

*Updated Fri Nov 06 22:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50052 | 43634 | 6418 (76) | 7 | $-14035.12 | -4.5% |
| **+10¢** | 37354 | 29886 | 7468 (102) | 8 | $-12934.44 | -5.5% |
| **+15¢** | 31284 | 23234 | 8050 (131) | 8 | $-11858.91 | -6.0% |
| **+20¢** | 27812 | 19372 | 8440 (172) | 8 | $-10488.49 | -6.0% |
| **+10¢ (15¢ stop)** | 60969 | 60870 | 99 (58) | 5 | $-22584.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 22:26 | +10 stop | HYPE | UP | 0.68 | open |  |
| 11-06 22:26 | +10 stop | BTC | UP | 0.64 | open |  |
| 11-06 22:24 | +10 stop | ETH | UP | 0.59 | 0.38 | -2.44 |
| 11-06 22:22 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-06 22:22 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-06 22:22 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 11-06 22:21 | +5 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 11-06 22:21 | +10 stop | BNB | UP | 0.55 | open |  |
| 11-06 22:20 | +10 stop | ZEC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-06 22:20 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 22:20 | +10 stop | ETH | UP | 0.61 | 0.42 | -2.25 |
| 11-06 22:19 | +10 stop | BNB | UP | 0.71 | 0.53 | -2.13 |
| 11-06 22:19 | +10 | BNB | UP | 0.71 | open |  |
| 11-06 22:19 | +5 | BNB | UP | 0.71 | open |  |
| 11-06 22:19 | +5 | HYPE | UP | 0.70 | open |  |
| 11-06 22:19 | +10 stop | SOL | UP | 0.67 | 0.50 | -2.04 |
| 11-06 22:19 | +15 | SOL | UP | 0.67 | open |  |
| 11-06 22:19 | +10 | SOL | UP | 0.66 | open |  |
| 11-06 22:19 | +5 | SOL | UP | 0.66 | open |  |
| 11-06 22:19 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 11-06 22:19 | +10 stop | ZEC | UP | 0.61 | 0.34 | -3.03 |
| 11-06 22:19 | +10 | ZEC | UP | 0.61 | open |  |
| 11-06 22:19 | +10 stop | DOGE | UP | 0.62 | 0.47 | -1.85 |
| 11-06 22:19 | +10 | DOGE | UP | 0.62 | open |  |
| 11-06 22:19 | +5 | DOGE | UP | 0.62 | open |  |
| 11-06 22:19 | +5 | NEAR | UP | 0.54 | open |  |
| 11-06 22:18 | +5 | ZEC | UP | 0.62 | open |  |
| 11-06 22:17 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-06 22:17 | +10 stop | BNB | UP | 0.58 | 0.72 | 1.07 |
| 11-06 22:17 | +20 | BNB | UP | 0.58 | open |  |
| 11-06 22:17 | +15 | BNB | UP | 0.58 | open |  |
| 11-06 22:17 | +10 | BNB | UP | 0.58 | 0.72 | 1.07 |
| 11-06 22:17 | +5 | BNB | UP | 0.58 | 0.66 | 0.42 |
| 11-06 22:17 | +10 stop | ZEC | UP | 0.53 | 0.64 | 0.75 |
| 11-06 22:17 | +20 | ZEC | UP | 0.53 | open |  |
| 11-06 22:17 | +15 | ZEC | UP | 0.53 | open |  |
| 11-06 22:17 | +10 | ZEC | UP | 0.53 | 0.64 | 0.75 |
| 11-06 22:17 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 11-06 22:17 | +10 stop | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 11-06 22:17 | +20 | DOGE | UP | 0.55 | open |  |
