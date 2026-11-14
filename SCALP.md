# Range-Scalp Bot

*Updated Sat Nov 14 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58971 | 51452 | 7519 (106) | 6 | $-15938.52 | -4.3% |
| **+10¢** | 44062 | 35272 | 8790 (139) | 5 | $-14891.80 | -5.4% |
| **+15¢** | 36921 | 27446 | 9475 (174) | 5 | $-13511.55 | -5.8% |
| **+20¢** | 32891 | 22943 | 9948 (226) | 5 | $-11897.34 | -5.8% |
| **+10¢ (15¢ stop)** | 71807 | 71669 | 138 (82) | 0 | $-26390.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 03:57 | +10 stop | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-14 03:57 | +10 stop | SOL | UP | 0.28 | 0.63 | 3.18 |
| 11-14 03:57 | +10 | SOL | UP | 0.28 | 0.63 | 3.18 |
| 11-14 03:57 | +5 | SOL | UP | 0.28 | 0.63 | 3.18 |
| 11-14 03:56 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 11-14 03:56 | +20 | ETH | UP | 0.58 | open |  |
| 11-14 03:56 | +15 | ETH | UP | 0.62 | open |  |
| 11-14 03:56 | +10 | ETH | UP | 0.62 | open |  |
| 11-14 03:56 | +5 | ETH | UP | 0.61 | open |  |
| 11-14 03:56 | +10 stop | BNB | UP | 0.62 | 0.37 | -2.84 |
| 11-14 03:56 | +10 | BNB | UP | 0.63 | open |  |
| 11-14 03:56 | +5 | BNB | UP | 0.61 | open |  |
| 11-14 03:56 | +10 stop | XRP | DOWN | 0.66 | 0.87 | 1.86 |
| 11-14 03:55 | +10 stop | SOL | UP | 0.53 | 0.67 | 1.06 |
| 11-14 03:55 | +15 | SOL | UP | 0.56 | open |  |
| 11-14 03:55 | +10 | SOL | UP | 0.56 | 0.67 | 0.76 |
| 11-14 03:55 | +5 | SOL | UP | 0.55 | 0.67 | 0.86 |
| 11-14 03:55 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 03:54 | +10 stop | XRP | UP | 0.69 | 0.43 | -2.93 |
| 11-14 03:54 | +15 | XRP | UP | 0.67 | open |  |
| 11-14 03:54 | +10 | XRP | UP | 0.68 | open |  |
| 11-14 03:54 | +5 | XRP | UP | 0.68 | open |  |
| 11-14 03:53 | +10 stop | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 03:52 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 11-14 03:51 | +5 | HYPE | UP | 0.61 | open |  |
| 11-14 03:51 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 11-14 03:51 | +10 stop | ETH | UP | 0.70 | 0.86 | 1.36 |
| 11-14 03:51 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 11-14 03:50 | +10 stop | HYPE | DOWN | 0.53 | 0.34 | -2.25 |
| 11-14 03:50 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.25 |
| 11-14 03:49 | +10 stop | NEAR | UP | 0.64 | 0.38 | -2.94 |
| 11-14 03:49 | +20 | NEAR | UP | 0.64 | open |  |
| 11-14 03:49 | +15 | NEAR | UP | 0.64 | open |  |
| 11-14 03:49 | +10 | NEAR | UP | 0.64 | open |  |
| 11-14 03:49 | +5 | NEAR | UP | 0.64 | open |  |
| 11-14 03:49 | +5 | HYPE | UP | 0.50 | 0.67 | 1.36 |
| 11-14 03:49 | +10 stop | ZEC | DOWN | 0.62 | 0.93 | 2.87 |
| 11-14 03:49 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.73 |
| 11-14 03:49 | +10 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-14 03:49 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
