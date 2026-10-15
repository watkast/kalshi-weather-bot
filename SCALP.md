# Range-Scalp Bot

*Updated Thu Oct 15 12:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17514 | 15209 | 2305 (28) | 0 | $-5300.04 | -4.8% |
| **+10¢** | 13236 | 10567 | 2669 (40) | 0 | $-4795.26 | -5.8% |
| **+15¢** | 11109 | 8239 | 2870 (59) | 1 | $-4282.60 | -6.1% |
| **+20¢** | 9871 | 6865 | 3006 (77) | 1 | $-3739.09 | -6.0% |
| **+10¢ (15¢ stop)** | 21545 | 21495 | 50 (29) | 1 | $-8305.16 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 12:40 | +10 stop | ZEC | UP | 0.70 | open |  |
| 10-15 12:37 | +10 stop | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-15 12:36 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-15 12:35 | +5 | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 10-15 12:34 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.58 |
| 10-15 12:33 | +10 stop | ZEC | UP | 0.57 | 0.37 | -2.35 |
| 10-15 12:33 | +15 | ZEC | UP | 0.57 | open |  |
| 10-15 12:33 | +10 | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 10-15 12:33 | +5 | ZEC | UP | 0.57 | 0.66 | 0.56 |
| 10-15 12:33 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 12:33 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 12:33 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-15 12:33 | +10 stop | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 12:33 | +10 | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
| 10-15 12:33 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 10-15 12:33 | +10 stop | ZEC | DOWN | 0.43 | 0.57 | 1.04 |
| 10-15 12:33 | +15 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:33 | +10 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:33 | +5 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:31 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-15 12:31 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-15 12:31 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-15 12:31 | +10 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-15 12:31 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-15 12:31 | +10 stop | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 10-15 12:31 | +20 | XRP | DOWN | 0.67 | 0.89 | 1.97 |
| 10-15 12:31 | +15 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-15 12:31 | +10 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-15 12:31 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-15 12:31 | +10 stop | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.89 |
| 10-15 12:31 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +10 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-15 12:31 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-15 12:31 | +20 | SOL | DOWN | 0.65 | 0.90 | 2.27 |
| 10-15 12:31 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 12:31 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-15 12:31 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 12:31 | +10 stop | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
