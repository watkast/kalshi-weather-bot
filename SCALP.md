# Range-Scalp Bot

*Updated Fri Nov 20 18:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66510 | 58049 | 8461 (128) | 0 | $-17870.53 | -4.3% |
| **+10¢** | 49657 | 39763 | 9894 (170) | 0 | $-16642.58 | -5.3% |
| **+15¢** | 41644 | 30976 | 10668 (217) | 0 | $-14953.22 | -5.7% |
| **+20¢** | 37075 | 25871 | 11204 (273) | 0 | $-13236.89 | -5.7% |
| **+10¢ (15¢ stop)** | 80993 | 80827 | 166 (100) | 0 | $-29931.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 18:10 | +10 stop | XRP | UP | 0.63 | 0.36 | -3.00 |
| 11-20 18:09 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-20 18:08 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-20 18:08 | +5 | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 11-20 18:08 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 11-20 18:07 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-20 18:06 | +10 stop | ZEC | UP | 0.41 | 0.56 | 1.15 |
| 11-20 18:06 | +10 stop | XRP | UP | 0.65 | 0.80 | 1.22 |
| 11-20 18:05 | +10 stop | BNB | DOWN | 0.50 | 0.74 | 2.08 |
| 11-20 18:04 | +10 stop | NEAR | DOWN | 0.61 | 0.39 | -2.54 |
| 11-20 18:04 | +5 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-20 18:04 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 11-20 18:04 | +10 stop | ETH | DOWN | 0.68 | 0.36 | -3.53 |
| 11-20 18:03 | +5 | ZEC | DOWN | 0.50 | 0.55 | 0.15 |
| 11-20 18:03 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 11-20 18:02 | +10 stop | NEAR | DOWN | 0.49 | 0.61 | 0.85 |
| 11-20 18:02 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-20 18:02 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.25 |
| 11-20 18:02 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 11-20 18:02 | +15 | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-20 18:02 | +10 | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-20 18:02 | +5 | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-20 18:02 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.10 |
| 11-20 18:02 | +20 | ZEC | DOWN | 0.59 | yes | -6.03 |
| 11-20 18:02 | +15 | ZEC | DOWN | 0.59 | yes | -6.03 |
| 11-20 18:02 | +10 | ZEC | DOWN | 0.59 | yes | -6.03 |
| 11-20 18:02 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-20 18:02 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 11-20 18:02 | +20 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-20 18:02 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-20 18:02 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-20 18:02 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-20 18:02 | +10 stop | BNB | DOWN | 0.55 | 0.36 | -2.27 |
| 11-20 18:02 | +20 | BNB | DOWN | 0.55 | 0.85 | 2.71 |
| 11-20 18:02 | +15 | BNB | DOWN | 0.55 | 0.74 | 1.56 |
| 11-20 18:02 | +10 | BNB | DOWN | 0.56 | 0.74 | 1.48 |
| 11-20 18:02 | +5 | BNB | DOWN | 0.56 | 0.74 | 1.46 |
| 11-20 18:02 | +10 stop | ETH | DOWN | 0.66 | 0.51 | -1.84 |
| 11-20 18:02 | +20 | ETH | DOWN | 0.66 | 0.90 | 2.18 |
| 11-20 18:02 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
