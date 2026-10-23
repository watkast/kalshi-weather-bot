# Range-Scalp Bot

*Updated Fri Oct 23 03:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29685 | 25833 | 3852 (39) | 0 | $-8808.16 | -4.7% |
| **+10¢** | 22258 | 17798 | 4460 (55) | 0 | $-7946.11 | -5.7% |
| **+15¢** | 18640 | 13852 | 4788 (78) | 0 | $-7123.62 | -6.1% |
| **+20¢** | 16498 | 11481 | 5017 (100) | 0 | $-6449.59 | -6.2% |
| **+10¢ (15¢ stop)** | 36431 | 36372 | 59 (32) | 0 | $-13740.22 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 03:06 | +10 stop | ZEC | DOWN | 0.62 | 0.41 | -2.44 |
| 10-23 03:04 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 10-23 03:04 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-23 03:04 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-23 03:04 | +10 | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-23 03:04 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 10-23 03:03 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-23 03:03 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-23 03:03 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-23 03:03 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 03:03 | +10 stop | HYPE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-23 03:03 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.17 |
| 10-23 03:03 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 03:02 | +10 stop | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 10-23 03:02 | +20 | SOL | DOWN | 0.62 | 0.87 | 2.25 |
| 10-23 03:02 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 03:02 | +10 | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 10-23 03:02 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 10-23 03:02 | +10 stop | ETH | UP | 0.40 | 0.54 | 1.05 |
| 10-23 03:02 | +5 | ETH | UP | 0.40 | 0.54 | 1.05 |
| 10-23 03:02 | +10 stop | NEAR | DOWN | 0.55 | 0.68 | 0.96 |
| 10-23 03:02 | +20 | NEAR | DOWN | 0.55 | 0.78 | 1.99 |
| 10-23 03:02 | +15 | NEAR | DOWN | 0.55 | 0.74 | 1.58 |
| 10-23 03:02 | +10 | NEAR | DOWN | 0.55 | 0.68 | 0.98 |
| 10-23 03:02 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.16 |
| 10-23 03:02 | +10 stop | ZEC | UP | 0.69 | 0.50 | -2.23 |
| 10-23 03:02 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-23 03:02 | +20 | XRP | DOWN | 0.68 | 0.90 | 1.97 |
| 10-23 03:02 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 10-23 03:02 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-23 03:02 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-23 03:02 | +10 stop | ETH | DOWN | 0.46 | 0.56 | 0.64 |
| 10-23 03:02 | +20 | ETH | DOWN | 0.46 | 0.71 | 2.17 |
| 10-23 03:02 | +15 | ETH | DOWN | 0.46 | 0.64 | 1.45 |
| 10-23 03:02 | +10 | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-23 03:02 | +5 | ETH | DOWN | 0.47 | 0.56 | 0.54 |
| 10-23 03:01 | +10 stop | HYPE | DOWN | 0.70 | 0.49 | -2.47 |
| 10-23 03:01 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.88 |
| 10-23 03:01 | +15 | HYPE | DOWN | 0.70 | 0.90 | 1.74 |
| 10-23 03:01 | +10 | HYPE | DOWN | 0.70 | 0.85 | 1.22 |
