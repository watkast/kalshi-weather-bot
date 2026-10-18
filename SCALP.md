# Range-Scalp Bot

*Updated Sun Oct 18 07:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22208 | 19332 | 2876 (29) | 0 | $-6470.10 | -4.6% |
| **+10¢** | 16722 | 13401 | 3321 (42) | 0 | $-5740.77 | -5.5% |
| **+15¢** | 14007 | 10424 | 3583 (62) | 0 | $-5237.14 | -6.0% |
| **+20¢** | 12394 | 8640 | 3754 (80) | 0 | $-4693.33 | -6.0% |
| **+10¢ (15¢ stop)** | 27313 | 27263 | 50 (29) | 0 | $-10415.79 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 07:24 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-18 07:24 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 10-18 07:23 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.71 |
| 10-18 07:23 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-18 07:23 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 10-18 07:23 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-18 07:22 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-18 07:22 | +20 | HYPE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-18 07:22 | +15 | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-18 07:22 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-18 07:22 | +5 | HYPE | DOWN | 0.58 | 0.67 | 0.56 |
| 10-18 07:22 | +15 | ETH | DOWN | 0.69 | 0.88 | 1.67 |
| 10-18 07:22 | +10 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 07:22 | +5 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 07:22 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 07:22 | +20 | ETH | DOWN | 0.69 | 0.92 | 2.05 |
| 10-18 07:21 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 07:21 | +10 stop | SOL | DOWN | 0.49 | 0.62 | 0.95 |
| 10-18 07:21 | +10 | SOL | DOWN | 0.49 | 0.62 | 0.95 |
| 10-18 07:21 | +5 | SOL | DOWN | 0.49 | 0.62 | 0.95 |
| 10-18 07:20 | +10 stop | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 10-18 07:20 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 10-18 07:20 | +10 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 10-18 07:20 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-18 07:20 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-18 07:20 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.05 |
| 10-18 07:20 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-18 07:20 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-18 07:20 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-18 07:20 | +10 stop | SOL | DOWN | 0.45 | 0.60 | 1.15 |
| 10-18 07:20 | +10 | SOL | DOWN | 0.45 | 0.60 | 1.15 |
| 10-18 07:20 | +5 | SOL | DOWN | 0.45 | 0.60 | 1.15 |
| 10-18 07:17 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 07:17 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +20 | NEAR | DOWN | 0.60 | 0.85 | 2.24 |
| 10-18 07:17 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-18 07:17 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +5 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-18 07:17 | +20 | ZEC | DOWN | 0.65 | 0.89 | 2.17 |
