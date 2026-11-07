# Range-Scalp Bot

*Updated Sat Nov 07 01:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50287 | 43839 | 6448 (76) | 4 | $-14109.67 | -4.5% |
| **+10¢** | 37526 | 30019 | 7507 (102) | 4 | $-13031.67 | -5.5% |
| **+15¢** | 31425 | 23335 | 8090 (131) | 4 | $-11941.47 | -6.1% |
| **+20¢** | 27936 | 19452 | 8484 (173) | 4 | $-10575.60 | -6.0% |
| **+10¢ (15¢ stop)** | 61223 | 61124 | 99 (58) | 1 | $-22679.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 01:38 | +5 | ZEC | UP | 0.64 | open |  |
| 11-07 01:37 | +5 | ZEC | UP | 0.51 | 0.60 | 0.55 |
| 11-07 01:36 | +10 stop | ZEC | UP | 0.60 | open |  |
| 11-07 01:36 | +10 | ZEC | UP | 0.60 | open |  |
| 11-07 01:36 | +5 | ZEC | UP | 0.60 | 0.69 | 0.58 |
| 11-07 01:35 | +10 stop | XRP | DOWN | 0.71 | 0.56 | -1.83 |
| 11-07 01:34 | +10 stop | XRP | UP | 0.67 | 0.41 | -2.88 |
| 11-07 01:34 | +10 | XRP | UP | 0.67 | open |  |
| 11-07 01:34 | +5 | XRP | UP | 0.67 | open |  |
| 11-07 01:34 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-07 01:34 | +20 | ZEC | UP | 0.62 | open |  |
| 11-07 01:34 | +15 | ZEC | UP | 0.62 | open |  |
| 11-07 01:34 | +10 | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-07 01:34 | +5 | ZEC | UP | 0.62 | 0.69 | 0.38 |
| 11-07 01:34 | +10 stop | DOGE | UP | 0.60 | 0.82 | 1.92 |
| 11-07 01:33 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 11-07 01:33 | +10 stop | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-07 01:33 | +10 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-07 01:32 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-07 01:32 | +5 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-07 01:32 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.69 |
| 11-07 01:32 | +20 | XRP | UP | 0.63 | open |  |
| 11-07 01:32 | +15 | XRP | UP | 0.63 | open |  |
| 11-07 01:32 | +10 | XRP | UP | 0.63 | 0.73 | 0.69 |
| 11-07 01:32 | +5 | XRP | UP | 0.63 | 0.72 | 0.58 |
| 11-07 01:32 | +10 stop | BNB | UP | 0.65 | 0.76 | 0.81 |
| 11-07 01:32 | +20 | BNB | UP | 0.65 | 0.86 | 1.85 |
| 11-07 01:32 | +15 | BNB | UP | 0.65 | 0.81 | 1.33 |
| 11-07 01:32 | +10 | BNB | UP | 0.65 | 0.76 | 0.81 |
| 11-07 01:32 | +5 | BNB | UP | 0.65 | 0.70 | 0.19 |
| 11-07 01:31 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-07 01:31 | +20 | SOL | UP | 0.71 | 0.91 | 1.81 |
| 11-07 01:31 | +15 | SOL | UP | 0.71 | 0.89 | 1.58 |
| 11-07 01:31 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-07 01:31 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 11-07 01:31 | +10 stop | DOGE | DOWN | 0.55 | 0.33 | -2.54 |
| 11-07 01:31 | +20 | DOGE | DOWN | 0.55 | open |  |
| 11-07 01:31 | +15 | DOGE | DOWN | 0.55 | open |  |
| 11-07 01:31 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-07 01:31 | +5 | DOGE | DOWN | 0.55 | open |  |
