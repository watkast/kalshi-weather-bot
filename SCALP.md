# Range-Scalp Bot

*Updated Sun Nov 15 19:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61138 | 53348 | 7790 (114) | 4 | $-16464.71 | -4.3% |
| **+10¢** | 45664 | 36536 | 9128 (153) | 5 | $-15470.16 | -5.4% |
| **+15¢** | 38246 | 28401 | 9845 (191) | 5 | $-14125.09 | -5.9% |
| **+20¢** | 34085 | 23758 | 10327 (243) | 7 | $-12404.35 | -5.8% |
| **+10¢ (15¢ stop)** | 74401 | 74249 | 152 (90) | 3 | $-27367.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 19:39 | +5 | DOGE | UP | 0.65 | open |  |
| 11-15 19:39 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-15 19:38 | +10 stop | ZEC | UP | 0.58 | 0.74 | 1.28 |
| 11-15 19:38 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 11-15 19:38 | +10 stop | DOGE | UP | 0.61 | open |  |
| 11-15 19:38 | +5 | DOGE | UP | 0.63 | 0.69 | 0.32 |
| 11-15 19:37 | +10 stop | HYPE | DOWN | 0.55 | 0.39 | -1.95 |
| 11-15 19:37 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 11-15 19:37 | +10 stop | NEAR | DOWN | 0.63 | 0.45 | -2.15 |
| 11-15 19:37 | +10 stop | HYPE | UP | 0.57 | 0.37 | -2.35 |
| 11-15 19:37 | +15 | HYPE | UP | 0.55 | 0.73 | 1.48 |
| 11-15 19:37 | +10 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 11-15 19:37 | +5 | HYPE | UP | 0.61 | 0.69 | 0.48 |
| 11-15 19:37 | +10 stop | ZEC | DOWN | 0.68 | 0.48 | -2.34 |
| 11-15 19:37 | +10 stop | ETH | DOWN | 0.71 | 0.43 | -3.13 |
| 11-15 19:36 | +5 | DOGE | UP | 0.48 | 0.53 | 0.14 |
| 11-15 19:36 | +10 stop | BNB | DOWN | 0.55 | 0.39 | -1.95 |
| 11-15 19:36 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
| 11-15 19:35 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 11-15 19:35 | +10 stop | SOL | UP | 0.66 | 0.51 | -1.84 |
| 11-15 19:35 | +20 | SOL | UP | 0.65 | open |  |
| 11-15 19:35 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-15 19:35 | +10 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-15 19:35 | +5 | SOL | UP | 0.65 | 0.74 | 0.60 |
| 11-15 19:35 | +10 stop | NEAR | UP | 0.68 | 0.40 | -3.13 |
| 11-15 19:35 | +20 | NEAR | UP | 0.68 | open |  |
| 11-15 19:35 | +15 | NEAR | UP | 0.68 | open |  |
| 11-15 19:35 | +10 | NEAR | UP | 0.68 | open |  |
| 11-15 19:35 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 11-15 19:34 | +10 stop | BNB | DOWN | 0.45 | 0.56 | 0.74 |
| 11-15 19:33 | +10 stop | DOGE | UP | 0.68 | 0.48 | -2.34 |
| 11-15 19:33 | +10 | DOGE | UP | 0.67 | open |  |
| 11-15 19:33 | +5 | DOGE | UP | 0.67 | 0.73 | 0.30 |
| 11-15 19:33 | +5 | BTC | UP | 0.56 | open |  |
| 11-15 19:33 | +10 stop | ETH | UP | 0.67 | 0.50 | -2.04 |
| 11-15 19:33 | +5 | ETH | UP | 0.67 | open |  |
| 11-15 19:32 | +10 stop | BNB | UP | 0.62 | 0.43 | -2.25 |
| 11-15 19:32 | +10 | BNB | UP | 0.62 | open |  |
| 11-15 19:32 | +5 | BNB | UP | 0.62 | open |  |
| 11-15 19:32 | +10 stop | ZEC | UP | 0.69 | 0.54 | -1.83 |
