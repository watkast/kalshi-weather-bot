# Range-Scalp Bot

*Updated Fri Nov 06 05:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49214 | 42885 | 6329 (75) | 3 | $-13944.73 | -4.5% |
| **+10¢** | 36747 | 29390 | 7357 (101) | 3 | $-12796.08 | -5.5% |
| **+15¢** | 30778 | 22858 | 7920 (130) | 5 | $-11661.08 | -6.0% |
| **+20¢** | 27359 | 19058 | 8301 (170) | 5 | $-10305.17 | -6.0% |
| **+10¢ (15¢ stop)** | 60009 | 59914 | 95 (57) | 3 | $-22218.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 05:04 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 11-06 05:04 | +10 stop | ZEC | UP | 0.58 | open |  |
| 11-06 05:04 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-06 05:04 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-06 05:04 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-06 05:03 | +5 | NEAR | DOWN | 0.53 | 0.65 | 0.86 |
| 11-06 05:03 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 11-06 05:03 | +15 | NEAR | DOWN | 0.57 | open |  |
| 11-06 05:03 | +10 | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 11-06 05:03 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.46 |
| 11-06 05:01 | +10 stop | ZEC | DOWN | 0.67 | 0.48 | -2.28 |
| 11-06 05:01 | +10 stop | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 05:01 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 05:01 | +15 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 05:01 | +10 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 05:01 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 11-06 05:01 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 05:01 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-06 05:01 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-06 05:01 | +10 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 05:01 | +5 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 05:01 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-06 05:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-06 05:01 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-06 05:01 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-06 05:01 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-06 05:01 | +10 stop | NEAR | DOWN | 0.65 | 0.81 | 1.32 |
| 11-06 05:01 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-06 05:01 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.32 |
| 11-06 05:01 | +10 | NEAR | DOWN | 0.65 | 0.81 | 1.32 |
| 11-06 05:01 | +5 | NEAR | DOWN | 0.65 | 0.81 | 1.32 |
| 11-06 05:00 | +10 stop | DOGE | UP | 0.57 | 0.39 | -2.15 |
| 11-06 05:00 | +20 | DOGE | UP | 0.57 | open |  |
| 11-06 05:00 | +15 | DOGE | UP | 0.57 | open |  |
| 11-06 05:00 | +10 | DOGE | UP | 0.57 | open |  |
| 11-06 05:00 | +5 | DOGE | UP | 0.57 | open |  |
| 11-06 05:00 | +10 stop | ZEC | UP | 0.55 | 0.38 | -2.05 |
| 11-06 05:00 | +20 | ZEC | UP | 0.55 | open |  |
| 11-06 05:00 | +15 | ZEC | UP | 0.57 | open |  |
| 11-06 05:00 | +10 | ZEC | UP | 0.57 | open |  |
