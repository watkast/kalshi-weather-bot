# Range-Scalp Bot

*Updated Mon Oct 26 03:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34221 | 29884 | 4337 (43) | 0 | $-9410.37 | -4.4% |
| **+10¢** | 25613 | 20593 | 5020 (65) | 0 | $-8269.31 | -5.1% |
| **+15¢** | 21416 | 16010 | 5406 (89) | 0 | $-7403.29 | -5.5% |
| **+20¢** | 18984 | 13323 | 5661 (111) | 0 | $-6478.88 | -5.4% |
| **+10¢ (15¢ stop)** | 41922 | 41860 | 62 (33) | 0 | $-15972.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 03:42 | +10 stop | NEAR | DOWN | 0.58 | 0.43 | -1.86 |
| 10-26 03:42 | +20 | NEAR | DOWN | 0.58 | 0.85 | 2.43 |
| 10-26 03:42 | +15 | NEAR | DOWN | 0.58 | 0.85 | 2.43 |
| 10-26 03:42 | +10 | NEAR | DOWN | 0.58 | 0.85 | 2.43 |
| 10-26 03:42 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 10-26 03:40 | +10 stop | HYPE | UP | 0.68 | 0.46 | -2.54 |
| 10-26 03:40 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.74 |
| 10-26 03:40 | +10 stop | HYPE | UP | 0.50 | 0.65 | 1.16 |
| 10-26 03:40 | +10 stop | SOL | DOWN | 0.63 | 0.43 | -2.35 |
| 10-26 03:40 | +20 | SOL | DOWN | 0.63 | 0.84 | 1.83 |
| 10-26 03:40 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 03:40 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 03:39 | +10 stop | ZEC | DOWN | 0.55 | 0.35 | -2.34 |
| 10-26 03:39 | +10 stop | XRP | UP | 0.59 | 0.80 | 1.81 |
| 10-26 03:39 | +10 stop | HYPE | UP | 0.65 | 0.47 | -2.14 |
| 10-26 03:39 | +10 stop | DOGE | DOWN | 0.53 | 0.32 | -2.44 |
| 10-26 03:38 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 10-26 03:38 | +10 stop | XRP | UP | 0.50 | 0.60 | 0.65 |
| 10-26 03:37 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 03:37 | +15 | SOL | DOWN | 0.70 | 0.94 | 2.25 |
| 10-26 03:37 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-26 03:37 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 10-26 03:37 | +10 stop | HYPE | DOWN | 0.58 | 0.38 | -2.35 |
| 10-26 03:37 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-26 03:37 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 10-26 03:37 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-26 03:37 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-26 03:37 | +10 stop | ZEC | UP | 0.55 | 0.40 | -1.85 |
| 10-26 03:36 | +15 | BTC | DOWN | 0.70 | 0.91 | 1.90 |
| 10-26 03:36 | +10 | BTC | DOWN | 0.70 | 0.91 | 1.90 |
| 10-26 03:36 | +5 | BTC | DOWN | 0.70 | 0.91 | 1.90 |
| 10-26 03:36 | +10 stop | ZEC | DOWN | 0.71 | 0.42 | -3.23 |
| 10-26 03:36 | +20 | ZEC | DOWN | 0.71 | 0.91 | 1.82 |
| 10-26 03:36 | +15 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-26 03:36 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-26 03:36 | +5 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-26 03:35 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-26 03:35 | +10 | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-26 03:35 | +5 | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-26 03:35 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
