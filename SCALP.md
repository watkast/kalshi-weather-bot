# Range-Scalp Bot

*Updated Sun Oct 18 18:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22832 | 19876 | 2956 (29) | 0 | $-6655.17 | -4.6% |
| **+10¢** | 17174 | 13761 | 3413 (43) | 0 | $-5916.87 | -5.5% |
| **+15¢** | 14390 | 10706 | 3684 (64) | 0 | $-5399.00 | -6.0% |
| **+20¢** | 12741 | 8887 | 3854 (82) | 0 | $-4774.23 | -6.0% |
| **+10¢ (15¢ stop)** | 28091 | 28041 | 50 (29) | 0 | $-10732.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 18:49 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-18 18:47 | +10 stop | HYPE | UP | 0.68 | 0.81 | 0.99 |
| 10-18 18:47 | +20 | HYPE | UP | 0.68 | 0.89 | 1.83 |
| 10-18 18:47 | +15 | HYPE | UP | 0.68 | 0.85 | 1.41 |
| 10-18 18:47 | +10 | HYPE | UP | 0.67 | 0.81 | 1.18 |
| 10-18 18:47 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-18 18:46 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-18 18:46 | +20 | DOGE | UP | 0.69 | 0.91 | 2.02 |
| 10-18 18:46 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-18 18:46 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-18 18:46 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-18 18:46 | +10 stop | ZEC | UP | 0.65 | 0.81 | 1.33 |
| 10-18 18:46 | +20 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 10-18 18:46 | +15 | ZEC | UP | 0.65 | 0.81 | 1.33 |
| 10-18 18:46 | +10 | ZEC | UP | 0.65 | 0.81 | 1.33 |
| 10-18 18:46 | +5 | ZEC | UP | 0.65 | 0.74 | 0.60 |
| 10-18 18:42 | +5 | ZEC | DOWN | 0.39 | yes | -4.06 |
| 10-18 18:42 | +10 stop | ZEC | DOWN | 0.54 | 0.37 | -2.05 |
| 10-18 18:42 | +10 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 10-18 18:42 | +5 | ZEC | DOWN | 0.52 | 0.61 | 0.55 |
| 10-18 18:42 | +10 stop | HYPE | UP | 0.60 | 0.78 | 1.50 |
| 10-18 18:41 | +10 stop | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-18 18:41 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-18 18:41 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-18 18:41 | +10 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 10-18 18:41 | +5 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 10-18 18:40 | +10 stop | ZEC | DOWN | 0.51 | 0.64 | 0.95 |
| 10-18 18:40 | +20 | ZEC | DOWN | 0.51 | yes | -5.28 |
| 10-18 18:40 | +15 | ZEC | DOWN | 0.51 | yes | -5.28 |
| 10-18 18:40 | +10 | ZEC | DOWN | 0.51 | 0.64 | 0.95 |
| 10-18 18:40 | +5 | ZEC | DOWN | 0.51 | 0.64 | 0.95 |
| 10-18 18:39 | +10 stop | HYPE | UP | 0.66 | 0.89 | 2.03 |
| 10-18 18:38 | +10 stop | HYPE | DOWN | 0.66 | 0.44 | -2.57 |
| 10-18 18:38 | +20 | HYPE | DOWN | 0.66 | yes | -6.79 |
| 10-18 18:38 | +15 | HYPE | DOWN | 0.66 | yes | -6.79 |
| 10-18 18:38 | +10 | HYPE | DOWN | 0.66 | yes | -6.79 |
| 10-18 18:38 | +5 | HYPE | DOWN | 0.66 | yes | -6.79 |
| 10-18 18:27 | +10 | NEAR | UP | 0.70 | 0.80 | 0.74 |
| 10-18 18:27 | +5 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 10-18 18:27 | +10 stop | SOL | DOWN | 0.42 | 0.59 | 1.35 |
