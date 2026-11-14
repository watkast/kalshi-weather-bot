# Range-Scalp Bot

*Updated Sat Nov 14 05:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59078 | 51546 | 7532 (106) | 0 | $-15968.19 | -4.3% |
| **+10¢** | 44135 | 35329 | 8806 (139) | 5 | $-14936.93 | -5.4% |
| **+15¢** | 36981 | 27488 | 9493 (174) | 5 | $-13558.98 | -5.8% |
| **+20¢** | 32945 | 22977 | 9968 (226) | 6 | $-11956.29 | -5.8% |
| **+10¢ (15¢ stop)** | 71919 | 71781 | 138 (82) | 1 | $-26447.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 05:10 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 05:10 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-14 05:10 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-14 05:10 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-14 05:09 | +10 stop | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 05:09 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-14 05:09 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 05:09 | +10 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 05:09 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-14 05:09 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 11-14 05:09 | +10 stop | NEAR | UP | 0.70 | open |  |
| 11-14 05:09 | +10 stop | XRP | DOWN | 0.50 | 0.18 | -3.49 |
| 11-14 05:09 | +15 | XRP | DOWN | 0.50 | open |  |
| 11-14 05:09 | +10 | XRP | DOWN | 0.50 | open |  |
| 11-14 05:09 | +5 | XRP | DOWN | 0.50 | 0.58 | 0.44 |
| 11-14 05:09 | +5 | BTC | DOWN | 0.45 | 0.55 | 0.64 |
| 11-14 05:08 | +10 stop | BTC | DOWN | 0.55 | 0.33 | -2.54 |
| 11-14 05:08 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-14 05:08 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-14 05:08 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-14 05:08 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-14 05:08 | +10 stop | BNB | UP | 0.69 | 0.81 | 0.94 |
| 11-14 05:07 | +10 stop | BNB | DOWN | 0.56 | 0.39 | -2.05 |
| 11-14 05:07 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-14 05:07 | +10 stop | ZEC | DOWN | 0.58 | 0.38 | -2.35 |
| 11-14 05:07 | +10 stop | NEAR | DOWN | 0.63 | 0.41 | -2.54 |
| 11-14 05:06 | +10 stop | HYPE | DOWN | 0.58 | 0.38 | -2.35 |
| 11-14 05:06 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-14 05:05 | +10 stop | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 11-14 05:05 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 05:05 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 05:04 | +10 stop | ZEC | UP | 0.64 | 0.42 | -2.55 |
| 11-14 05:04 | +10 | ZEC | UP | 0.64 | 0.75 | 0.79 |
| 11-14 05:04 | +5 | DOGE | DOWN | 0.59 | 0.68 | 0.57 |
| 11-14 05:04 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 11-14 05:04 | +5 | DOGE | DOWN | 0.55 | 0.60 | 0.15 |
| 11-14 05:04 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-14 05:04 | +10 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 05:04 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 11-14 05:04 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
