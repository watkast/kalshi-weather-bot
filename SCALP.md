# Range-Scalp Bot

*Updated Fri Nov 06 14:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49570 | 43204 | 6366 (76) | 0 | $-13975.03 | -4.5% |
| **+10¢** | 37002 | 29602 | 7400 (101) | 2 | $-12829.69 | -5.5% |
| **+15¢** | 30989 | 23018 | 7971 (130) | 5 | $-11722.33 | -6.0% |
| **+20¢** | 27546 | 19192 | 8354 (171) | 6 | $-10341.90 | -6.0% |
| **+10¢ (15¢ stop)** | 60400 | 60303 | 97 (57) | 0 | $-22337.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 14:01 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 14:01 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 14:01 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 14:01 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-06 14:01 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 11-06 14:01 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-06 14:00 | +10 stop | BNB | UP | 0.50 | 0.33 | -2.04 |
| 11-06 14:00 | +20 | BNB | UP | 0.50 | open |  |
| 11-06 14:00 | +15 | BNB | UP | 0.50 | open |  |
| 11-06 14:00 | +10 | BNB | UP | 0.50 | open |  |
| 11-06 14:00 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 11-06 14:00 | +10 stop | DOGE | UP | 0.49 | 0.62 | 0.95 |
| 11-06 14:00 | +20 | DOGE | UP | 0.49 | open |  |
| 11-06 14:00 | +15 | DOGE | UP | 0.49 | open |  |
| 11-06 14:00 | +10 | DOGE | UP | 0.49 | 0.62 | 0.95 |
| 11-06 14:00 | +5 | DOGE | UP | 0.48 | 0.62 | 1.05 |
| 11-06 14:00 | +10 stop | NEAR | UP | 0.48 | 0.33 | -1.84 |
| 11-06 14:00 | +20 | NEAR | UP | 0.48 | open |  |
| 11-06 14:00 | +15 | NEAR | UP | 0.48 | open |  |
| 11-06 14:00 | +10 | NEAR | UP | 0.48 | open |  |
| 11-06 14:00 | +5 | NEAR | UP | 0.48 | 0.53 | 0.14 |
| 11-06 14:00 | +10 stop | BTC | UP | 0.50 | 0.61 | 0.75 |
| 11-06 14:00 | +20 | BTC | UP | 0.48 | open |  |
| 11-06 14:00 | +15 | BTC | UP | 0.48 | open |  |
| 11-06 14:00 | +10 | BTC | UP | 0.48 | 0.61 | 0.95 |
| 11-06 14:00 | +5 | BTC | UP | 0.48 | 0.61 | 0.95 |
| 11-06 14:00 | +10 stop | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-06 14:00 | +20 | SOL | UP | 0.52 | open |  |
| 11-06 14:00 | +15 | SOL | UP | 0.52 | open |  |
| 11-06 14:00 | +10 | SOL | UP | 0.53 | 0.66 | 0.96 |
| 11-06 14:00 | +5 | SOL | UP | 0.53 | 0.66 | 0.96 |
| 11-06 14:00 | +10 stop | ZEC | UP | 0.48 | 0.65 | 1.36 |
| 11-06 14:00 | +20 | ZEC | UP | 0.49 | open |  |
| 11-06 14:00 | +15 | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-06 14:00 | +10 | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-06 14:00 | +5 | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-06 13:57 | +10 stop | DOGE | UP | 0.56 | 0.74 | 1.48 |
| 11-06 13:55 | +10 stop | DOGE | UP | 0.58 | 0.32 | -2.94 |
| 11-06 13:53 | +20 | SOL | UP | 0.67 | 0.88 | 1.86 |
| 11-06 13:53 | +15 | SOL | UP | 0.67 | 0.86 | 1.65 |
