# Range-Scalp Bot

*Updated Wed Oct 21 15:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27358 | 23818 | 3540 (39) | 2 | $-8000.91 | -4.6% |
| **+10¢** | 20568 | 16480 | 4088 (55) | 4 | $-7071.57 | -5.5% |
| **+15¢** | 17226 | 12828 | 4398 (78) | 4 | $-6312.29 | -5.8% |
| **+20¢** | 15249 | 10640 | 4609 (98) | 4 | $-5667.43 | -5.9% |
| **+10¢ (15¢ stop)** | 33567 | 33508 | 59 (32) | 0 | $-12464.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 15:26 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-21 15:26 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.82 |
| 10-21 15:26 | +15 | ZEC | DOWN | 0.69 | 0.91 | 1.93 |
| 10-21 15:26 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 15:26 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.39 |
| 10-21 15:26 | +10 stop | NEAR | UP | 0.62 | 0.43 | -2.25 |
| 10-21 15:26 | +20 | NEAR | UP | 0.62 | open |  |
| 10-21 15:26 | +15 | NEAR | UP | 0.62 | open |  |
| 10-21 15:26 | +10 | NEAR | UP | 0.59 | open |  |
| 10-21 15:26 | +5 | NEAR | UP | 0.57 | open |  |
| 10-21 15:26 | +10 stop | BNB | UP | 0.52 | 0.63 | 0.75 |
| 10-21 15:26 | +20 | BNB | UP | 0.53 | open |  |
| 10-21 15:26 | +15 | BNB | UP | 0.56 | open |  |
| 10-21 15:26 | +10 | BNB | UP | 0.56 | open |  |
| 10-21 15:26 | +5 | BNB | UP | 0.56 | 0.63 | 0.35 |
| 10-21 15:24 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-21 15:23 | +10 stop | DOGE | UP | 0.70 | 0.93 | 2.10 |
| 10-21 15:23 | +10 stop | SOL | DOWN | 0.53 | 0.34 | -2.24 |
| 10-21 15:23 | +20 | SOL | DOWN | 0.52 | open |  |
| 10-21 15:23 | +15 | SOL | DOWN | 0.52 | open |  |
| 10-21 15:23 | +10 | SOL | DOWN | 0.52 | open |  |
| 10-21 15:23 | +5 | SOL | DOWN | 0.53 | 0.58 | 0.14 |
| 10-21 15:22 | +5 | DOGE | DOWN | 0.61 | open |  |
| 10-21 15:22 | +10 stop | DOGE | DOWN | 0.63 | 0.42 | -2.45 |
| 10-21 15:22 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-21 15:22 | +15 | DOGE | DOWN | 0.63 | open |  |
| 10-21 15:22 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-21 15:22 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-21 15:18 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-21 15:18 | +10 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-21 15:17 | +5 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-21 15:16 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-21 15:16 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 15:16 | +20 | NEAR | DOWN | 0.66 | 0.90 | 2.18 |
| 10-21 15:16 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-21 15:16 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 15:16 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 10-21 15:16 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 15:16 | +20 | XRP | DOWN | 0.60 | 0.86 | 2.34 |
| 10-21 15:16 | +15 | XRP | DOWN | 0.60 | 0.86 | 2.34 |
