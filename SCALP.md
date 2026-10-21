# Range-Scalp Bot

*Updated Wed Oct 21 05:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26748 | 23295 | 3453 (33) | 1 | $-7809.97 | -4.6% |
| **+10¢** | 20132 | 16145 | 3987 (48) | 2 | $-6881.26 | -5.4% |
| **+15¢** | 16853 | 12564 | 4289 (72) | 1 | $-6117.17 | -5.8% |
| **+20¢** | 14920 | 10424 | 4496 (91) | 2 | $-5486.15 | -5.9% |
| **+10¢ (15¢ stop)** | 32787 | 32734 | 53 (30) | 0 | $-12061.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 05:29 | +10 stop | HYPE | DOWN | 0.23 | 0.55 | 2.89 |
| 10-21 05:29 | +20 | HYPE | DOWN | 0.25 | 0.55 | 2.68 |
| 10-21 05:29 | +10 | HYPE | DOWN | 0.25 | 0.55 | 2.68 |
| 10-21 05:29 | +5 | HYPE | DOWN | 0.26 | 0.55 | 2.58 |
| 10-21 05:28 | +10 stop | HYPE | UP | 0.69 | 0.46 | -2.63 |
| 10-21 05:27 | +10 stop | HYPE | DOWN | 0.45 | 0.57 | 0.84 |
| 10-21 05:26 | +10 stop | SOL | UP | 0.46 | 0.68 | 1.86 |
| 10-21 05:26 | +5 | SOL | UP | 0.46 | 0.53 | 0.34 |
| 10-21 05:25 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-21 05:25 | +10 stop | SOL | DOWN | 0.62 | 0.44 | -2.15 |
| 10-21 05:23 | +10 stop | SOL | UP | 0.49 | 0.34 | -1.84 |
| 10-21 05:23 | +10 stop | HYPE | UP | 0.66 | 0.37 | -3.27 |
| 10-21 05:23 | +10 stop | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-21 05:23 | +5 | NEAR | UP | 0.57 | 0.66 | 0.56 |
| 10-21 05:23 | +10 stop | ETH | UP | 0.61 | 0.36 | -2.84 |
| 10-21 05:22 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-21 05:22 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-21 05:22 | +10 | NEAR | DOWN | 0.62 | 0.80 | 1.52 |
| 10-21 05:22 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.28 |
| 10-21 05:22 | +10 stop | BNB | UP | 0.67 | 0.24 | -4.63 |
| 10-21 05:22 | +10 | BNB | UP | 0.67 | open |  |
| 10-21 05:22 | +5 | BNB | UP | 0.67 | 0.73 | 0.26 |
| 10-21 05:21 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-21 05:21 | +10 stop | NEAR | DOWN | 0.65 | 0.37 | -3.13 |
| 10-21 05:21 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-21 05:20 | +10 stop | DOGE | UP | 0.58 | 0.33 | -2.84 |
| 10-21 05:20 | +5 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-21 05:19 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.89 |
| 10-21 05:19 | +15 | HYPE | UP | 0.64 | 0.98 | 3.17 |
| 10-21 05:19 | +10 | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 10-21 05:19 | +5 | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 10-21 05:19 | +10 stop | NEAR | UP | 0.69 | 0.48 | -2.43 |
| 10-21 05:18 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-21 05:17 | +10 stop | SOL | UP | 0.68 | 0.51 | -2.04 |
| 10-21 05:17 | +10 stop | ETH | UP | 0.64 | 0.48 | -1.95 |
| 10-21 05:17 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.74 |
| 10-21 05:17 | +20 | ZEC | DOWN | 0.58 | 0.82 | 2.08 |
| 10-21 05:17 | +15 | ZEC | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 05:17 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-21 05:17 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
