# Range-Scalp Bot

*Updated Sun Oct 04 06:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1873 | 1611 | 262 (3) | 2 | $-660.34 | -5.6% |
| **+10¢** | 1451 | 1161 | 290 (4) | 3 | $-484.64 | -5.3% |
| **+15¢** | 1221 | 914 | 307 (5) | 4 | $-421.33 | -5.5% |
| **+20¢** | 1076 | 750 | 326 (7) | 5 | $-418.24 | -6.2% |
| **+10¢ (15¢ stop)** | 2353 | 2352 | 1 (1) | 3 | $-974.34 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 06:19 | +10 stop | BNB | UP | 0.69 | open |  |
| 10-04 06:18 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-04 06:18 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-04 06:18 | +10 stop | BNB | DOWN | 0.52 | 0.34 | -2.14 |
| 10-04 06:17 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 10-04 06:16 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-04 06:16 | +20 | DOGE | UP | 0.71 | open |  |
| 10-04 06:16 | +15 | DOGE | UP | 0.71 | 0.88 | 1.47 |
| 10-04 06:16 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-04 06:16 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-04 06:16 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 10-04 06:16 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-04 06:16 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-04 06:16 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-04 06:16 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-04 06:16 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-04 06:16 | +20 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-04 06:16 | +15 | XRP | UP | 0.64 | 0.82 | 1.52 |
| 10-04 06:16 | +10 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-04 06:16 | +5 | XRP | UP | 0.64 | 0.73 | 0.59 |
| 10-04 06:16 | +10 stop | ZEC | UP | 0.48 | 0.30 | -2.13 |
| 10-04 06:16 | +20 | ZEC | UP | 0.48 | open |  |
| 10-04 06:16 | +15 | ZEC | UP | 0.49 | open |  |
| 10-04 06:16 | +10 | ZEC | UP | 0.49 | open |  |
| 10-04 06:16 | +5 | ZEC | UP | 0.49 | open |  |
| 10-04 06:16 | +10 stop | HYPE | UP | 0.54 | 0.68 | 1.06 |
| 10-04 06:16 | +20 | HYPE | UP | 0.54 | 0.74 | 1.68 |
| 10-04 06:16 | +15 | HYPE | UP | 0.54 | 0.73 | 1.58 |
| 10-04 06:16 | +10 | HYPE | UP | 0.54 | 0.68 | 1.06 |
| 10-04 06:16 | +5 | HYPE | UP | 0.54 | 0.59 | 0.15 |
| 10-04 06:16 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.87 |
| 10-04 06:16 | +20 | BNB | UP | 0.60 | open |  |
| 10-04 06:16 | +15 | BNB | UP | 0.60 | open |  |
| 10-04 06:16 | +10 | BNB | UP | 0.61 | open |  |
| 10-04 06:16 | +5 | BNB | UP | 0.61 | 0.66 | 0.17 |
| 10-04 06:16 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 06:16 | +20 | BTC | UP | 0.62 | open |  |
| 10-04 06:16 | +15 | BTC | UP | 0.62 | open |  |
| 10-04 06:16 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 06:16 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
