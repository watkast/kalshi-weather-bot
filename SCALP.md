# Range-Scalp Bot

*Updated Mon Nov 16 22:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62371 | 54414 | 7957 (117) | 2 | $-16880.42 | -4.3% |
| **+10¢** | 46578 | 37267 | 9311 (159) | 2 | $-15759.74 | -5.4% |
| **+15¢** | 39030 | 28986 | 10044 (201) | 2 | $-14340.86 | -5.9% |
| **+20¢** | 34784 | 24251 | 10533 (256) | 3 | $-12531.61 | -5.7% |
| **+10¢ (15¢ stop)** | 75921 | 75765 | 156 (92) | 0 | $-28022.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 22:42 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-16 22:42 | +5 | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-16 22:42 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-16 22:41 | +10 stop | DOGE | UP | 0.48 | 0.87 | 3.64 |
| 11-16 22:41 | +10 stop | XRP | UP | 0.71 | 0.85 | 1.16 |
| 11-16 22:41 | +10 stop | ETH | DOWN | 0.71 | 0.13 | -6.03 |
| 11-16 22:41 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-16 22:40 | +5 | NEAR | UP | 0.61 | 0.75 | 1.09 |
| 11-16 22:40 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.85 |
| 11-16 22:40 | +10 stop | DOGE | DOWN | 0.52 | 0.35 | -2.04 |
| 11-16 22:39 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.33 |
| 11-16 22:39 | +10 stop | NEAR | UP | 0.60 | 0.75 | 1.19 |
| 11-16 22:39 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-16 22:39 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-16 22:38 | +10 stop | BTC | DOWN | 0.69 | 0.27 | -4.49 |
| 11-16 22:38 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-16 22:38 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-16 22:38 | +5 | DOGE | UP | 0.59 | 0.87 | 2.55 |
| 11-16 22:38 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 22:37 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 11-16 22:37 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.05 |
| 11-16 22:37 | +5 | NEAR | UP | 0.56 | 0.61 | 0.15 |
| 11-16 22:36 | +5 | DOGE | UP | 0.64 | 0.69 | 0.19 |
| 11-16 22:36 | +10 stop | BNB | UP | 0.58 | 0.30 | -3.13 |
| 11-16 22:36 | +10 stop | SOL | UP | 0.58 | 0.33 | -2.84 |
| 11-16 22:35 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-16 22:35 | +10 | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-16 22:35 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-16 22:34 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-16 22:34 | +10 stop | NEAR | UP | 0.70 | 0.50 | -2.33 |
| 11-16 22:34 | +15 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-16 22:34 | +10 | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-16 22:34 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 11-16 22:34 | +10 stop | XRP | DOWN | 0.54 | 0.73 | 1.58 |
| 11-16 22:34 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.37 |
| 11-16 22:32 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 11-16 22:32 | +10 stop | BNB | DOWN | 0.55 | 0.36 | -2.25 |
| 11-16 22:32 | +10 stop | XRP | DOWN | 0.67 | 0.46 | -2.44 |
| 11-16 22:32 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-16 22:32 | +20 | BTC | DOWN | 0.55 | open |  |
