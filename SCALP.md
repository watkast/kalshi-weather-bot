# Range-Scalp Bot

*Updated Thu Oct 08 09:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7380 | 6394 | 986 (13) | 2 | $-2305.85 | -5.0% |
| **+10¢** | 5604 | 4440 | 1164 (22) | 2 | $-2254.24 | -6.4% |
| **+15¢** | 4699 | 3471 | 1228 (30) | 2 | $-1892.71 | -6.4% |
| **+20¢** | 4196 | 2922 | 1274 (37) | 2 | $-1510.78 | -5.7% |
| **+10¢ (15¢ stop)** | 8940 | 8913 | 27 (17) | 1 | $-3237.13 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 09:37 | +10 stop | ZEC | UP | 0.61 | open |  |
| 10-08 09:32 | +10 stop | ZEC | UP | 0.59 | 0.70 | 0.78 |
| 10-08 09:31 | +10 stop | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-08 09:31 | +20 | DOGE | UP | 0.60 | 0.83 | 2.03 |
| 10-08 09:31 | +15 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-08 09:31 | +10 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-08 09:31 | +5 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-08 09:31 | +10 stop | ETH | DOWN | 0.55 | 0.30 | -2.83 |
| 10-08 09:31 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-08 09:31 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-08 09:31 | +10 | ETH | DOWN | 0.55 | open |  |
| 10-08 09:31 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-08 09:31 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.08 |
| 10-08 09:31 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-08 09:31 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-08 09:31 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-08 09:31 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-08 09:28 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 09:28 | +10 stop | BTC | UP | 0.39 | 0.56 | 1.35 |
| 10-08 09:27 | +10 stop | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +10 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +5 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +10 stop | BTC | DOWN | 0.40 | 0.62 | 1.86 |
| 10-08 09:27 | +10 stop | BTC | UP | 0.47 | 0.62 | 1.15 |
| 10-08 09:26 | +10 stop | BTC | DOWN | 0.60 | 0.41 | -2.24 |
| 10-08 09:24 | +10 stop | XRP | UP | 0.55 | 0.82 | 2.41 |
| 10-08 09:24 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 10-08 09:24 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-08 09:24 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.98 |
| 10-08 09:24 | +20 | HYPE | UP | 0.62 | no | -6.40 |
| 10-08 09:24 | +15 | HYPE | UP | 0.62 | no | -6.40 |
| 10-08 09:24 | +10 | HYPE | UP | 0.62 | 0.73 | 0.76 |
| 10-08 09:24 | +5 | HYPE | UP | 0.62 | 0.69 | 0.35 |
| 10-08 09:23 | +10 stop | BNB | DOWN | 0.57 | 0.27 | -3.32 |
| 10-08 09:23 | +20 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +15 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +10 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +5 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:22 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-08 09:22 | +20 | DOGE | DOWN | 0.70 | yes | -7.15 |
