# Range-Scalp Bot

*Updated Tue Nov 03 00:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45370 | 39504 | 5866 (67) | 0 | $-13116.87 | -4.6% |
| **+10¢** | 33864 | 27067 | 6797 (89) | 0 | $-11991.30 | -5.6% |
| **+15¢** | 28326 | 21013 | 7313 (116) | 1 | $-11032.44 | -6.2% |
| **+20¢** | 25156 | 17497 | 7659 (151) | 1 | $-9799.65 | -6.2% |
| **+10¢ (15¢ stop)** | 55352 | 55265 | 87 (51) | 0 | $-20896.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 00:45 | +10 stop | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-03 00:45 | +20 | XRP | UP | 0.57 | open |  |
| 11-03 00:45 | +15 | XRP | UP | 0.57 | open |  |
| 11-03 00:45 | +10 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-03 00:45 | +5 | XRP | UP | 0.57 | 0.64 | 0.35 |
| 11-03 00:41 | +10 stop | ETH | UP | 0.69 | 0.25 | -4.69 |
| 11-03 00:41 | +10 | ETH | UP | 0.69 | no | -7.05 |
| 11-03 00:41 | +10 stop | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-03 00:41 | +20 | ZEC | DOWN | 0.71 | 0.94 | 2.05 |
| 11-03 00:41 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-03 00:41 | +10 | ZEC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-03 00:41 | +5 | ZEC | DOWN | 0.71 | 0.86 | 1.30 |
| 11-03 00:41 | +10 stop | BNB | UP | 0.57 | 0.67 | 0.66 |
| 11-03 00:41 | +5 | DOGE | UP | 0.62 | no | -6.37 |
| 11-03 00:41 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.48 |
| 11-03 00:40 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-03 00:40 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-03 00:40 | +10 stop | ZEC | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 00:40 | +5 | ZEC | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 00:40 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.17 |
| 11-03 00:40 | +10 stop | BNB | DOWN | 0.65 | 0.46 | -2.24 |
| 11-03 00:40 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-03 00:40 | +15 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-03 00:40 | +10 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-03 00:40 | +5 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-03 00:40 | +10 stop | DOGE | UP | 0.58 | 0.20 | -4.10 |
| 11-03 00:40 | +10 | DOGE | UP | 0.58 | no | -5.98 |
| 11-03 00:40 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-03 00:40 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.38 |
| 11-03 00:40 | +20 | HYPE | DOWN | 0.60 | 0.85 | 2.22 |
| 11-03 00:40 | +15 | HYPE | DOWN | 0.60 | 0.77 | 1.38 |
| 11-03 00:40 | +10 | HYPE | DOWN | 0.60 | 0.77 | 1.38 |
| 11-03 00:40 | +5 | HYPE | DOWN | 0.60 | 0.68 | 0.45 |
| 11-03 00:39 | +10 stop | ETH | UP | 0.53 | 0.65 | 0.86 |
| 11-03 00:39 | +15 | ETH | UP | 0.53 | no | -5.48 |
| 11-03 00:39 | +10 | ETH | UP | 0.53 | 0.65 | 0.86 |
| 11-03 00:39 | +5 | ETH | UP | 0.54 | 0.59 | 0.15 |
| 11-03 00:39 | +10 stop | SOL | UP | 0.67 | 0.88 | 1.86 |
| 11-03 00:39 | +20 | SOL | UP | 0.66 | 0.88 | 1.96 |
| 11-03 00:39 | +15 | SOL | UP | 0.66 | 0.88 | 1.96 |
