# Range-Scalp Bot

*Updated Mon Oct 05 17:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4026 | 3457 | 569 (4) | 0 | $-1469.98 | -5.8% |
| **+10¢** | 3114 | 2459 | 655 (5) | 0 | $-1352.58 | -6.9% |
| **+15¢** | 2619 | 1930 | 689 (8) | 0 | $-1159.60 | -7.1% |
| **+20¢** | 2339 | 1621 | 718 (13) | 0 | $-995.53 | -6.8% |
| **+10¢ (15¢ stop)** | 4959 | 4954 | 5 (2) | 0 | $-1811.72 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 17:03 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 17:03 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 17:03 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 17:02 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 17:02 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.80 |
| 10-05 17:02 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-05 17:02 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 17:02 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-05 17:01 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 17:01 | +20 | NEAR | DOWN | 0.65 | 0.89 | 2.17 |
| 10-05 17:01 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 10-05 17:01 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.88 |
| 10-05 17:01 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.36 |
| 10-05 17:01 | +10 stop | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-05 17:01 | +20 | DOGE | DOWN | 0.57 | 0.79 | 1.90 |
| 10-05 17:01 | +15 | DOGE | DOWN | 0.57 | 0.79 | 1.90 |
| 10-05 17:01 | +10 | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-05 17:01 | +5 | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-05 17:01 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 10-05 17:01 | +20 | SOL | DOWN | 0.56 | 0.85 | 2.63 |
| 10-05 17:01 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-05 17:01 | +10 | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 10-05 17:01 | +5 | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 10-05 17:01 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 10-05 17:01 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 17:01 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-05 17:01 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 10-05 17:01 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-05 17:01 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-05 17:01 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-05 17:01 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 17:01 | +15 | ETH | DOWN | 0.61 | 0.82 | 1.80 |
| 10-05 17:01 | +10 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 10-05 17:01 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 10-05 17:00 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.67 |
| 10-05 17:00 | +20 | ZEC | DOWN | 0.55 | 0.77 | 1.90 |
| 10-05 17:00 | +15 | ZEC | DOWN | 0.55 | 0.77 | 1.90 |
| 10-05 17:00 | +10 | ZEC | DOWN | 0.55 | 0.65 | 0.67 |
| 10-05 17:00 | +5 | ZEC | DOWN | 0.55 | 0.65 | 0.67 |
| 10-05 17:00 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
