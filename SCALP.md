# Range-Scalp Bot

*Updated Sat Oct 17 10:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20817 | 18112 | 2705 (29) | 1 | $-6116.12 | -4.7% |
| **+10¢** | 15682 | 12565 | 3117 (41) | 1 | $-5409.01 | -5.5% |
| **+15¢** | 13115 | 9761 | 3354 (61) | 1 | $-4871.08 | -5.9% |
| **+20¢** | 11624 | 8112 | 3512 (80) | 1 | $-4298.96 | -5.9% |
| **+10¢ (15¢ stop)** | 25592 | 25542 | 50 (29) | 0 | $-9741.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 10:39 | +5 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-17 10:36 | +10 stop | HYPE | UP | 0.57 | 0.74 | 1.42 |
| 10-17 10:35 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-17 10:34 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.07 |
| 10-17 10:33 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 10-17 10:33 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-17 10:32 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-17 10:32 | +20 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 10-17 10:32 | +15 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-17 10:32 | +10 | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-17 10:32 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
| 10-17 10:31 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 10-17 10:31 | +20 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-17 10:31 | +15 | ZEC | UP | 0.59 | 0.81 | 1.87 |
| 10-17 10:31 | +10 | ZEC | UP | 0.59 | 0.72 | 0.93 |
| 10-17 10:31 | +5 | ZEC | UP | 0.60 | 0.72 | 0.88 |
| 10-17 10:31 | +10 stop | HYPE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-17 10:31 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-17 10:31 | +15 | HYPE | DOWN | 0.59 | open |  |
| 10-17 10:31 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-17 10:31 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-17 10:31 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 10-17 10:31 | +20 | XRP | UP | 0.61 | 0.87 | 2.35 |
| 10-17 10:31 | +15 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 10-17 10:31 | +10 | XRP | UP | 0.59 | 0.72 | 0.98 |
| 10-17 10:31 | +5 | XRP | UP | 0.59 | 0.65 | 0.27 |
| 10-17 10:31 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-17 10:31 | +20 | BNB | UP | 0.66 | 0.87 | 1.86 |
| 10-17 10:31 | +15 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-17 10:31 | +10 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-17 10:31 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-17 10:31 | +10 stop | DOGE | UP | 0.56 | 0.71 | 1.15 |
| 10-17 10:31 | +20 | DOGE | UP | 0.56 | 0.77 | 1.77 |
| 10-17 10:31 | +15 | DOGE | UP | 0.56 | 0.77 | 1.77 |
| 10-17 10:31 | +10 | DOGE | UP | 0.56 | 0.71 | 1.15 |
| 10-17 10:31 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 10-17 10:31 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 10-17 10:31 | +20 | BTC | UP | 0.54 | 0.79 | 2.20 |
| 10-17 10:31 | +15 | BTC | UP | 0.54 | 0.73 | 1.58 |
| 10-17 10:31 | +10 | BTC | UP | 0.54 | 0.65 | 0.76 |
