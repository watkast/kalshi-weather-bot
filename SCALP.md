# Range-Scalp Bot

*Updated Mon Oct 19 09:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23809 | 20702 | 3107 (31) | 2 | $-7097.15 | -4.7% |
| **+10¢** | 17915 | 14333 | 3582 (45) | 2 | $-6333.29 | -5.6% |
| **+15¢** | 15003 | 11147 | 3856 (67) | 3 | $-5734.18 | -6.1% |
| **+20¢** | 13282 | 9249 | 4033 (86) | 5 | $-5085.19 | -6.1% |
| **+10¢ (15¢ stop)** | 29302 | 29251 | 51 (30) | 2 | $-11070.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 09:40 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 10-19 09:40 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-19 09:40 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-19 09:39 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-19 09:39 | +10 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-19 09:39 | +5 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-19 09:39 | +10 | BNB | UP | 0.62 | 0.78 | 1.27 |
| 10-19 09:39 | +5 | BNB | UP | 0.62 | 0.78 | 1.27 |
| 10-19 09:38 | +10 stop | SOL | DOWN | 0.43 | 0.57 | 1.04 |
| 10-19 09:38 | +10 | SOL | DOWN | 0.43 | 0.57 | 1.04 |
| 10-19 09:38 | +5 | BNB | UP | 0.58 | 0.65 | 0.34 |
| 10-19 09:38 | +10 stop | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-19 09:37 | +10 stop | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-19 09:37 | +10 | XRP | UP | 0.65 | 0.83 | 1.54 |
| 10-19 09:37 | +5 | XRP | UP | 0.65 | 0.74 | 0.60 |
| 10-19 09:37 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 10-19 09:37 | +5 | HYPE | UP | 0.62 | 0.70 | 0.48 |
| 10-19 09:37 | +10 stop | NEAR | DOWN | 0.51 | 0.64 | 0.95 |
| 10-19 09:37 | +15 | BNB | UP | 0.54 | 0.78 | 2.09 |
| 10-19 09:37 | +10 | BNB | UP | 0.54 | 0.65 | 0.76 |
| 10-19 09:37 | +5 | BNB | UP | 0.54 | 0.63 | 0.55 |
| 10-19 09:37 | +10 stop | SOL | UP | 0.47 | 0.61 | 1.05 |
| 10-19 09:37 | +10 | SOL | UP | 0.47 | 0.61 | 1.05 |
| 10-19 09:36 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 10-19 09:36 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 10-19 09:36 | +10 stop | BNB | UP | 0.67 | 0.52 | -1.84 |
| 10-19 09:35 | +10 stop | NEAR | DOWN | 0.59 | 0.41 | -2.12 |
| 10-19 09:35 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-19 09:34 | +5 | SOL | UP | 0.66 | open |  |
| 10-19 09:34 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-19 09:34 | +10 stop | DOGE | DOWN | 0.54 | 0.39 | -1.85 |
| 10-19 09:33 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 10-19 09:33 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-19 09:33 | +20 | BTC | UP | 0.61 | 0.82 | 1.82 |
| 10-19 09:33 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-19 09:33 | +10 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-19 09:33 | +5 | BTC | UP | 0.62 | 0.70 | 0.48 |
| 10-19 09:32 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
| 10-19 09:31 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 09:31 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
