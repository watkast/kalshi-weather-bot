# Range-Scalp Bot

*Updated Fri Nov 20 16:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66387 | 57934 | 8453 (128) | 0 | $-17886.59 | -4.3% |
| **+10¢** | 49566 | 39683 | 9883 (170) | 0 | $-16661.28 | -5.3% |
| **+15¢** | 41568 | 30911 | 10657 (217) | 0 | $-14985.91 | -5.7% |
| **+20¢** | 37014 | 25822 | 11192 (273) | 0 | $-13274.07 | -5.7% |
| **+10¢ (15¢ stop)** | 80837 | 80671 | 166 (100) | 0 | $-29842.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 16:17 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-20 16:17 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-20 16:17 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-20 16:17 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-20 16:17 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-20 16:17 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.80 |
| 11-20 16:17 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 11-20 16:16 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.93 |
| 11-20 16:16 | +20 | BNB | DOWN | 0.67 | 0.90 | 2.08 |
| 11-20 16:16 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.43 |
| 11-20 16:16 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.00 |
| 11-20 16:16 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.48 |
| 11-20 16:16 | +10 stop | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-20 16:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-20 16:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-20 16:16 | +10 | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-20 16:16 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-20 16:16 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-20 16:16 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-20 16:16 | +15 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 11-20 16:16 | +10 | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-20 16:16 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 11-20 16:16 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-20 16:16 | +20 | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-20 16:16 | +15 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-20 16:16 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-20 16:16 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-20 16:16 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 16:16 | +20 | XRP | DOWN | 0.63 | 0.87 | 2.15 |
| 11-20 16:16 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 11-20 16:16 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 16:16 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 11-20 16:16 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.07 |
| 11-20 16:16 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.88 |
| 11-20 16:16 | +15 | SOL | DOWN | 0.69 | 0.86 | 1.47 |
| 11-20 16:16 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-20 16:16 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.22 |
| 11-20 16:16 | +10 stop | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-20 16:16 | +20 | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 11-20 16:16 | +15 | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
