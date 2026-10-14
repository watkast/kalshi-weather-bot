# Range-Scalp Bot

*Updated Wed Oct 14 20:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16452 | 14252 | 2200 (28) | 2 | $-5209.15 | -5.0% |
| **+10¢** | 12450 | 9901 | 2549 (40) | 2 | $-4780.78 | -6.1% |
| **+15¢** | 10464 | 7729 | 2735 (59) | 2 | $-4275.52 | -6.5% |
| **+20¢** | 9304 | 6436 | 2868 (76) | 3 | $-3793.34 | -6.5% |
| **+10¢ (15¢ stop)** | 20271 | 20221 | 50 (29) | 2 | $-7836.20 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 20:16 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-14 20:16 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-14 20:16 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-14 20:16 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-14 20:16 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-14 20:16 | +10 stop | BTC | UP | 0.52 | open |  |
| 10-14 20:16 | +20 | BTC | UP | 0.52 | open |  |
| 10-14 20:16 | +15 | BTC | UP | 0.53 | open |  |
| 10-14 20:16 | +10 | BTC | UP | 0.53 | open |  |
| 10-14 20:16 | +5 | BTC | UP | 0.53 | open |  |
| 10-14 20:15 | +10 stop | DOGE | DOWN | 0.44 | 0.62 | 1.43 |
| 10-14 20:15 | +20 | DOGE | DOWN | 0.44 | open |  |
| 10-14 20:15 | +15 | DOGE | DOWN | 0.44 | 0.62 | 1.43 |
| 10-14 20:15 | +10 | DOGE | DOWN | 0.44 | 0.62 | 1.43 |
| 10-14 20:15 | +5 | DOGE | DOWN | 0.44 | 0.62 | 1.43 |
| 10-14 20:07 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-14 20:07 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-14 20:07 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 10-14 20:07 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-14 20:07 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 10-14 20:07 | +10 stop | ZEC | UP | 0.69 | 0.88 | 1.67 |
| 10-14 20:07 | +20 | ZEC | UP | 0.69 | 0.94 | 2.25 |
| 10-14 20:07 | +15 | ZEC | UP | 0.69 | 0.88 | 1.67 |
| 10-14 20:07 | +10 | ZEC | UP | 0.69 | 0.88 | 1.67 |
| 10-14 20:07 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 10-14 20:07 | +10 stop | XRP | DOWN | 0.59 | 0.23 | -3.90 |
| 10-14 20:04 | +10 stop | BNB | UP | 0.52 | 0.64 | 0.85 |
| 10-14 20:04 | +10 stop | HYPE | UP | 0.71 | 0.85 | 1.16 |
| 10-14 20:04 | +20 | HYPE | UP | 0.71 | 0.93 | 1.95 |
| 10-14 20:04 | +15 | HYPE | UP | 0.71 | 0.93 | 1.95 |
| 10-14 20:04 | +10 | HYPE | UP | 0.71 | 0.85 | 1.16 |
| 10-14 20:04 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 10-14 20:02 | +10 stop | XRP | UP | 0.62 | 0.44 | -2.15 |
| 10-14 20:02 | +20 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 10-14 20:02 | +15 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 10-14 20:02 | +10 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-14 20:02 | +5 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-14 20:01 | +10 stop | BNB | UP | 0.69 | 0.48 | -2.43 |
| 10-14 20:01 | +20 | BNB | UP | 0.69 | 0.90 | 1.90 |
| 10-14 20:01 | +15 | BNB | UP | 0.69 | 0.86 | 1.46 |
