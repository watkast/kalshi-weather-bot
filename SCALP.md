# Range-Scalp Bot

*Updated Fri Nov 13 08:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58022 | 50622 | 7400 (102) | 1 | $-15697.72 | -4.3% |
| **+10¢** | 43347 | 34698 | 8649 (134) | 1 | $-14659.60 | -5.4% |
| **+15¢** | 36342 | 27031 | 9311 (168) | 1 | $-13209.72 | -5.8% |
| **+20¢** | 32378 | 22604 | 9774 (219) | 2 | $-11582.24 | -5.7% |
| **+10¢ (15¢ stop)** | 70701 | 70572 | 129 (79) | 1 | $-26009.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 08:40 | +5 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 11-13 08:40 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 11-13 08:40 | +10 stop | ZEC | DOWN | 0.56 | 0.30 | -2.93 |
| 11-13 08:39 | +5 | ETH | UP | 0.62 | 0.71 | 0.58 |
| 11-13 08:38 | +10 stop | SOL | UP | 0.59 | 0.84 | 2.23 |
| 11-13 08:38 | +20 | SOL | UP | 0.59 | 0.84 | 2.23 |
| 11-13 08:38 | +15 | SOL | UP | 0.58 | 0.84 | 2.32 |
| 11-13 08:38 | +10 | SOL | UP | 0.58 | 0.84 | 2.32 |
| 11-13 08:38 | +5 | SOL | UP | 0.58 | 0.63 | 0.15 |
| 11-13 08:38 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-13 08:38 | +20 | XRP | UP | 0.71 | open |  |
| 11-13 08:38 | +15 | XRP | UP | 0.71 | open |  |
| 11-13 08:38 | +10 stop | ZEC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-13 08:38 | +10 | XRP | UP | 0.71 | open |  |
| 11-13 08:38 | +5 | XRP | UP | 0.71 | open |  |
| 11-13 08:38 | +10 stop | ETH | UP | 0.56 | 0.71 | 1.17 |
| 11-13 08:38 | +20 | ETH | UP | 0.56 | 0.76 | 1.69 |
| 11-13 08:38 | +15 | ETH | UP | 0.56 | 0.71 | 1.17 |
| 11-13 08:38 | +10 | ETH | UP | 0.56 | 0.71 | 1.17 |
| 11-13 08:38 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 11-13 08:36 | +10 stop | ZEC | UP | 0.71 | 0.48 | -2.63 |
| 11-13 08:35 | +10 stop | BTC | UP | 0.62 | 0.76 | 1.10 |
| 11-13 08:35 | +10 stop | BNB | UP | 0.64 | 0.79 | 1.17 |
| 11-13 08:34 | +10 stop | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 11-13 08:34 | +10 stop | SOL | DOWN | 0.48 | 0.31 | -2.03 |
| 11-13 08:34 | +10 stop | BTC | DOWN | 0.53 | 0.38 | -1.85 |
| 11-13 08:34 | +10 stop | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 11-13 08:34 | +10 stop | ZEC | DOWN | 0.51 | 0.36 | -1.85 |
| 11-13 08:34 | +10 | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 11-13 08:33 | +5 | HYPE | UP | 0.69 | 0.76 | 0.42 |
| 11-13 08:33 | +5 | ZEC | UP | 0.64 | 0.75 | 0.79 |
| 11-13 08:33 | +10 stop | XRP | DOWN | 0.58 | 0.34 | -2.74 |
| 11-13 08:32 | +5 | HYPE | UP | 0.57 | 0.65 | 0.41 |
| 11-13 08:32 | +5 | ETH | UP | 0.52 | 0.58 | 0.24 |
| 11-13 08:32 | +10 stop | ZEC | UP | 0.71 | 0.47 | -2.73 |
| 11-13 08:32 | +20 | ZEC | UP | 0.69 | open |  |
| 11-13 08:32 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-13 08:32 | +10 | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 11-13 08:32 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 11-13 08:32 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.85 |
