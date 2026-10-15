# Range-Scalp Bot

*Updated Thu Oct 15 18:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17932 | 15562 | 2370 (28) | 1 | $-5528.62 | -4.9% |
| **+10¢** | 13546 | 10801 | 2745 (40) | 1 | $-5027.70 | -5.9% |
| **+15¢** | 11361 | 8410 | 2951 (59) | 1 | $-4531.42 | -6.4% |
| **+20¢** | 10099 | 7012 | 3087 (77) | 1 | $-3948.33 | -6.2% |
| **+10¢ (15¢ stop)** | 22085 | 22035 | 50 (29) | 0 | $-8548.81 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 18:11 | +10 stop | NEAR | DOWN | 0.69 | 0.34 | -3.82 |
| 10-15 18:11 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-15 18:09 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-15 18:08 | +10 stop | NEAR | UP | 0.60 | 0.41 | -2.24 |
| 10-15 18:08 | +10 stop | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 10-15 18:08 | +20 | XRP | DOWN | 0.68 | 0.91 | 2.05 |
| 10-15 18:08 | +15 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-15 18:08 | +10 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-15 18:08 | +5 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-15 18:06 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 18:06 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-15 18:06 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
| 10-15 18:06 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 10-15 18:05 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 10-15 18:03 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.26 |
| 10-15 18:02 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-15 18:02 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-15 18:02 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-15 18:02 | +10 stop | ZEC | UP | 0.63 | 0.47 | -1.95 |
| 10-15 18:01 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 18:01 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-15 18:01 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-15 18:01 | +10 | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 18:01 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-15 18:01 | +10 stop | ZEC | UP | 0.70 | 0.53 | -2.03 |
| 10-15 18:01 | +20 | ZEC | UP | 0.70 | 0.90 | 1.78 |
| 10-15 18:01 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-15 18:01 | +10 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-15 18:01 | +5 | ZEC | UP | 0.70 | 0.75 | 0.21 |
| 10-15 18:01 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-15 18:01 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 18:00 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 18:00 | +20 | BNB | DOWN | 0.56 | 0.80 | 2.10 |
| 10-15 18:00 | +15 | BNB | DOWN | 0.56 | 0.71 | 1.17 |
| 10-15 18:00 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 18:00 | +5 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 17:58 | +10 stop | HYPE | UP | 0.67 | 0.95 | 2.58 |
