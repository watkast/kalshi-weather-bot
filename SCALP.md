# Range-Scalp Bot

*Updated Sun Oct 04 11:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2165 | 1870 | 295 (3) | 0 | $-707.40 | -5.2% |
| **+10¢** | 1687 | 1358 | 329 (4) | 0 | $-524.23 | -4.9% |
| **+15¢** | 1416 | 1067 | 349 (5) | 0 | $-448.93 | -5.0% |
| **+20¢** | 1250 | 882 | 368 (8) | 0 | $-401.27 | -5.1% |
| **+10¢ (15¢ stop)** | 2686 | 2685 | 1 (1) | 0 | $-1025.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 10:57 | +10 stop | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-04 10:57 | +5 | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-04 10:56 | +10 stop | HYPE | DOWN | 0.66 | 0.85 | 1.68 |
| 10-04 10:56 | +15 | HYPE | DOWN | 0.66 | 0.85 | 1.68 |
| 10-04 10:56 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-04 10:56 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-04 10:55 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-04 10:54 | +10 stop | ETH | UP | 0.70 | 0.47 | -2.63 |
| 10-04 10:54 | +10 | ETH | UP | 0.70 | no | -7.15 |
| 10-04 10:54 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-04 10:53 | +10 stop | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 10-04 10:53 | +10 stop | NEAR | DOWN | 0.32 | 0.53 | 1.76 |
| 10-04 10:52 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.98 |
| 10-04 10:52 | +20 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 10-04 10:52 | +15 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 10-04 10:52 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 10-04 10:52 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-04 10:52 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.94 |
| 10-04 10:51 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
| 10-04 10:51 | +10 stop | HYPE | DOWN | 0.56 | 0.35 | -2.44 |
| 10-04 10:51 | +15 | HYPE | DOWN | 0.56 | 0.72 | 1.27 |
| 10-04 10:51 | +10 | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-04 10:51 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-04 10:51 | +10 stop | NEAR | DOWN | 0.58 | 0.40 | -2.15 |
| 10-04 10:50 | +10 stop | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 10-04 10:48 | +10 stop | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-04 10:48 | +15 | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-04 10:48 | +10 | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-04 10:48 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-04 10:48 | +10 stop | NEAR | DOWN | 0.70 | 0.46 | -2.72 |
| 10-04 10:48 | +10 | NEAR | DOWN | 0.69 | yes | -7.08 |
| 10-04 10:48 | +5 | NEAR | DOWN | 0.70 | yes | -7.16 |
| 10-04 10:48 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 10-04 10:48 | +10 stop | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-04 10:48 | +10 stop | XRP | DOWN | 0.56 | 0.38 | -2.13 |
| 10-04 10:48 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.93 |
| 10-04 10:48 | +10 stop | BTC | DOWN | 0.68 | 0.51 | -2.04 |
| 10-04 10:48 | +20 | BTC | DOWN | 0.68 | 0.94 | 2.42 |
| 10-04 10:48 | +15 | BTC | DOWN | 0.68 | 0.94 | 2.42 |
| 10-04 10:48 | +10 | BTC | DOWN | 0.68 | 0.94 | 2.42 |
