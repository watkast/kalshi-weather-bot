# Range-Scalp Bot

*Updated Fri Oct 30 22:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41379 | 36115 | 5264 (54) | 3 | $-11549.07 | -4.4% |
| **+10¢** | 30845 | 24755 | 6090 (78) | 4 | $-10274.62 | -5.3% |
| **+15¢** | 25780 | 19219 | 6561 (106) | 5 | $-9324.41 | -5.8% |
| **+20¢** | 22882 | 16011 | 6871 (137) | 6 | $-8194.55 | -5.7% |
| **+10¢ (15¢ stop)** | 50443 | 50368 | 75 (41) | 1 | $-19053.86 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 22:57 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 10-30 22:57 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-30 22:56 | +10 stop | BNB | DOWN | 0.53 | 0.65 | 0.86 |
| 10-30 22:56 | +10 | BNB | DOWN | 0.53 | 0.65 | 0.86 |
| 10-30 22:56 | +5 | BNB | DOWN | 0.54 | 0.65 | 0.76 |
| 10-30 22:56 | +10 stop | SOL | DOWN | 0.64 | 0.42 | -2.55 |
| 10-30 22:55 | +10 stop | DOGE | DOWN | 0.71 | 0.50 | -2.43 |
| 10-30 22:55 | +10 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-30 22:55 | +5 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-30 22:54 | +10 stop | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-30 22:53 | +5 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-30 22:53 | +10 stop | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-30 22:53 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-30 22:52 | +10 stop | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-30 22:51 | +10 stop | ETH | UP | 0.54 | 0.22 | -3.51 |
| 10-30 22:51 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-30 22:51 | +5 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-30 22:51 | +10 stop | SOL | UP | 0.56 | 0.39 | -2.05 |
| 10-30 22:50 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 10-30 22:50 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-30 22:50 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 22:50 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 22:50 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-30 22:49 | +10 stop | HYPE | UP | 0.56 | 0.37 | -2.25 |
| 10-30 22:49 | +10 | HYPE | UP | 0.56 | open |  |
| 10-30 22:49 | +5 | HYPE | UP | 0.56 | open |  |
| 10-30 22:49 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-30 22:49 | +5 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-30 22:49 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-30 22:49 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-30 22:49 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-30 22:48 | +10 stop | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 10-30 22:48 | +20 | HYPE | UP | 0.51 | open |  |
| 10-30 22:48 | +15 | HYPE | UP | 0.51 | open |  |
| 10-30 22:48 | +10 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 10-30 22:48 | +5 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 10-30 22:48 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-30 22:48 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-30 22:48 | +10 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-30 22:48 | +10 stop | DOGE | DOWN | 0.57 | 0.42 | -1.86 |
