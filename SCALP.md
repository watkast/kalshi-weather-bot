# Range-Scalp Bot

*Updated Thu Oct 22 16:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29012 | 25267 | 3745 (39) | 0 | $-8450.60 | -4.6% |
| **+10¢** | 21768 | 17436 | 4332 (55) | 0 | $-7548.89 | -5.5% |
| **+15¢** | 18222 | 13566 | 4656 (78) | 0 | $-6749.19 | -5.9% |
| **+20¢** | 16128 | 11247 | 4881 (100) | 0 | $-6084.04 | -6.0% |
| **+10¢ (15¢ stop)** | 35602 | 35543 | 59 (32) | 0 | $-13381.66 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 16:46 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-22 16:46 | +20 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 10-22 16:46 | +15 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-22 16:46 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-22 16:46 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-22 16:46 | +10 stop | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-22 16:46 | +20 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-22 16:46 | +15 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-22 16:46 | +10 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-22 16:46 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.57 |
| 10-22 16:46 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 16:46 | +20 | BTC | DOWN | 0.64 | 0.88 | 2.15 |
| 10-22 16:46 | +15 | BTC | DOWN | 0.64 | 0.88 | 2.15 |
| 10-22 16:46 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 16:46 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-22 16:46 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-22 16:46 | +20 | DOGE | DOWN | 0.62 | 0.87 | 2.25 |
| 10-22 16:46 | +15 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-22 16:46 | +10 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-22 16:46 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-22 16:46 | +10 stop | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-22 16:46 | +20 | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-22 16:46 | +15 | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-22 16:46 | +10 | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-22 16:46 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 10-22 16:46 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 16:46 | +20 | XRP | DOWN | 0.68 | 0.91 | 2.08 |
| 10-22 16:46 | +15 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-22 16:46 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 16:46 | +5 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 16:46 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 16:46 | +20 | NEAR | DOWN | 0.71 | 0.93 | 2.00 |
| 10-22 16:46 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 10-22 16:46 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 16:46 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 10-22 16:42 | +10 stop | NEAR | UP | 0.37 | 0.54 | 1.35 |
| 10-22 16:41 | +10 stop | NEAR | UP | 0.51 | 0.63 | 0.85 |
| 10-22 16:40 | +10 stop | XRP | DOWN | 0.67 | 0.88 | 1.90 |
| 10-22 16:40 | +10 stop | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-22 16:40 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
