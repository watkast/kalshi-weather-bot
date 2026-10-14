# Range-Scalp Bot

*Updated Wed Oct 14 21:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16577 | 14370 | 2207 (28) | 0 | $-5185.39 | -5.0% |
| **+10¢** | 12540 | 9983 | 2557 (40) | 0 | $-4737.06 | -6.0% |
| **+15¢** | 10537 | 7792 | 2745 (59) | 0 | $-4235.89 | -6.4% |
| **+20¢** | 9362 | 6485 | 2877 (76) | 0 | $-3747.61 | -6.4% |
| **+10¢ (15¢ stop)** | 20404 | 20354 | 50 (29) | 0 | $-7863.07 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 21:31 | +10 stop | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-14 21:31 | +20 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-14 21:31 | +15 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-14 21:31 | +10 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-14 21:31 | +5 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-14 21:30 | +10 stop | ZEC | UP | 0.56 | 0.75 | 1.58 |
| 10-14 21:30 | +20 | ZEC | UP | 0.56 | 0.82 | 2.31 |
| 10-14 21:30 | +15 | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-14 21:30 | +10 | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-14 21:30 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
| 10-14 21:30 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-14 21:30 | +20 | XRP | UP | 0.55 | 0.75 | 1.68 |
| 10-14 21:30 | +15 | XRP | UP | 0.55 | 0.75 | 1.68 |
| 10-14 21:30 | +10 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-14 21:30 | +5 | XRP | UP | 0.55 | 0.61 | 0.25 |
| 10-14 21:30 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-14 21:30 | +20 | BTC | UP | 0.70 | 0.90 | 1.79 |
| 10-14 21:30 | +15 | BTC | UP | 0.70 | 0.88 | 1.57 |
| 10-14 21:30 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-14 21:30 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-14 21:28 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-14 21:28 | +10 stop | HYPE | UP | 0.53 | 0.33 | -2.34 |
| 10-14 21:26 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |
| 10-14 21:26 | +10 stop | BNB | DOWN | 0.70 | 0.51 | -2.23 |
| 10-14 21:24 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.72 |
| 10-14 21:23 | +10 stop | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-14 21:23 | +10 stop | HYPE | DOWN | 0.70 | 0.54 | -1.93 |
| 10-14 21:22 | +10 stop | BNB | DOWN | 0.66 | 0.47 | -2.23 |
| 10-14 21:22 | +10 | BNB | DOWN | 0.66 | yes | -6.75 |
| 10-14 21:22 | +5 | BNB | DOWN | 0.66 | yes | -6.75 |
| 10-14 21:21 | +10 stop | XRP | DOWN | 0.47 | 0.32 | -1.84 |
| 10-14 21:21 | +10 stop | DOGE | DOWN | 0.61 | 0.34 | -3.03 |
| 10-14 21:21 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 10-14 21:20 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 21:20 | +10 stop | NEAR | DOWN | 0.58 | 0.35 | -2.63 |
| 10-14 21:20 | +5 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-14 21:18 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 10-14 21:18 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-14 21:18 | +15 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 10-14 21:18 | +5 | BTC | UP | 0.58 | 0.66 | 0.46 |
