# Range-Scalp Bot

*Updated Sat Oct 31 14:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42348 | 36937 | 5411 (59) | 1 | $-11921.83 | -4.5% |
| **+10¢** | 31576 | 25312 | 6264 (81) | 1 | $-10715.12 | -5.4% |
| **+15¢** | 26409 | 19655 | 6754 (109) | 1 | $-9810.37 | -5.9% |
| **+20¢** | 23454 | 16377 | 7077 (141) | 1 | $-8667.58 | -5.9% |
| **+10¢ (15¢ stop)** | 51639 | 51560 | 79 (44) | 1 | $-19507.86 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 14:34 | +10 stop | ZEC | UP | 0.53 | open |  |
| 10-31 14:31 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-31 14:31 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-31 14:31 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-31 14:31 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-31 14:31 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-31 14:31 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 14:31 | +20 | HYPE | UP | 0.66 | 0.88 | 1.96 |
| 10-31 14:31 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-31 14:31 | +10 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-31 14:31 | +5 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 14:31 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 10-31 14:31 | +20 | XRP | UP | 0.67 | 0.88 | 1.86 |
| 10-31 14:31 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 10-31 14:31 | +10 | XRP | UP | 0.67 | 0.77 | 0.71 |
| 10-31 14:31 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-31 14:31 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-31 14:31 | +20 | NEAR | UP | 0.66 | 0.92 | 2.42 |
| 10-31 14:31 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-31 14:31 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-31 14:31 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-31 14:30 | +10 stop | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-31 14:30 | +20 | BNB | UP | 0.57 | 0.77 | 1.69 |
| 10-31 14:30 | +15 | BNB | UP | 0.57 | 0.77 | 1.69 |
| 10-31 14:30 | +10 | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-31 14:30 | +5 | BNB | UP | 0.57 | 0.63 | 0.25 |
| 10-31 14:28 | +10 stop | BNB | DOWN | 0.67 | 0.84 | 1.44 |
| 10-31 14:28 | +5 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-31 14:28 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 10-31 14:28 | +15 | BNB | UP | 0.57 | 0.88 | 2.82 |
| 10-31 14:28 | +10 | BNB | UP | 0.57 | 0.88 | 2.82 |
| 10-31 14:28 | +5 | BNB | UP | 0.57 | 0.65 | 0.44 |
| 10-31 14:27 | +10 stop | HYPE | UP | 0.69 | 0.33 | -3.91 |
| 10-31 14:27 | +20 | HYPE | UP | 0.69 | no | -7.05 |
| 10-31 14:27 | +15 | HYPE | UP | 0.68 | no | -6.99 |
| 10-31 14:27 | +10 | HYPE | UP | 0.68 | no | -6.99 |
| 10-31 14:27 | +5 | HYPE | UP | 0.68 | no | -6.99 |
| 10-31 14:26 | +10 stop | BNB | UP | 0.50 | 0.65 | 1.16 |
| 10-31 14:26 | +20 | BNB | UP | 0.50 | 0.88 | 3.54 |
| 10-31 14:26 | +15 | BNB | UP | 0.50 | 0.65 | 1.16 |
