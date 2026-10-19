# Range-Scalp Bot

*Updated Mon Oct 19 11:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23901 | 20785 | 3116 (31) | 1 | $-7102.80 | -4.7% |
| **+10¢** | 17980 | 14389 | 3591 (45) | 1 | $-6326.14 | -5.6% |
| **+15¢** | 15062 | 11194 | 3868 (68) | 1 | $-5719.56 | -6.1% |
| **+20¢** | 13331 | 9285 | 4046 (86) | 3 | $-5090.29 | -6.1% |
| **+10¢ (15¢ stop)** | 29423 | 29372 | 51 (30) | 0 | $-11138.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 10:58 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-19 10:58 | +10 stop | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-19 10:57 | +10 stop | SOL | UP | 0.53 | 0.63 | 0.65 |
| 10-19 10:57 | +10 | SOL | UP | 0.53 | 0.63 | 0.65 |
| 10-19 10:57 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 10-19 10:57 | +10 stop | DOGE | UP | 0.71 | 0.51 | -2.33 |
| 10-19 10:57 | +5 | DOGE | UP | 0.71 | 0.85 | 1.16 |
| 10-19 10:56 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.15 |
| 10-19 10:56 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-19 10:56 | +10 stop | ZEC | UP | 0.64 | 0.38 | -2.94 |
| 10-19 10:55 | +5 | DOGE | UP | 0.71 | 0.76 | 0.23 |
| 10-19 10:55 | +10 stop | HYPE | UP | 0.60 | 0.42 | -2.15 |
| 10-19 10:55 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 10:54 | +10 stop | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-19 10:54 | +15 | SOL | DOWN | 0.51 | 0.70 | 1.57 |
| 10-19 10:54 | +10 | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-19 10:54 | +5 | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-19 10:54 | +10 stop | HYPE | DOWN | 0.46 | 0.57 | 0.70 |
| 10-19 10:54 | +5 | DOGE | UP | 0.68 | 0.74 | 0.31 |
| 10-19 10:54 | +10 stop | XRP | UP | 0.69 | 0.48 | -2.42 |
| 10-19 10:54 | +5 | ZEC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-19 10:54 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 10-19 10:54 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 10:54 | +20 | ETH | DOWN | 0.67 | 0.96 | 2.74 |
| 10-19 10:54 | +15 | ETH | DOWN | 0.67 | 0.85 | 1.55 |
| 10-19 10:54 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 10:54 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 10:53 | +10 stop | BTC | UP | 0.71 | 0.35 | -3.91 |
| 10-19 10:53 | +10 stop | ZEC | DOWN | 0.55 | 0.38 | -2.05 |
| 10-19 10:53 | +15 | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 10-19 10:53 | +10 | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 10-19 10:53 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-19 10:53 | +10 stop | BNB | UP | 0.59 | 0.72 | 0.98 |
| 10-19 10:53 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-19 10:53 | +15 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 10-19 10:53 | +10 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 10-19 10:53 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-19 10:52 | +10 stop | NEAR | DOWN | 0.64 | 0.46 | -2.15 |
| 10-19 10:52 | +10 stop | BNB | DOWN | 0.64 | 0.43 | -2.45 |
| 10-19 10:52 | +10 stop | XRP | DOWN | 0.64 | 0.29 | -3.82 |
