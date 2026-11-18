# Range-Scalp Bot

*Updated Wed Nov 18 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63305 | 55216 | 8089 (118) | 1 | $-17266.79 | -4.3% |
| **+10¢** | 47295 | 37828 | 9467 (159) | 0 | $-16171.67 | -5.4% |
| **+15¢** | 39651 | 29443 | 10208 (203) | 1 | $-14654.41 | -5.9% |
| **+20¢** | 35328 | 24616 | 10712 (258) | 1 | $-12895.97 | -5.8% |
| **+10¢ (15¢ stop)** | 77051 | 76893 | 158 (93) | 0 | $-28389.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 00:10 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 11-18 00:10 | +5 | BTC | UP | 0.64 | open |  |
| 11-18 00:10 | +10 stop | ETH | UP | 0.60 | 0.36 | -2.74 |
| 11-18 00:09 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-18 00:09 | +10 | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-18 00:09 | +5 | BNB | UP | 0.69 | 0.79 | 0.73 |
| 11-18 00:09 | +10 stop | BTC | DOWN | 0.45 | 0.62 | 1.35 |
| 11-18 00:09 | +5 | BTC | DOWN | 0.46 | 0.62 | 1.25 |
| 11-18 00:08 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 00:08 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.96 |
| 11-18 00:08 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-18 00:08 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 00:08 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 00:08 | +10 stop | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-18 00:08 | +20 | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 11-18 00:08 | +15 | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 11-18 00:08 | +10 | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-18 00:08 | +5 | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-18 00:07 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-18 00:07 | +20 | BTC | DOWN | 0.68 | 0.90 | 2.00 |
| 11-18 00:07 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-18 00:07 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-18 00:07 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-18 00:06 | +10 stop | BNB | DOWN | 0.67 | 0.33 | -3.72 |
| 11-18 00:06 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-18 00:06 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 11-18 00:04 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-18 00:04 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 11-18 00:02 | +10 stop | ETH | DOWN | 0.68 | 0.49 | -2.24 |
| 11-18 00:02 | +20 | ETH | DOWN | 0.68 | 0.90 | 2.00 |
| 11-18 00:02 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-18 00:02 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-18 00:02 | +5 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-18 00:02 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.74 |
| 11-18 00:02 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-18 00:02 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-18 00:02 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-18 00:02 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.28 |
| 11-18 00:01 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-18 00:01 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
