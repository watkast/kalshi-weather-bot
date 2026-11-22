# Range-Scalp Bot

*Updated Sun Nov 22 11:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68579 | 59837 | 8742 (142) | 1 | $-18478.68 | -4.3% |
| **+10¢** | 51206 | 40996 | 10210 (186) | 1 | $-17130.75 | -5.3% |
| **+15¢** | 42917 | 31913 | 11004 (237) | 1 | $-15363.38 | -5.7% |
| **+20¢** | 38206 | 26643 | 11563 (295) | 1 | $-13685.95 | -5.7% |
| **+10¢ (15¢ stop)** | 83534 | 83349 | 185 (116) | 0 | $-30777.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 11:40 | +10 stop | BTC | UP | 0.53 | 0.31 | -2.53 |
| 11-22 11:40 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 11:40 | +5 | ZEC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-22 11:40 | +10 stop | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 11-22 11:40 | +10 stop | NEAR | UP | 0.54 | 0.24 | -3.31 |
| 11-22 11:40 | +20 | NEAR | UP | 0.54 | open |  |
| 11-22 11:40 | +15 | NEAR | UP | 0.54 | open |  |
| 11-22 11:40 | +10 | NEAR | UP | 0.54 | open |  |
| 11-22 11:40 | +5 | NEAR | UP | 0.54 | open |  |
| 11-22 11:40 | +10 stop | BTC | UP | 0.53 | 0.64 | 0.75 |
| 11-22 11:39 | +10 stop | HYPE | UP | 0.49 | 0.26 | -2.59 |
| 11-22 11:39 | +10 stop | BNB | UP | 0.50 | 0.33 | -2.04 |
| 11-22 11:39 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 11-22 11:39 | +10 | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 11-22 11:39 | +10 stop | SOL | UP | 0.49 | 0.33 | -1.92 |
| 11-22 11:39 | +10 stop | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 11-22 11:39 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-22 11:38 | +10 stop | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-22 11:38 | +15 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-22 11:38 | +10 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-22 11:38 | +5 | XRP | DOWN | 0.57 | 0.65 | 0.46 |
| 11-22 11:38 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-22 11:38 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-22 11:38 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 11-22 11:37 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-22 11:37 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.41 |
| 11-22 11:37 | +10 stop | BTC | DOWN | 0.57 | 0.37 | -2.35 |
| 11-22 11:36 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.77 |
| 11-22 11:35 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-22 11:35 | +10 stop | BNB | DOWN | 0.68 | 0.40 | -3.13 |
| 11-22 11:35 | +10 stop | SOL | DOWN | 0.68 | 0.33 | -3.82 |
| 11-22 11:35 | +10 stop | BTC | UP | 0.51 | 0.35 | -1.94 |
| 11-22 11:35 | +10 stop | XRP | UP | 0.51 | 0.36 | -1.85 |
| 11-22 11:34 | +10 stop | ZEC | UP | 0.65 | 0.48 | -2.04 |
| 11-22 11:34 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-22 11:34 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-22 11:34 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-22 11:34 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-22 11:33 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-22 11:33 | +5 | ETH | DOWN | 0.56 | 0.68 | 0.86 |
