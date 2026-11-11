# Range-Scalp Bot

*Updated Wed Nov 11 19:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56138 | 48958 | 7180 (94) | 2 | $-15339.20 | -4.3% |
| **+10¢** | 41946 | 33568 | 8378 (124) | 3 | $-14305.75 | -5.4% |
| **+15¢** | 35174 | 26143 | 9031 (158) | 3 | $-13004.53 | -5.9% |
| **+20¢** | 31331 | 21856 | 9475 (208) | 3 | $-11368.51 | -5.8% |
| **+10¢ (15¢ stop)** | 68397 | 68276 | 121 (73) | 0 | $-25172.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 19:58 | +10 stop | BTC | DOWN | 0.58 | 0.36 | -2.55 |
| 11-11 19:57 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-11 19:55 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-11 19:55 | +5 | SOL | UP | 0.66 | 0.75 | 0.60 |
| 11-11 19:54 | +15 | BNB | UP | 0.63 | 0.78 | 1.20 |
| 11-11 19:54 | +10 stop | BNB | UP | 0.61 | 0.78 | 1.40 |
| 11-11 19:54 | +10 | BNB | UP | 0.62 | 0.78 | 1.30 |
| 11-11 19:54 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 19:54 | +5 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-11 19:53 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-11 19:51 | +10 stop | BTC | UP | 0.57 | 0.39 | -2.15 |
| 11-11 19:50 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-11 19:50 | +10 | XRP | UP | 0.70 | 0.82 | 0.89 |
| 11-11 19:50 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 11-11 19:50 | +10 | BTC | UP | 0.64 | open |  |
| 11-11 19:49 | +5 | XRP | UP | 0.68 | 0.73 | 0.25 |
| 11-11 19:49 | +5 | BTC | UP | 0.64 | open |  |
| 11-11 19:49 | +10 stop | BNB | UP | 0.52 | 0.62 | 0.65 |
| 11-11 19:49 | +20 | BNB | UP | 0.52 | 0.78 | 2.29 |
| 11-11 19:49 | +15 | BNB | UP | 0.52 | 0.67 | 1.16 |
| 11-11 19:49 | +10 | BNB | UP | 0.52 | 0.62 | 0.65 |
| 11-11 19:49 | +5 | BNB | UP | 0.52 | 0.59 | 0.35 |
| 11-11 19:48 | +10 stop | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 11-11 19:48 | +10 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 11-11 19:48 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 11-11 19:48 | +5 | XRP | UP | 0.58 | 0.63 | 0.15 |
| 11-11 19:47 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 11-11 19:47 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-11 19:47 | +20 | HYPE | UP | 0.67 | 0.89 | 1.97 |
| 11-11 19:47 | +15 | HYPE | UP | 0.67 | 0.85 | 1.55 |
| 11-11 19:47 | +10 | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-11 19:47 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 11-11 19:47 | +10 stop | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-11 19:47 | +20 | BTC | UP | 0.56 | open |  |
| 11-11 19:47 | +15 | BTC | UP | 0.56 | open |  |
| 11-11 19:47 | +10 | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-11 19:47 | +5 | BTC | UP | 0.56 | 0.65 | 0.56 |
| 11-11 19:47 | +10 stop | ETH | UP | 0.60 | 0.44 | -1.95 |
| 11-11 19:47 | +20 | ETH | UP | 0.60 | open |  |
| 11-11 19:47 | +15 | ETH | UP | 0.60 | open |  |
