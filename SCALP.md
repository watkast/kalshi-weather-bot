# Range-Scalp Bot

*Updated Fri Nov 20 16:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66400 | 57947 | 8453 (128) | 2 | $-17878.03 | -4.3% |
| **+10¢** | 49572 | 39689 | 9883 (170) | 5 | $-16655.44 | -5.3% |
| **+15¢** | 41571 | 30914 | 10657 (217) | 6 | $-14981.97 | -5.7% |
| **+20¢** | 37015 | 25823 | 11192 (273) | 8 | $-13271.86 | -5.7% |
| **+10¢ (15¢ stop)** | 80847 | 80681 | 166 (100) | 3 | $-29838.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 16:33 | +5 | HYPE | DOWN | 0.45 | 0.58 | 0.94 |
| 11-20 16:33 | +5 | BNB | DOWN | 0.48 | 0.56 | 0.44 |
| 11-20 16:33 | +10 stop | BTC | DOWN | 0.47 | 0.58 | 0.74 |
| 11-20 16:33 | +10 stop | ETH | DOWN | 0.49 | open |  |
| 11-20 16:32 | +10 stop | HYPE | DOWN | 0.54 | open |  |
| 11-20 16:32 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-20 16:32 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.25 |
| 11-20 16:32 | +10 stop | BNB | DOWN | 0.54 | open |  |
| 11-20 16:32 | +20 | BNB | DOWN | 0.53 | open |  |
| 11-20 16:32 | +15 | BNB | DOWN | 0.53 | open |  |
| 11-20 16:32 | +10 | BNB | DOWN | 0.54 | open |  |
| 11-20 16:32 | +5 | BNB | DOWN | 0.54 | 0.62 | 0.45 |
| 11-20 16:32 | +5 | DOGE | UP | 0.59 | 0.74 | 1.19 |
| 11-20 16:32 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 11-20 16:32 | +20 | XRP | UP | 0.62 | open |  |
| 11-20 16:32 | +15 | XRP | UP | 0.62 | open |  |
| 11-20 16:32 | +10 | XRP | UP | 0.62 | open |  |
| 11-20 16:32 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 11-20 16:31 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-20 16:31 | +10 stop | NEAR | UP | 0.57 | 0.73 | 1.28 |
| 11-20 16:31 | +10 | NEAR | UP | 0.57 | 0.73 | 1.28 |
| 11-20 16:31 | +5 | NEAR | UP | 0.54 | 0.73 | 1.58 |
| 11-20 16:31 | +10 stop | BTC | UP | 0.56 | 0.41 | -1.85 |
| 11-20 16:31 | +20 | BTC | UP | 0.56 | open |  |
| 11-20 16:31 | +15 | BTC | UP | 0.56 | open |  |
| 11-20 16:31 | +10 | BTC | UP | 0.56 | open |  |
| 11-20 16:31 | +5 | BTC | UP | 0.56 | open |  |
| 11-20 16:30 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-20 16:30 | +20 | ZEC | UP | 0.57 | 0.82 | 2.21 |
| 11-20 16:30 | +15 | ZEC | UP | 0.56 | 0.73 | 1.38 |
| 11-20 16:30 | +10 | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-20 16:30 | +5 | ZEC | UP | 0.56 | 0.61 | 0.15 |
| 11-20 16:30 | +10 stop | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-20 16:30 | +20 | HYPE | UP | 0.51 | open |  |
| 11-20 16:30 | +15 | HYPE | UP | 0.51 | open |  |
| 11-20 16:30 | +10 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-20 16:30 | +5 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-20 16:30 | +10 stop | DOGE | UP | 0.60 | 0.74 | 1.09 |
| 11-20 16:30 | +20 | DOGE | UP | 0.60 | open |  |
| 11-20 16:30 | +15 | DOGE | UP | 0.60 | open |  |
