# Range-Scalp Bot

*Updated Thu Nov 12 05:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56667 | 49398 | 7269 (98) | 4 | $-15625.43 | -4.4% |
| **+10¢** | 42349 | 33869 | 8480 (128) | 4 | $-14577.46 | -5.5% |
| **+15¢** | 35506 | 26376 | 9130 (162) | 4 | $-13220.74 | -5.9% |
| **+20¢** | 31631 | 22049 | 9582 (212) | 4 | $-11620.74 | -5.9% |
| **+10¢ (15¢ stop)** | 69091 | 68968 | 123 (73) | 4 | $-25518.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 05:16 | +10 stop | ZEC | UP | 0.66 | open |  |
| 11-12 05:16 | +20 | ZEC | UP | 0.66 | open |  |
| 11-12 05:16 | +15 | ZEC | UP | 0.66 | open |  |
| 11-12 05:16 | +10 | ZEC | UP | 0.66 | open |  |
| 11-12 05:16 | +5 | ZEC | UP | 0.65 | open |  |
| 11-12 05:16 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-12 05:16 | +20 | SOL | UP | 0.63 | open |  |
| 11-12 05:16 | +15 | SOL | UP | 0.63 | open |  |
| 11-12 05:16 | +10 | SOL | UP | 0.63 | open |  |
| 11-12 05:16 | +5 | SOL | UP | 0.63 | open |  |
| 11-12 05:16 | +10 stop | DOGE | UP | 0.62 | open |  |
| 11-12 05:16 | +20 | DOGE | UP | 0.62 | open |  |
| 11-12 05:16 | +15 | DOGE | UP | 0.63 | open |  |
| 11-12 05:16 | +10 | DOGE | UP | 0.63 | open |  |
| 11-12 05:16 | +5 | DOGE | UP | 0.63 | open |  |
| 11-12 05:16 | +10 stop | XRP | UP | 0.56 | open |  |
| 11-12 05:16 | +20 | XRP | UP | 0.56 | open |  |
| 11-12 05:16 | +15 | XRP | UP | 0.56 | open |  |
| 11-12 05:16 | +10 | XRP | UP | 0.56 | open |  |
| 11-12 05:16 | +5 | XRP | UP | 0.56 | open |  |
| 11-12 05:10 | +10 stop | NEAR | UP | 0.52 | 0.67 | 1.16 |
| 11-12 05:09 | +10 stop | NEAR | DOWN | 0.63 | 0.45 | -2.15 |
| 11-12 05:09 | +10 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 11-12 05:09 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 11-12 05:08 | +10 stop | ZEC | DOWN | 0.64 | 0.42 | -2.55 |
| 11-12 05:07 | +10 stop | ZEC | DOWN | 0.66 | 0.45 | -2.44 |
| 11-12 05:06 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 05:06 | +20 | NEAR | DOWN | 0.67 | 0.92 | 2.33 |
| 11-12 05:06 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 11-12 05:06 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 05:06 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 05:06 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 05:06 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-12 05:06 | +10 | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 05:06 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 11-12 05:03 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 05:02 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 05:02 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 11-12 05:02 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-12 05:02 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
