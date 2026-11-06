# Range-Scalp Bot

*Updated Fri Nov 06 17:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49804 | 43415 | 6389 (76) | 0 | $-13977.72 | -4.5% |
| **+10¢** | 37175 | 29744 | 7431 (101) | 0 | $-12859.94 | -5.5% |
| **+15¢** | 31135 | 23126 | 8009 (130) | 0 | $-11775.76 | -6.0% |
| **+20¢** | 27678 | 19281 | 8397 (171) | 0 | $-10411.34 | -6.0% |
| **+10¢ (15¢ stop)** | 60662 | 60565 | 97 (57) | 0 | $-22431.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 17:12 | +10 stop | NEAR | UP | 0.65 | 0.50 | -1.84 |
| 11-06 17:12 | +10 | NEAR | UP | 0.67 | no | -6.86 |
| 11-06 17:12 | +5 | NEAR | UP | 0.64 | no | -6.57 |
| 11-06 17:12 | +10 stop | SOL | DOWN | 0.61 | 0.91 | 2.78 |
| 11-06 17:12 | +15 | SOL | DOWN | 0.61 | 0.91 | 2.78 |
| 11-06 17:12 | +10 | SOL | DOWN | 0.61 | 0.91 | 2.78 |
| 11-06 17:12 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 11-06 17:12 | +10 stop | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-06 17:12 | +20 | ETH | DOWN | 0.62 | 0.96 | 3.20 |
| 11-06 17:12 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-06 17:12 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-06 17:12 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-06 17:11 | +10 stop | NEAR | DOWN | 0.63 | 0.38 | -2.88 |
| 11-06 17:10 | +10 stop | NEAR | UP | 0.43 | 0.63 | 1.63 |
| 11-06 17:09 | +5 | ZEC | UP | 0.53 | no | -5.48 |
| 11-06 17:09 | +10 stop | ZEC | UP | 0.49 | 0.33 | -1.94 |
| 11-06 17:09 | +5 | ZEC | UP | 0.49 | 0.56 | 0.30 |
| 11-06 17:07 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 17:07 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-06 17:07 | +10 | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-06 17:07 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 11-06 17:07 | +10 stop | NEAR | UP | 0.63 | 0.48 | -1.85 |
| 11-06 17:07 | +20 | NEAR | UP | 0.63 | no | -6.47 |
| 11-06 17:07 | +15 | NEAR | UP | 0.63 | no | -6.47 |
| 11-06 17:07 | +10 | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 11-06 17:07 | +5 | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 11-06 17:07 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-06 17:07 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 11-06 17:07 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.21 |
| 11-06 17:07 | +10 stop | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 17:07 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.80 |
| 11-06 17:07 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 17:07 | +10 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 17:07 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 17:07 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 17:07 | +20 | SOL | DOWN | 0.71 | 0.91 | 1.80 |
| 11-06 17:07 | +5 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-06 17:07 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 11-06 17:07 | +10 stop | BTC | UP | 0.59 | 0.34 | -2.83 |
| 11-06 17:06 | +10 stop | BNB | UP | 0.43 | 0.58 | 1.14 |
