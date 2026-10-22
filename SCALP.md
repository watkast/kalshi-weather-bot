# Range-Scalp Bot

*Updated Thu Oct 22 03:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28209 | 24582 | 3627 (39) | 3 | $-8095.06 | -4.6% |
| **+10¢** | 21189 | 16997 | 4192 (55) | 3 | $-7148.02 | -5.4% |
| **+15¢** | 17746 | 13234 | 4512 (78) | 4 | $-6384.79 | -5.7% |
| **+20¢** | 15699 | 10969 | 4730 (98) | 6 | $-5751.89 | -5.8% |
| **+10¢ (15¢ stop)** | 34620 | 34561 | 59 (32) | 2 | $-12945.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 03:35 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 10-22 03:35 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-22 03:35 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-22 03:35 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-22 03:35 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-22 03:35 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-22 03:35 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-22 03:35 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-22 03:34 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 03:32 | +10 stop | NEAR | UP | 0.57 | 0.40 | -2.05 |
| 10-22 03:32 | +20 | NEAR | UP | 0.58 | open |  |
| 10-22 03:32 | +15 | NEAR | UP | 0.58 | open |  |
| 10-22 03:32 | +10 | NEAR | UP | 0.58 | open |  |
| 10-22 03:32 | +5 | NEAR | UP | 0.58 | open |  |
| 10-22 03:32 | +5 | ZEC | DOWN | 0.57 | 0.66 | 0.54 |
| 10-22 03:31 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-22 03:31 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-22 03:31 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-22 03:31 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-22 03:31 | +5 | BNB | DOWN | 0.61 | 0.70 | 0.58 |
| 10-22 03:31 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-22 03:31 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-22 03:31 | +15 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 10-22 03:31 | +10 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-22 03:31 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-22 03:31 | +10 stop | ZEC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-22 03:31 | +20 | ZEC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-22 03:31 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-22 03:31 | +10 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-22 03:31 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.28 |
| 10-22 03:31 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 03:31 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-22 03:31 | +15 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 03:31 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 03:31 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 10-22 03:31 | +10 stop | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 10-22 03:31 | +20 | HYPE | DOWN | 0.57 | 0.86 | 2.63 |
| 10-22 03:31 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-22 03:31 | +10 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-22 03:31 | +5 | HYPE | DOWN | 0.56 | 0.74 | 1.44 |
