# Range-Scalp Bot

*Updated Mon Oct 19 23:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24781 | 21569 | 3212 (31) | 0 | $-7282.95 | -4.7% |
| **+10¢** | 18637 | 14925 | 3712 (46) | 0 | $-6493.95 | -5.5% |
| **+15¢** | 15600 | 11601 | 3999 (70) | 0 | $-5874.74 | -6.0% |
| **+20¢** | 13793 | 9605 | 4188 (88) | 0 | $-5301.96 | -6.1% |
| **+10¢ (15¢ stop)** | 30424 | 30372 | 52 (30) | 0 | $-11410.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 23:52 | +10 stop | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 23:50 | +10 stop | DOGE | DOWN | 0.70 | 0.48 | -2.53 |
| 10-19 23:50 | +15 | DOGE | DOWN | 0.70 | 0.93 | 2.07 |
| 10-19 23:50 | +10 | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-19 23:50 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-19 23:48 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-19 23:46 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 23:46 | +20 | XRP | DOWN | 0.67 | 0.93 | 2.35 |
| 10-19 23:46 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 10-19 23:46 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-19 23:46 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-19 23:46 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 23:46 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-19 23:46 | +15 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-19 23:46 | +10 | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 23:46 | +5 | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 23:46 | +10 stop | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-19 23:46 | +20 | BTC | DOWN | 0.60 | 0.80 | 1.71 |
| 10-19 23:46 | +15 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-19 23:46 | +10 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-19 23:46 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-19 23:46 | +10 stop | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 23:46 | +20 | ETH | DOWN | 0.62 | 0.84 | 1.93 |
| 10-19 23:46 | +15 | ETH | DOWN | 0.61 | 0.78 | 1.40 |
| 10-19 23:46 | +10 | ETH | DOWN | 0.61 | 0.78 | 1.40 |
| 10-19 23:46 | +5 | ETH | DOWN | 0.61 | 0.69 | 0.48 |
| 10-19 23:46 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-19 23:46 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-19 23:46 | +15 | NEAR | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 23:46 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-19 23:46 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 10-19 23:46 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-19 23:46 | +20 | DOGE | DOWN | 0.58 | 0.84 | 2.32 |
| 10-19 23:46 | +15 | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-19 23:46 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-19 23:46 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-19 23:46 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-19 23:46 | +20 | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-19 23:46 | +15 | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-19 23:46 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
