# Range-Scalp Bot

*Updated Thu Oct 22 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28844 | 25129 | 3715 (39) | 1 | $-8330.27 | -4.6% |
| **+10¢** | 21648 | 17350 | 4298 (55) | 0 | $-7423.30 | -5.5% |
| **+15¢** | 18122 | 13501 | 4621 (78) | 0 | $-6638.00 | -5.8% |
| **+20¢** | 16036 | 11191 | 4845 (100) | 0 | $-5978.89 | -5.9% |
| **+10¢ (15¢ stop)** | 35392 | 35333 | 59 (32) | 0 | $-13277.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 14:28 | +10 stop | HYPE | UP | 0.64 | 0.32 | -3.53 |
| 10-22 14:28 | +5 | HYPE | UP | 0.64 | open |  |
| 10-22 14:27 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 14:27 | +10 stop | BTC | UP | 0.68 | 0.47 | -2.44 |
| 10-22 14:27 | +10 stop | BNB | DOWN | 0.56 | 0.72 | 1.27 |
| 10-22 14:26 | +10 stop | BNB | UP | 0.44 | 0.56 | 0.84 |
| 10-22 14:26 | +10 stop | ETH | UP | 0.64 | 0.39 | -2.84 |
| 10-22 14:24 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 10-22 14:24 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 10-22 14:24 | +5 | XRP | UP | 0.60 | 0.69 | 0.58 |
| 10-22 14:24 | +10 stop | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 10-22 14:24 | +10 stop | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-22 14:23 | +10 stop | SOL | UP | 0.60 | 0.40 | -2.34 |
| 10-22 14:23 | +10 stop | ZEC | DOWN | 0.63 | 0.86 | 2.04 |
| 10-22 14:23 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 14:22 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-22 14:22 | +10 stop | SOL | DOWN | 0.62 | 0.32 | -3.33 |
| 10-22 14:22 | +10 stop | BNB | UP | 0.51 | 0.69 | 1.47 |
| 10-22 14:22 | +10 stop | DOGE | UP | 0.55 | 0.70 | 1.17 |
| 10-22 14:22 | +5 | XRP | UP | 0.51 | 0.56 | 0.14 |
| 10-22 14:21 | +10 stop | SOL | UP | 0.66 | 0.51 | -1.84 |
| 10-22 14:21 | +10 stop | XRP | UP | 0.71 | 0.56 | -1.83 |
| 10-22 14:21 | +5 | XRP | UP | 0.71 | 0.78 | 0.42 |
| 10-22 14:21 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 10-22 14:21 | +10 stop | NEAR | DOWN | 0.49 | 0.59 | 0.65 |
| 10-22 14:21 | +10 stop | BTC | DOWN | 0.49 | 0.33 | -1.94 |
| 10-22 14:20 | +10 stop | BNB | DOWN | 0.53 | 0.63 | 0.65 |
| 10-22 14:20 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.76 |
| 10-22 14:20 | +5 | HYPE | UP | 0.59 | 0.65 | 0.25 |
| 10-22 14:19 | +10 stop | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 14:19 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-22 14:19 | +10 stop | NEAR | DOWN | 0.58 | 0.69 | 0.77 |
| 10-22 14:18 | +5 | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-22 14:18 | +10 stop | BNB | DOWN | 0.62 | 0.41 | -2.44 |
| 10-22 14:18 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-22 14:18 | +15 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-22 14:18 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-22 14:18 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-22 14:18 | +5 | BTC | DOWN | 0.55 | 0.94 | 3.66 |
| 10-22 14:18 | +5 | XRP | DOWN | 0.56 | 0.64 | 0.45 |
