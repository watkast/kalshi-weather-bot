# Range-Scalp Bot

*Updated Tue Oct 06 18:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5291 | 4580 | 711 (7) | 0 | $-1674.33 | -5.0% |
| **+10¢** | 4040 | 3210 | 830 (12) | 1 | $-1564.02 | -6.2% |
| **+15¢** | 3385 | 2506 | 879 (15) | 2 | $-1368.83 | -6.4% |
| **+20¢** | 3032 | 2119 | 913 (22) | 2 | $-1092.81 | -5.7% |
| **+10¢ (15¢ stop)** | 6464 | 6449 | 15 (9) | 1 | $-2352.65 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 18:07 | +10 stop | ZEC | UP | 0.52 | 0.65 | 0.96 |
| 10-06 18:07 | +20 | ZEC | UP | 0.52 | open |  |
| 10-06 18:07 | +15 | ZEC | UP | 0.52 | open |  |
| 10-06 18:07 | +10 | ZEC | UP | 0.52 | 0.65 | 1.00 |
| 10-06 18:07 | +5 | ZEC | UP | 0.52 | 0.65 | 1.00 |
| 10-06 18:02 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 18:02 | +20 | BTC | UP | 0.59 | 0.80 | 1.81 |
| 10-06 18:02 | +15 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-06 18:02 | +10 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 18:02 | +5 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 18:01 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 10-06 18:01 | +20 | ZEC | UP | 0.66 | 0.89 | 2.07 |
| 10-06 18:01 | +15 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-06 18:01 | +10 | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 10-06 18:01 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-06 18:01 | +10 stop | HYPE | UP | 0.68 | open |  |
| 10-06 18:01 | +20 | HYPE | UP | 0.68 | open |  |
| 10-06 18:01 | +15 | HYPE | UP | 0.68 | open |  |
| 10-06 18:01 | +10 | HYPE | UP | 0.68 | open |  |
| 10-06 18:01 | +5 | HYPE | UP | 0.68 | 0.77 | 0.58 |
| 10-06 18:01 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.85 |
| 10-06 18:01 | +20 | NEAR | UP | 0.66 | 0.86 | 1.79 |
| 10-06 18:01 | +15 | NEAR | UP | 0.66 | 0.86 | 1.79 |
| 10-06 18:01 | +10 | NEAR | UP | 0.66 | 0.77 | 0.85 |
| 10-06 18:01 | +5 | NEAR | UP | 0.66 | 0.74 | 0.54 |
| 10-06 17:57 | +10 stop | NEAR | UP | 0.58 | 0.83 | 2.22 |
| 10-06 17:51 | +10 stop | HYPE | UP | 0.66 | 0.82 | 1.29 |
| 10-06 17:51 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-06 17:50 | +10 stop | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-06 17:50 | +10 stop | DOGE | UP | 0.61 | 0.80 | 1.61 |
| 10-06 17:50 | +10 stop | SOL | UP | 0.67 | 0.88 | 1.86 |
| 10-06 17:50 | +5 | SOL | UP | 0.67 | 0.75 | 0.50 |
| 10-06 17:50 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 10-06 17:50 | +5 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-06 17:50 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-06 17:50 | +10 stop | HYPE | DOWN | 0.60 | 0.41 | -2.24 |
| 10-06 17:50 | +10 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 10-06 17:50 | +5 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-06 17:50 | +10 stop | ETH | UP | 0.65 | 0.83 | 1.54 |
| 10-06 17:50 | +10 stop | BNB | DOWN | 0.54 | 0.34 | -2.34 |
