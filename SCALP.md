# Range-Scalp Bot

*Updated Thu Oct 22 16:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28976 | 25232 | 3744 (39) | 5 | $-8462.42 | -4.6% |
| **+10¢** | 21740 | 17410 | 4330 (55) | 7 | $-7563.77 | -5.5% |
| **+15¢** | 18195 | 13541 | 4654 (78) | 9 | $-6777.74 | -5.9% |
| **+20¢** | 16103 | 11225 | 4878 (100) | 9 | $-6112.31 | -6.0% |
| **+10¢ (15¢ stop)** | 35555 | 35496 | 59 (32) | 3 | $-13369.63 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 16:21 | +10 stop | NEAR | DOWN | 0.52 | 0.65 | 0.96 |
| 10-22 16:20 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-22 16:20 | +15 | BTC | UP | 0.61 | open |  |
| 10-22 16:20 | +10 | BTC | UP | 0.61 | open |  |
| 10-22 16:20 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-22 16:20 | +10 stop | SOL | DOWN | 0.67 | 0.51 | -1.94 |
| 10-22 16:20 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-22 16:20 | +20 | BNB | UP | 0.61 | open |  |
| 10-22 16:20 | +15 | BNB | UP | 0.61 | open |  |
| 10-22 16:20 | +10 | BNB | UP | 0.61 | open |  |
| 10-22 16:20 | +5 | BNB | UP | 0.61 | open |  |
| 10-22 16:20 | +10 stop | ZEC | UP | 0.58 | open |  |
| 10-22 16:20 | +10 | ZEC | UP | 0.58 | open |  |
| 10-22 16:20 | +5 | ZEC | UP | 0.58 | 0.64 | 0.25 |
| 10-22 16:19 | +10 | NEAR | UP | 0.70 | open |  |
| 10-22 16:19 | +5 | NEAR | UP | 0.70 | open |  |
| 10-22 16:19 | +5 | SOL | UP | 0.63 | open |  |
| 10-22 16:17 | +10 stop | SOL | UP | 0.66 | 0.39 | -3.03 |
| 10-22 16:17 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.86 |
| 10-22 16:17 | +20 | HYPE | UP | 0.64 | open |  |
| 10-22 16:17 | +15 | HYPE | UP | 0.64 | open |  |
| 10-22 16:17 | +10 | HYPE | UP | 0.64 | 0.76 | 0.86 |
| 10-22 16:17 | +5 | HYPE | UP | 0.64 | 0.70 | 0.24 |
| 10-22 16:17 | +10 stop | ETH | UP | 0.68 | 0.53 | -1.84 |
| 10-22 16:17 | +20 | ETH | UP | 0.67 | open |  |
| 10-22 16:17 | +15 | ETH | UP | 0.67 | open |  |
| 10-22 16:17 | +10 | ETH | UP | 0.68 | open |  |
| 10-22 16:17 | +5 | ETH | UP | 0.68 | open |  |
| 10-22 16:17 | +10 stop | NEAR | UP | 0.71 | 0.50 | -2.43 |
| 10-22 16:17 | +10 stop | DOGE | UP | 0.66 | 0.51 | -1.84 |
| 10-22 16:17 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-22 16:17 | +20 | BTC | UP | 0.65 | open |  |
| 10-22 16:17 | +15 | BTC | UP | 0.65 | 0.80 | 1.22 |
| 10-22 16:17 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-22 16:17 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-22 16:17 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-22 16:17 | +20 | BNB | UP | 0.62 | 0.83 | 1.83 |
| 10-22 16:17 | +15 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 10-22 16:17 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-22 16:17 | +5 | BNB | UP | 0.62 | 0.69 | 0.34 |
