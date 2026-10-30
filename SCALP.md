# Range-Scalp Bot

*Updated Fri Oct 30 05:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40260 | 35161 | 5099 (51) | 0 | $-11089.33 | -4.4% |
| **+10¢** | 29996 | 24098 | 5898 (74) | 0 | $-9829.25 | -5.2% |
| **+15¢** | 25082 | 18734 | 6348 (101) | 0 | $-8837.17 | -5.6% |
| **+20¢** | 22260 | 15605 | 6655 (130) | 0 | $-7750.44 | -5.5% |
| **+10¢ (15¢ stop)** | 49106 | 49036 | 70 (37) | 0 | $-18552.00 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 05:29 | +10 stop | XRP | UP | 0.38 | 0.64 | 2.26 |
| 10-30 05:27 | +5 | HYPE | UP | 0.71 | 0.89 | 1.61 |
| 10-30 05:27 | +5 | BTC | DOWN | 0.64 | yes | -6.57 |
| 10-30 05:26 | +5 | BTC | DOWN | 0.54 | 0.61 | 0.35 |
| 10-30 05:26 | +10 stop | HYPE | UP | 0.71 | 0.52 | -2.23 |
| 10-30 05:25 | +10 stop | NEAR | UP | 0.65 | 0.22 | -4.59 |
| 10-30 05:25 | +10 stop | BTC | DOWN | 0.55 | 0.37 | -2.15 |
| 10-30 05:25 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-30 05:25 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 10-30 05:24 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.85 |
| 10-30 05:24 | +5 | HYPE | UP | 0.64 | 0.72 | 0.48 |
| 10-30 05:23 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 10-30 05:23 | +10 stop | BTC | UP | 0.68 | 0.53 | -1.84 |
| 10-30 05:23 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-30 05:23 | +20 | ETH | DOWN | 0.60 | 0.88 | 2.55 |
| 10-30 05:23 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-30 05:23 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-30 05:23 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 10-30 05:23 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 10-30 05:23 | +10 | HYPE | UP | 0.57 | 0.72 | 1.17 |
| 10-30 05:23 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
| 10-30 05:23 | +10 stop | XRP | UP | 0.70 | 0.44 | -2.93 |
| 10-30 05:22 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-30 05:22 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-30 05:22 | +10 stop | BTC | DOWN | 0.58 | 0.37 | -2.45 |
| 10-30 05:22 | +10 | BTC | DOWN | 0.58 | yes | -5.98 |
| 10-30 05:22 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-30 05:22 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 10-30 05:22 | +10 | XRP | DOWN | 0.62 | 0.98 | 3.43 |
| 10-30 05:22 | +5 | XRP | DOWN | 0.62 | 0.98 | 3.43 |
| 10-30 05:22 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 10-30 05:21 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-30 05:20 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 10-30 05:20 | +10 stop | BTC | UP | 0.49 | 0.26 | -2.62 |
| 10-30 05:19 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-30 05:19 | +10 stop | XRP | UP | 0.69 | 0.46 | -2.63 |
| 10-30 05:19 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 05:19 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 05:19 | +5 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 05:18 | +10 stop | SOL | UP | 0.71 | 0.50 | -2.43 |
