# Range-Scalp Bot

*Updated Sun Oct 18 21:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22999 | 20005 | 2994 (30) | 0 | $-6809.85 | -4.7% |
| **+10¢** | 17301 | 13843 | 3458 (44) | 0 | $-6102.95 | -5.6% |
| **+15¢** | 14502 | 10771 | 3731 (66) | 2 | $-5567.87 | -6.1% |
| **+20¢** | 12840 | 8938 | 3902 (84) | 4 | $-4950.05 | -6.1% |
| **+10¢ (15¢ stop)** | 28300 | 28249 | 51 (30) | 0 | $-10815.26 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 21:32 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-18 21:32 | +10 stop | DOGE | UP | 0.71 | 0.85 | 1.16 |
| 10-18 21:32 | +20 | DOGE | UP | 0.71 | open |  |
| 10-18 21:32 | +15 | DOGE | UP | 0.71 | open |  |
| 10-18 21:32 | +10 | DOGE | UP | 0.71 | 0.85 | 1.16 |
| 10-18 21:32 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-18 21:32 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 10-18 21:31 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-18 21:31 | +20 | BNB | UP | 0.66 | 0.90 | 2.19 |
| 10-18 21:31 | +15 | BNB | UP | 0.66 | 0.84 | 1.54 |
| 10-18 21:31 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-18 21:31 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-18 21:31 | +10 stop | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-18 21:31 | +20 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-18 21:31 | +15 | XRP | UP | 0.62 | 0.78 | 1.30 |
| 10-18 21:31 | +10 | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-18 21:31 | +5 | XRP | UP | 0.62 | 0.69 | 0.38 |
| 10-18 21:31 | +10 stop | SOL | UP | 0.68 | 0.79 | 0.82 |
| 10-18 21:31 | +20 | SOL | UP | 0.69 | open |  |
| 10-18 21:31 | +15 | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-18 21:31 | +10 | SOL | UP | 0.68 | 0.79 | 0.82 |
| 10-18 21:31 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 10-18 21:31 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 10-18 21:31 | +20 | NEAR | UP | 0.69 | open |  |
| 10-18 21:31 | +15 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 10-18 21:31 | +10 | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 10-18 21:31 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 10-18 21:31 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 10-18 21:31 | +20 | HYPE | UP | 0.70 | open |  |
| 10-18 21:31 | +15 | HYPE | UP | 0.70 | open |  |
| 10-18 21:31 | +10 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-18 21:31 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 10-18 21:28 | +10 stop | SOL | UP | 0.43 | 0.54 | 0.74 |
| 10-18 21:28 | +10 stop | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 10-18 21:27 | +5 | HYPE | UP | 0.56 | 0.61 | 0.15 |
| 10-18 21:27 | +10 stop | HYPE | UP | 0.56 | 0.36 | -2.35 |
| 10-18 21:26 | +10 stop | XRP | DOWN | 0.37 | 0.54 | 1.35 |
| 10-18 21:26 | +20 | XRP | DOWN | 0.37 | 0.59 | 1.86 |
| 10-18 21:26 | +15 | XRP | DOWN | 0.37 | 0.54 | 1.35 |
| 10-18 21:26 | +10 | XRP | DOWN | 0.37 | 0.54 | 1.35 |
