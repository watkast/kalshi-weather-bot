# Range-Scalp Bot

*Updated Sun Oct 11 03:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11326 | 9766 | 1560 (23) | 2 | $-3840.57 | -5.4% |
| **+10¢** | 8579 | 6766 | 1813 (36) | 3 | $-3650.30 | -6.8% |
| **+15¢** | 7231 | 5313 | 1918 (52) | 3 | $-3086.01 | -6.8% |
| **+20¢** | 6440 | 4444 | 1996 (66) | 3 | $-2588.85 | -6.4% |
| **+10¢ (15¢ stop)** | 13950 | 13909 | 41 (25) | 0 | $-5593.89 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 03:47 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-11 03:47 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.05 |
| 10-11 03:47 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 03:47 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 10-11 03:46 | +5 | XRP | UP | 0.44 | 0.60 | 1.25 |
| 10-11 03:45 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.95 |
| 10-11 03:45 | +20 | NEAR | UP | 0.61 | open |  |
| 10-11 03:45 | +15 | NEAR | UP | 0.61 | open |  |
| 10-11 03:45 | +10 | NEAR | UP | 0.61 | open |  |
| 10-11 03:45 | +5 | NEAR | UP | 0.61 | open |  |
| 10-11 03:45 | +10 stop | XRP | UP | 0.58 | 0.38 | -2.35 |
| 10-11 03:45 | +20 | XRP | UP | 0.58 | open |  |
| 10-11 03:45 | +15 | XRP | UP | 0.58 | open |  |
| 10-11 03:45 | +10 | XRP | UP | 0.58 | open |  |
| 10-11 03:45 | +5 | XRP | UP | 0.58 | 0.66 | 0.46 |
| 10-11 03:45 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-11 03:45 | +20 | BTC | DOWN | 0.55 | 0.79 | 2.10 |
| 10-11 03:45 | +15 | BTC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-11 03:45 | +10 | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-11 03:45 | +5 | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-11 03:45 | +10 stop | SOL | UP | 0.60 | 0.36 | -2.74 |
| 10-11 03:45 | +20 | SOL | UP | 0.60 | open |  |
| 10-11 03:45 | +15 | SOL | UP | 0.60 | open |  |
| 10-11 03:45 | +10 | SOL | UP | 0.60 | open |  |
| 10-11 03:45 | +5 | SOL | UP | 0.60 | open |  |
| 10-11 03:41 | +10 stop | NEAR | UP | 0.65 | 0.88 | 2.06 |
| 10-11 03:39 | +10 stop | XRP | DOWN | 0.57 | 0.78 | 1.79 |
| 10-11 03:38 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-11 03:36 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 10-11 03:32 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-11 03:32 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-11 03:32 | +10 stop | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-11 03:32 | +20 | BNB | UP | 0.66 | 0.89 | 2.07 |
| 10-11 03:32 | +15 | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-11 03:32 | +10 | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-11 03:32 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-11 03:31 | +5 | HYPE | DOWN | 0.65 | yes | -6.70 |
| 10-11 03:31 | +10 stop | XRP | DOWN | 0.69 | 0.49 | -2.33 |
| 10-11 03:31 | +20 | XRP | DOWN | 0.69 | 0.94 | 2.26 |
| 10-11 03:31 | +15 | XRP | DOWN | 0.69 | 0.94 | 2.26 |
