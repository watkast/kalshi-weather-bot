# Range-Scalp Bot

*Updated Wed Oct 14 13:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16040 | 13894 | 2146 (27) | 0 | $-5079.19 | -5.0% |
| **+10¢** | 12136 | 9650 | 2486 (39) | 1 | $-4673.89 | -6.1% |
| **+15¢** | 10202 | 7530 | 2672 (58) | 1 | $-4204.04 | -6.6% |
| **+20¢** | 9072 | 6269 | 2803 (75) | 1 | $-3734.42 | -6.6% |
| **+10¢ (15¢ stop)** | 19746 | 19696 | 50 (29) | 1 | $-7610.67 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 13:32 | +10 stop | ZEC | UP | 0.71 | open |  |
| 10-14 13:32 | +20 | ZEC | UP | 0.71 | open |  |
| 10-14 13:32 | +15 | ZEC | UP | 0.71 | open |  |
| 10-14 13:32 | +10 | ZEC | UP | 0.71 | open |  |
| 10-14 13:32 | +5 | ZEC | UP | 0.71 | 0.80 | 0.63 |
| 10-14 13:26 | +10 stop | XRP | UP | 0.71 | 0.88 | 1.47 |
| 10-14 13:26 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-14 13:26 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-14 13:25 | +10 stop | DOGE | DOWN | 0.47 | 0.60 | 0.95 |
| 10-14 13:25 | +20 | DOGE | DOWN | 0.48 | yes | -4.98 |
| 10-14 13:25 | +15 | DOGE | DOWN | 0.48 | yes | -4.98 |
| 10-14 13:25 | +10 | DOGE | DOWN | 0.48 | 0.60 | 0.85 |
| 10-14 13:25 | +5 | DOGE | DOWN | 0.48 | 0.60 | 0.85 |
| 10-14 13:25 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-14 13:25 | +20 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-14 13:25 | +15 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-14 13:25 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-14 13:25 | +5 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-14 13:25 | +10 stop | ETH | DOWN | 0.60 | 0.29 | -3.42 |
| 10-14 13:25 | +5 | ETH | DOWN | 0.60 | yes | -6.17 |
| 10-14 13:24 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-14 13:24 | +10 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-14 13:24 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 10-14 13:24 | +10 stop | BTC | DOWN | 0.58 | 0.39 | -2.25 |
| 10-14 13:24 | +5 | BNB | DOWN | 0.66 | yes | -6.76 |
| 10-14 13:24 | +5 | SOL | DOWN | 0.68 | yes | -6.96 |
| 10-14 13:23 | +10 stop | SOL | DOWN | 0.60 | 0.31 | -3.18 |
| 10-14 13:23 | +20 | SOL | DOWN | 0.60 | yes | -6.13 |
| 10-14 13:23 | +15 | SOL | DOWN | 0.60 | yes | -6.13 |
| 10-14 13:23 | +10 | SOL | DOWN | 0.60 | yes | -6.17 |
| 10-14 13:23 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-14 13:23 | +10 stop | BNB | DOWN | 0.65 | 0.38 | -3.03 |
| 10-14 13:23 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 10-14 13:22 | +10 stop | ZEC | DOWN | 0.56 | 0.25 | -3.42 |
| 10-14 13:22 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-14 13:21 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-14 13:20 | +10 stop | NEAR | DOWN | 0.63 | 0.37 | -2.94 |
| 10-14 13:20 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-14 13:20 | +5 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 10-14 13:19 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
