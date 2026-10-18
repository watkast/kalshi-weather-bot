# Range-Scalp Bot

*Updated Sun Oct 18 06:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22165 | 19293 | 2872 (29) | 0 | $-6472.11 | -4.6% |
| **+10¢** | 16688 | 13372 | 3316 (42) | 0 | $-5742.00 | -5.5% |
| **+15¢** | 13975 | 10399 | 3576 (62) | 0 | $-5230.10 | -6.0% |
| **+20¢** | 12366 | 8619 | 3747 (80) | 0 | $-4693.60 | -6.0% |
| **+10¢ (15¢ stop)** | 27266 | 27216 | 50 (29) | 0 | $-10425.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 06:26 | +10 stop | ETH | DOWN | 0.67 | 0.95 | 2.58 |
| 10-18 06:26 | +10 | ETH | DOWN | 0.67 | 0.95 | 2.58 |
| 10-18 06:26 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-18 06:25 | +10 stop | HYPE | UP | 0.58 | 0.70 | 0.87 |
| 10-18 06:25 | +15 | HYPE | UP | 0.58 | 0.83 | 2.22 |
| 10-18 06:25 | +10 | HYPE | UP | 0.58 | 0.70 | 0.87 |
| 10-18 06:25 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 10-18 06:25 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-18 06:25 | +20 | ETH | DOWN | 0.63 | 0.95 | 2.97 |
| 10-18 06:25 | +15 | ETH | DOWN | 0.63 | 0.95 | 2.97 |
| 10-18 06:25 | +10 | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-18 06:25 | +5 | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-18 06:24 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-18 06:24 | +20 | SOL | DOWN | 0.68 | 0.97 | 2.68 |
| 10-18 06:24 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-18 06:24 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-18 06:24 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 10-18 06:23 | +10 stop | HYPE | DOWN | 0.39 | 0.65 | 2.27 |
| 10-18 06:23 | +15 | HYPE | DOWN | 0.39 | 0.65 | 2.27 |
| 10-18 06:23 | +10 | HYPE | DOWN | 0.40 | 0.65 | 2.17 |
| 10-18 06:23 | +5 | HYPE | DOWN | 0.40 | 0.65 | 2.17 |
| 10-18 06:23 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 10-18 06:23 | +5 | DOGE | DOWN | 0.64 | yes | -6.57 |
| 10-18 06:22 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-18 06:22 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-18 06:22 | +10 stop | XRP | DOWN | 0.67 | 0.29 | -4.11 |
| 10-18 06:22 | +15 | XRP | DOWN | 0.67 | yes | -6.86 |
| 10-18 06:22 | +10 | XRP | DOWN | 0.67 | yes | -6.86 |
| 10-18 06:22 | +5 | XRP | DOWN | 0.67 | yes | -6.86 |
| 10-18 06:22 | +10 stop | DOGE | DOWN | 0.64 | 0.38 | -2.93 |
| 10-18 06:22 | +15 | DOGE | DOWN | 0.64 | yes | -6.56 |
| 10-18 06:22 | +10 | DOGE | DOWN | 0.64 | yes | -6.56 |
| 10-18 06:22 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.19 |
| 10-18 06:22 | +10 stop | BNB | DOWN | 0.42 | 0.27 | -1.82 |
| 10-18 06:22 | +10 | BNB | DOWN | 0.42 | yes | -4.38 |
| 10-18 06:22 | +5 | BNB | DOWN | 0.42 | 0.51 | 0.54 |
| 10-18 06:21 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-18 06:21 | +10 | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-18 06:21 | +5 | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-18 06:21 | +10 stop | BNB | DOWN | 0.55 | 0.67 | 0.86 |
