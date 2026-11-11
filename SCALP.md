# Range-Scalp Bot

*Updated Wed Nov 11 11:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55778 | 48646 | 7132 (94) | 4 | $-15215.82 | -4.3% |
| **+10¢** | 41675 | 33357 | 8318 (124) | 4 | $-14149.42 | -5.4% |
| **+15¢** | 34941 | 25967 | 8974 (158) | 4 | $-12925.86 | -5.9% |
| **+20¢** | 31119 | 21706 | 9413 (208) | 4 | $-11290.10 | -5.8% |
| **+10¢ (15¢ stop)** | 67954 | 67833 | 121 (73) | 1 | $-24998.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 11:54 | +10 stop | XRP | UP | 0.60 | 0.43 | -2.04 |
| 11-11 11:54 | +10 stop | BTC | UP | 0.60 | open |  |
| 11-11 11:54 | +10 stop | ZEC | UP | 0.54 | 0.39 | -1.85 |
| 11-11 11:52 | +10 stop | BTC | UP | 0.70 | 0.48 | -2.53 |
| 11-11 11:52 | +5 | BTC | UP | 0.70 | open |  |
| 11-11 11:51 | +10 stop | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 11:50 | +5 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 11-11 11:49 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 11-11 11:49 | +10 stop | XRP | UP | 0.66 | 0.81 | 1.23 |
| 11-11 11:49 | +5 | BTC | UP | 0.67 | 0.74 | 0.40 |
| 11-11 11:49 | +10 stop | HYPE | UP | 0.64 | 0.82 | 1.52 |
| 11-11 11:49 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 11:49 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 11:49 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-11 11:48 | +10 stop | BNB | UP | 0.61 | 0.81 | 1.68 |
| 11-11 11:48 | +20 | BNB | UP | 0.61 | 0.82 | 1.78 |
| 11-11 11:48 | +15 | BNB | UP | 0.61 | 0.81 | 1.76 |
| 11-11 11:48 | +10 | BNB | UP | 0.60 | 0.81 | 1.78 |
| 11-11 11:48 | +5 | BNB | UP | 0.61 | 0.66 | 0.21 |
| 11-11 11:48 | +5 | ETH | UP | 0.61 | 0.70 | 0.58 |
| 11-11 11:48 | +5 | SOL | UP | 0.61 | 0.69 | 0.48 |
| 11-11 11:47 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.25 |
| 11-11 11:47 | +10 stop | BTC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-11 11:47 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-11 11:47 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-11 11:47 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-11 11:47 | +5 | BTC | DOWN | 0.56 | 0.62 | 0.25 |
| 11-11 11:47 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.95 |
| 11-11 11:47 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-11 11:47 | +15 | HYPE | DOWN | 0.64 | open |  |
| 11-11 11:47 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-11 11:47 | +5 | HYPE | DOWN | 0.64 | open |  |
| 11-11 11:46 | +10 stop | ETH | UP | 0.50 | 0.64 | 1.05 |
| 11-11 11:46 | +20 | ETH | UP | 0.50 | 0.70 | 1.67 |
| 11-11 11:46 | +15 | ETH | UP | 0.52 | 0.70 | 1.47 |
| 11-11 11:46 | +10 | ETH | UP | 0.52 | 0.64 | 0.85 |
| 11-11 11:46 | +5 | ETH | UP | 0.51 | 0.56 | 0.14 |
| 11-11 11:46 | +10 stop | ZEC | DOWN | 0.64 | 0.32 | -3.50 |
| 11-11 11:46 | +20 | ZEC | DOWN | 0.64 | open |  |
| 11-11 11:46 | +15 | ZEC | DOWN | 0.64 | open |  |
