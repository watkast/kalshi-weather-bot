# Range-Scalp Bot

*Updated Sat Oct 24 05:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31515 | 27471 | 4044 (40) | 2 | $-9048.27 | -4.6% |
| **+10¢** | 23566 | 18896 | 4670 (58) | 3 | $-8027.60 | -5.4% |
| **+15¢** | 19730 | 14710 | 5020 (81) | 4 | $-7162.57 | -5.8% |
| **+20¢** | 17483 | 12226 | 5257 (103) | 3 | $-6360.55 | -5.8% |
| **+10¢ (15¢ stop)** | 38679 | 38620 | 59 (32) | 0 | $-14764.05 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 05:43 | +10 stop | BTC | UP | 0.70 | 0.97 | 2.49 |
| 10-24 05:43 | +10 stop | DOGE | UP | 0.70 | 0.97 | 2.55 |
| 10-24 05:43 | +20 | DOGE | UP | 0.70 | 0.97 | 2.55 |
| 10-24 05:43 | +5 | DOGE | UP | 0.70 | 0.97 | 2.55 |
| 10-24 05:43 | +10 | DOGE | UP | 0.71 | 0.97 | 2.45 |
| 10-24 05:39 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 10-24 05:38 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.80 |
| 10-24 05:38 | +15 | DOGE | DOWN | 0.63 | open |  |
| 10-24 05:38 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.80 |
| 10-24 05:38 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-24 05:38 | +10 stop | NEAR | UP | 0.66 | 0.83 | 1.44 |
| 10-24 05:38 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-24 05:38 | +10 stop | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-24 05:38 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 10-24 05:38 | +10 stop | BTC | UP | 0.56 | 0.76 | 1.69 |
| 10-24 05:37 | +10 stop | DOGE | UP | 0.42 | 0.53 | 0.74 |
| 10-24 05:37 | +20 | DOGE | UP | 0.38 | 0.65 | 2.37 |
| 10-24 05:37 | +15 | DOGE | UP | 0.38 | 0.53 | 1.15 |
| 10-24 05:37 | +10 | DOGE | UP | 0.38 | 0.53 | 1.15 |
| 10-24 05:37 | +5 | DOGE | UP | 0.38 | 0.53 | 1.15 |
| 10-24 05:36 | +10 stop | BNB | UP | 0.59 | 0.71 | 0.88 |
| 10-24 05:36 | +5 | DOGE | UP | 0.64 | 0.85 | 1.84 |
| 10-24 05:36 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-24 05:35 | +5 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 10-24 05:35 | +10 stop | DOGE | UP | 0.62 | 0.85 | 2.04 |
| 10-24 05:35 | +10 stop | ETH | UP | 0.65 | 0.85 | 1.75 |
| 10-24 05:35 | +10 stop | BTC | UP | 0.62 | 0.81 | 1.62 |
| 10-24 05:34 | +10 stop | DOGE | DOWN | 0.48 | 0.58 | 0.64 |
| 10-24 05:34 | +5 | NEAR | UP | 0.56 | 0.63 | 0.35 |
| 10-24 05:34 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.34 |
| 10-24 05:34 | +10 stop | NEAR | DOWN | 0.48 | 0.31 | -2.03 |
| 10-24 05:34 | +20 | NEAR | DOWN | 0.48 | open |  |
| 10-24 05:34 | +15 | NEAR | DOWN | 0.48 | open |  |
| 10-24 05:34 | +10 | NEAR | DOWN | 0.47 | open |  |
| 10-24 05:34 | +5 | NEAR | DOWN | 0.48 | 0.57 | 0.55 |
| 10-24 05:33 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-24 05:33 | +5 | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 10-24 05:33 | +10 stop | XRP | UP | 0.60 | 0.45 | -1.85 |
| 10-24 05:33 | +5 | XRP | UP | 0.60 | 0.66 | 0.27 |
| 10-24 05:32 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
