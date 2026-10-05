# Range-Scalp Bot

*Updated Mon Oct 05 23:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4326 | 3728 | 598 (6) | 4 | $-1472.77 | -5.4% |
| **+10¢** | 3332 | 2639 | 693 (9) | 4 | $-1351.12 | -6.4% |
| **+15¢** | 2794 | 2062 | 732 (12) | 4 | $-1174.71 | -6.7% |
| **+20¢** | 2498 | 1735 | 763 (17) | 5 | $-1002.68 | -6.4% |
| **+10¢ (15¢ stop)** | 5313 | 5302 | 11 (6) | 2 | $-1901.10 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 23:25 | +5 | DOGE | UP | 0.60 | open |  |
| 10-05 23:25 | +10 stop | SOL | UP | 0.65 | open |  |
| 10-05 23:24 | +10 stop | DOGE | UP | 0.64 | open |  |
| 10-05 23:24 | +20 | DOGE | UP | 0.64 | open |  |
| 10-05 23:24 | +5 | DOGE | UP | 0.57 | 0.66 | 0.56 |
| 10-05 23:24 | +5 | DOGE | DOWN | 0.47 | 0.58 | 0.74 |
| 10-05 23:23 | +10 stop | SOL | DOWN | 0.71 | 0.51 | -2.33 |
| 10-05 23:23 | +10 stop | BNB | UP | 0.70 | 0.82 | 0.94 |
| 10-05 23:23 | +10 stop | DOGE | DOWN | 0.60 | 0.35 | -2.83 |
| 10-05 23:23 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-05 23:22 | +10 stop | DOGE | DOWN | 0.46 | 0.60 | 1.05 |
| 10-05 23:22 | +5 | DOGE | DOWN | 0.46 | 0.60 | 1.05 |
| 10-05 23:21 | +10 stop | ETH | UP | 0.59 | 0.74 | 1.19 |
| 10-05 23:21 | +5 | DOGE | DOWN | 0.48 | 0.57 | 0.54 |
| 10-05 23:21 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-05 23:20 | +10 stop | HYPE | UP | 0.71 | 0.56 | -1.83 |
| 10-05 23:20 | +10 | HYPE | UP | 0.71 | open |  |
| 10-05 23:20 | +5 | HYPE | UP | 0.70 | open |  |
| 10-05 23:20 | +5 | ZEC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-05 23:20 | +10 stop | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-05 23:19 | +5 | HYPE | DOWN | 0.42 | 0.64 | 1.85 |
| 10-05 23:19 | +10 stop | BNB | DOWN | 0.67 | 0.52 | -1.84 |
| 10-05 23:19 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-05 23:19 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-05 23:19 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-05 23:19 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-05 23:19 | +10 stop | DOGE | UP | 0.37 | 0.56 | 1.55 |
| 10-05 23:19 | +20 | DOGE | UP | 0.37 | 0.64 | 2.36 |
| 10-05 23:19 | +15 | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 10-05 23:19 | +10 | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 10-05 23:19 | +5 | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 10-05 23:18 | +10 stop | SOL | UP | 0.62 | 0.29 | -3.62 |
| 10-05 23:18 | +10 | SOL | UP | 0.62 | open |  |
| 10-05 23:18 | +5 | SOL | UP | 0.62 | open |  |
| 10-05 23:18 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-05 23:18 | +20 | BTC | UP | 0.63 | 0.85 | 1.94 |
| 10-05 23:18 | +15 | BTC | UP | 0.63 | 0.79 | 1.31 |
| 10-05 23:18 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-05 23:18 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-05 23:18 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
