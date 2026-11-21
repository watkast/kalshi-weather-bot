# Range-Scalp Bot

*Updated Sat Nov 21 04:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67017 | 58489 | 8528 (128) | 0 | $-18019.91 | -4.3% |
| **+10¢** | 50051 | 40081 | 9970 (170) | 0 | $-16765.40 | -5.3% |
| **+15¢** | 41971 | 31225 | 10746 (217) | 0 | $-15040.25 | -5.7% |
| **+20¢** | 37358 | 26067 | 11291 (274) | 0 | $-13363.71 | -5.7% |
| **+10¢ (15¢ stop)** | 81598 | 81432 | 166 (100) | 0 | $-30029.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 04:13 | +10 stop | HYPE | DOWN | 0.70 | 0.52 | -2.13 |
| 11-21 04:12 | +10 stop | NEAR | DOWN | 0.62 | 0.37 | -2.84 |
| 11-21 04:10 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-21 04:07 | +10 stop | ZEC | UP | 0.51 | 0.74 | 1.99 |
| 11-21 04:07 | +10 stop | HYPE | DOWN | 0.53 | 0.74 | 1.78 |
| 11-21 04:06 | +10 stop | NEAR | DOWN | 0.62 | 0.79 | 1.42 |
| 11-21 04:06 | +10 stop | ZEC | UP | 0.70 | 0.52 | -2.13 |
| 11-21 04:06 | +20 | ZEC | UP | 0.70 | 0.94 | 2.25 |
| 11-21 04:06 | +15 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 11-21 04:06 | +10 | ZEC | UP | 0.70 | 0.84 | 1.15 |
| 11-21 04:05 | +10 stop | NEAR | DOWN | 0.54 | 0.69 | 1.17 |
| 11-21 04:05 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.97 |
| 11-21 04:04 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.90 |
| 11-21 04:04 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-21 04:04 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 11-21 04:04 | +10 stop | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-21 04:03 | +10 stop | BNB | DOWN | 0.70 | 0.92 | 2.00 |
| 11-21 04:03 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 11-21 04:03 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-21 04:03 | +5 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 11-21 04:02 | +10 stop | ZEC | UP | 0.48 | 0.61 | 0.95 |
| 11-21 04:02 | +20 | ZEC | UP | 0.48 | 0.71 | 1.97 |
| 11-21 04:02 | +15 | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 11-21 04:02 | +10 | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 11-21 04:02 | +5 | ZEC | UP | 0.46 | 0.55 | 0.54 |
| 11-21 04:02 | +5 | HYPE | UP | 0.70 | no | -7.15 |
| 11-21 04:02 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 11-21 04:02 | +20 | SOL | UP | 0.55 | no | -5.68 |
| 11-21 04:02 | +15 | SOL | UP | 0.56 | no | -5.78 |
| 11-21 04:02 | +10 | SOL | UP | 0.56 | no | -5.78 |
| 11-21 04:02 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 11-21 04:01 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 11-21 04:01 | +20 | NEAR | UP | 0.64 | 0.94 | 2.76 |
| 11-21 04:01 | +15 | NEAR | UP | 0.64 | 0.94 | 2.76 |
| 11-21 04:01 | +10 | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 11-21 04:01 | +5 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-21 04:01 | +10 stop | DOGE | UP | 0.56 | 0.39 | -2.05 |
| 11-21 04:01 | +20 | DOGE | UP | 0.56 | no | -5.78 |
| 11-21 04:01 | +15 | DOGE | UP | 0.55 | no | -5.68 |
| 11-21 04:01 | +10 | DOGE | UP | 0.55 | no | -5.68 |
