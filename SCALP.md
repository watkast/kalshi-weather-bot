# Range-Scalp Bot

*Updated Wed Oct 07 13:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6491 | 5642 | 849 (9) | 7 | $-1914.53 | -4.7% |
| **+10¢** | 4929 | 3932 | 997 (16) | 8 | $-1786.46 | -5.8% |
| **+15¢** | 4138 | 3084 | 1054 (20) | 8 | $-1499.10 | -5.8% |
| **+20¢** | 3700 | 2598 | 1102 (27) | 8 | $-1206.98 | -5.2% |
| **+10¢ (15¢ stop)** | 7888 | 7873 | 15 (9) | 0 | $-2780.11 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 13:36 | +10 stop | BTC | UP | 0.63 | 0.44 | -2.25 |
| 10-07 13:36 | +10 stop | HYPE | UP | 0.71 | 0.25 | -4.89 |
| 10-07 13:36 | +20 | HYPE | UP | 0.70 | open |  |
| 10-07 13:36 | +15 | HYPE | UP | 0.70 | open |  |
| 10-07 13:36 | +10 | HYPE | UP | 0.70 | open |  |
| 10-07 13:36 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-07 13:36 | +10 stop | DOGE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-07 13:36 | +10 stop | SOL | DOWN | 0.71 | 0.48 | -2.63 |
| 10-07 13:35 | +10 stop | BTC | DOWN | 0.49 | 0.63 | 1.05 |
| 10-07 13:35 | +5 | HYPE | UP | 0.64 | 0.78 | 1.10 |
| 10-07 13:35 | +10 stop | ETH | DOWN | 0.58 | 0.38 | -2.35 |
| 10-07 13:35 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-07 13:34 | +10 stop | NEAR | DOWN | 0.63 | 0.46 | -2.02 |
| 10-07 13:34 | +10 stop | HYPE | UP | 0.52 | 0.78 | 2.29 |
| 10-07 13:34 | +20 | HYPE | UP | 0.52 | 0.78 | 2.29 |
| 10-07 13:34 | +15 | HYPE | UP | 0.52 | 0.78 | 2.29 |
| 10-07 13:34 | +10 | HYPE | UP | 0.52 | 0.78 | 2.29 |
| 10-07 13:34 | +5 | HYPE | UP | 0.52 | 0.60 | 0.45 |
| 10-07 13:34 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-07 13:34 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-07 13:34 | +10 stop | ETH | UP | 0.64 | 0.38 | -2.94 |
| 10-07 13:34 | +10 | ETH | UP | 0.64 | open |  |
| 10-07 13:34 | +5 | ETH | UP | 0.64 | open |  |
| 10-07 13:34 | +20 | DOGE | UP | 0.61 | open |  |
| 10-07 13:34 | +15 | DOGE | UP | 0.61 | open |  |
| 10-07 13:34 | +5 | DOGE | UP | 0.61 | open |  |
| 10-07 13:33 | +10 stop | ZEC | DOWN | 0.53 | 0.70 | 1.37 |
| 10-07 13:33 | +15 | ZEC | DOWN | 0.53 | 0.70 | 1.37 |
| 10-07 13:33 | +10 | ZEC | DOWN | 0.53 | 0.70 | 1.37 |
| 10-07 13:33 | +5 | ZEC | DOWN | 0.53 | 0.70 | 1.37 |
| 10-07 13:32 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-07 13:32 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 10-07 13:32 | +20 | SOL | UP | 0.71 | open |  |
| 10-07 13:32 | +15 | SOL | UP | 0.71 | open |  |
| 10-07 13:32 | +10 | SOL | UP | 0.71 | open |  |
| 10-07 13:32 | +5 | SOL | UP | 0.71 | open |  |
| 10-07 13:31 | +10 stop | BTC | UP | 0.66 | 0.48 | -2.14 |
| 10-07 13:31 | +20 | BTC | UP | 0.66 | open |  |
| 10-07 13:31 | +15 | BTC | UP | 0.66 | open |  |
| 10-07 13:31 | +10 | BTC | UP | 0.66 | open |  |
