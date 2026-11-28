# Range-Scalp Bot

*Updated Sat Nov 28 03:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74297 | 64858 | 9439 (171) | 1 | $-19666.51 | -4.2% |
| **+10¢** | 55350 | 44322 | 11028 (217) | 1 | $-18274.29 | -5.3% |
| **+15¢** | 46347 | 34471 | 11876 (275) | 1 | $-16315.84 | -5.6% |
| **+20¢** | 41244 | 28736 | 12508 (342) | 1 | $-14722.77 | -5.7% |
| **+10¢ (15¢ stop)** | 90422 | 90203 | 219 (135) | 0 | $-33387.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 03:23 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-28 03:20 | +10 stop | DOGE | DOWN | 0.67 | 0.85 | 1.60 |
| 11-28 03:20 | +10 stop | NEAR | UP | 0.59 | 0.41 | -2.14 |
| 11-28 03:20 | +10 stop | HYPE | UP | 0.51 | 0.34 | -2.06 |
| 11-28 03:19 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-28 03:19 | +10 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 11-28 03:19 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-28 03:19 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-28 03:19 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 03:18 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.15 |
| 11-28 03:18 | +10 | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-28 03:18 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-28 03:18 | +15 | NEAR | DOWN | 0.61 | 0.80 | 1.61 |
| 11-28 03:18 | +15 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 11-28 03:18 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.27 |
| 11-28 03:18 | +10 stop | DOGE | DOWN | 0.69 | 0.49 | -2.29 |
| 11-28 03:18 | +10 | DOGE | DOWN | 0.69 | 0.85 | 1.40 |
| 11-28 03:18 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.51 |
| 11-28 03:17 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-28 03:17 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-28 03:17 | +10 stop | NEAR | DOWN | 0.57 | 0.36 | -2.50 |
| 11-28 03:17 | +10 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-28 03:17 | +5 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-28 03:17 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-28 03:17 | +20 | ETH | DOWN | 0.62 | 0.83 | 1.83 |
| 11-28 03:17 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-28 03:17 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-28 03:17 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-28 03:17 | +10 stop | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 11-28 03:17 | +10 | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 11-28 03:17 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-28 03:17 | +20 | BTC | DOWN | 0.62 | 0.89 | 2.46 |
| 11-28 03:17 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-28 03:17 | +10 | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-28 03:17 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-28 03:17 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 03:17 | +20 | SOL | DOWN | 0.60 | 0.83 | 2.03 |
| 11-28 03:17 | +15 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 11-28 03:17 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 03:17 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
