# Range-Scalp Bot

*Updated Fri Nov 06 16:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49722 | 43341 | 6381 (76) | 1 | $-13970.60 | -4.5% |
| **+10¢** | 37117 | 29695 | 7422 (101) | 1 | $-12858.66 | -5.5% |
| **+15¢** | 31088 | 23092 | 7996 (130) | 1 | $-11752.81 | -6.0% |
| **+20¢** | 27637 | 19253 | 8384 (171) | 1 | $-10397.28 | -6.0% |
| **+10¢ (15¢ stop)** | 60593 | 60496 | 97 (57) | 0 | $-22432.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 16:22 | +10 | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-06 16:22 | +5 | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-06 16:22 | +5 | BTC | UP | 0.57 | 0.64 | 0.35 |
| 11-06 16:22 | +10 stop | BNB | UP | 0.70 | 0.52 | -2.13 |
| 11-06 16:21 | +10 stop | BTC | UP | 0.71 | 0.86 | 1.26 |
| 11-06 16:21 | +10 stop | ETH | UP | 0.70 | 0.85 | 1.26 |
| 11-06 16:21 | +10 stop | ETH | DOWN | 0.48 | 0.67 | 1.56 |
| 11-06 16:20 | +10 stop | SOL | UP | 0.64 | 0.47 | -2.05 |
| 11-06 16:19 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-06 16:19 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-06 16:18 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 11-06 16:18 | +10 stop | NEAR | DOWN | 0.46 | 0.29 | -2.04 |
| 11-06 16:18 | +10 stop | DOGE | DOWN | 0.58 | 0.41 | -2.05 |
| 11-06 16:18 | +10 stop | XRP | DOWN | 0.52 | 0.37 | -1.85 |
| 11-06 16:18 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-06 16:18 | +5 | HYPE | UP | 0.63 | 0.70 | 0.38 |
| 11-06 16:18 | +10 stop | BNB | DOWN | 0.66 | 0.46 | -2.34 |
| 11-06 16:18 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.43 |
| 11-06 16:18 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-06 16:18 | +15 | SOL | DOWN | 0.69 | open |  |
| 11-06 16:18 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-06 16:18 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-06 16:17 | +10 stop | NEAR | UP | 0.62 | 0.45 | -2.05 |
| 11-06 16:17 | +20 | NEAR | UP | 0.62 | 0.84 | 1.93 |
| 11-06 16:17 | +15 | NEAR | UP | 0.62 | 0.80 | 1.51 |
| 11-06 16:17 | +10 | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 11-06 16:17 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 11-06 16:15 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-06 16:15 | +20 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 11-06 16:15 | +15 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 11-06 16:15 | +10 | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-06 16:15 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-06 16:15 | +10 stop | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 11-06 16:15 | +20 | HYPE | UP | 0.63 | 0.85 | 1.94 |
| 11-06 16:15 | +15 | HYPE | UP | 0.63 | 0.78 | 1.20 |
| 11-06 16:15 | +10 | HYPE | UP | 0.62 | 0.75 | 0.99 |
| 11-06 16:15 | +5 | HYPE | UP | 0.62 | 0.69 | 0.38 |
| 11-06 16:15 | +10 stop | ETH | UP | 0.61 | 0.33 | -3.13 |
| 11-06 16:15 | +20 | ETH | UP | 0.61 | 0.85 | 2.14 |
| 11-06 16:15 | +15 | ETH | UP | 0.61 | 0.76 | 1.20 |
