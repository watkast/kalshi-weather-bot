# Range-Scalp Bot

*Updated Sun Nov 01 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43164 | 37625 | 5539 (62) | 3 | $-12272.94 | -4.5% |
| **+10¢** | 32187 | 25787 | 6400 (84) | 4 | $-10996.08 | -5.4% |
| **+15¢** | 26930 | 20033 | 6897 (112) | 4 | $-10056.78 | -5.9% |
| **+20¢** | 23914 | 16688 | 7226 (146) | 4 | $-8889.85 | -5.9% |
| **+10¢ (15¢ stop)** | 52636 | 52553 | 83 (48) | 0 | $-19915.20 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 03:37 | +5 | ETH | DOWN | 0.63 | open |  |
| 11-01 03:36 | +10 stop | ETH | DOWN | 0.60 | 0.41 | -2.24 |
| 11-01 03:36 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-01 03:36 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-01 03:36 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-01 03:36 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 11-01 03:35 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-01 03:34 | +5 | ETH | UP | 0.47 | 0.54 | 0.34 |
| 11-01 03:34 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 11-01 03:34 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-01 03:34 | +15 | BNB | UP | 0.63 | 0.82 | 1.62 |
| 11-01 03:34 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-01 03:34 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 11-01 03:33 | +5 | DOGE | UP | 0.68 | 0.76 | 0.51 |
| 11-01 03:33 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-01 03:32 | +10 stop | ETH | DOWN | 0.48 | 0.70 | 1.87 |
| 11-01 03:32 | +20 | ETH | DOWN | 0.48 | 0.70 | 1.87 |
| 11-01 03:32 | +15 | ETH | DOWN | 0.49 | 0.70 | 1.77 |
| 11-01 03:32 | +10 | ETH | DOWN | 0.49 | 0.70 | 1.77 |
| 11-01 03:32 | +5 | ETH | DOWN | 0.49 | 0.54 | 0.14 |
| 11-01 03:31 | +10 stop | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 11-01 03:31 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-01 03:31 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-01 03:31 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +5 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 03:31 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-01 03:31 | +20 | SOL | UP | 0.68 | 0.88 | 1.76 |
| 11-01 03:31 | +15 | SOL | UP | 0.68 | 0.86 | 1.55 |
| 11-01 03:31 | +10 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-01 03:31 | +5 | SOL | UP | 0.68 | 0.75 | 0.40 |
| 11-01 03:31 | +10 stop | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +20 | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-01 03:31 | +15 | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +10 | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-01 03:31 | +5 | BNB | UP | 0.53 | 0.59 | 0.25 |
| 11-01 03:31 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 11-01 03:31 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-01 03:31 | +20 | BTC | UP | 0.64 | 0.86 | 1.94 |
| 11-01 03:31 | +15 | BTC | UP | 0.64 | 0.80 | 1.31 |
