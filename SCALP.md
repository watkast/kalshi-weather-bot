# Range-Scalp Bot

*Updated Fri Nov 27 00:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73153 | 63846 | 9307 (158) | 4 | $-19524.15 | -4.2% |
| **+10¢** | 54538 | 43671 | 10867 (204) | 4 | $-18112.20 | -5.3% |
| **+15¢** | 45670 | 33962 | 11708 (262) | 4 | $-16227.15 | -5.7% |
| **+20¢** | 40645 | 28316 | 12329 (328) | 4 | $-14626.23 | -5.7% |
| **+10¢ (15¢ stop)** | 89103 | 88894 | 209 (128) | 0 | $-32886.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 00:58 | +10 stop | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-27 00:57 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-27 00:57 | +10 stop | BNB | UP | 0.68 | 0.34 | -3.72 |
| 11-27 00:56 | +10 stop | BTC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-27 00:56 | +10 stop | BNB | DOWN | 0.57 | 0.41 | -1.94 |
| 11-27 00:55 | +10 stop | SOL | DOWN | 0.62 | 0.73 | 0.76 |
| 11-27 00:53 | +10 stop | BTC | DOWN | 0.67 | 0.48 | -2.24 |
| 11-27 00:53 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-27 00:52 | +10 stop | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-27 00:52 | +10 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-27 00:52 | +5 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-27 00:52 | +10 stop | ZEC | UP | 0.60 | 0.70 | 0.68 |
| 11-27 00:51 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 11-27 00:50 | +5 | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-27 00:49 | +10 stop | ZEC | UP | 0.68 | 0.52 | -1.94 |
| 11-27 00:49 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-27 00:49 | +10 stop | HYPE | DOWN | 0.44 | 0.64 | 1.65 |
| 11-27 00:49 | +10 stop | XRP | DOWN | 0.54 | 0.37 | -2.05 |
| 11-27 00:49 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-27 00:49 | +20 | ETH | UP | 0.67 | 0.91 | 2.20 |
| 11-27 00:49 | +15 | ETH | UP | 0.67 | 0.83 | 1.34 |
| 11-27 00:49 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-27 00:49 | +5 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-27 00:49 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-27 00:48 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.14 |
| 11-27 00:48 | +10 stop | ZEC | DOWN | 0.60 | 0.37 | -2.64 |
| 11-27 00:48 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-27 00:48 | +15 | ZEC | DOWN | 0.60 | open |  |
| 11-27 00:48 | +10 | ZEC | DOWN | 0.60 | open |  |
| 11-27 00:48 | +5 | ZEC | DOWN | 0.60 | open |  |
| 11-27 00:48 | +10 stop | DOGE | UP | 0.51 | 0.31 | -2.33 |
| 11-27 00:47 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-27 00:47 | +5 | XRP | UP | 0.67 | 0.79 | 0.92 |
| 11-27 00:47 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-27 00:47 | +20 | NEAR | UP | 0.68 | 0.91 | 2.02 |
| 11-27 00:47 | +15 | NEAR | UP | 0.68 | 0.91 | 2.02 |
| 11-27 00:47 | +10 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 11-27 00:47 | +5 | NEAR | UP | 0.64 | 0.71 | 0.37 |
| 11-27 00:46 | +10 stop | HYPE | UP | 0.61 | 0.44 | -2.05 |
| 11-27 00:46 | +20 | HYPE | UP | 0.61 | 0.81 | 1.72 |
