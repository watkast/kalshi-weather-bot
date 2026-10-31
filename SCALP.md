# Range-Scalp Bot

*Updated Sat Oct 31 17:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42556 | 37111 | 5445 (59) | 3 | $-12023.57 | -4.5% |
| **+10¢** | 31733 | 25434 | 6299 (81) | 4 | $-10793.42 | -5.4% |
| **+15¢** | 26540 | 19748 | 6792 (109) | 4 | $-9892.73 | -5.9% |
| **+20¢** | 23572 | 16451 | 7121 (141) | 4 | $-8783.69 | -5.9% |
| **+10¢ (15¢ stop)** | 51916 | 51837 | 79 (44) | 3 | $-19663.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 17:49 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-31 17:49 | +10 | XRP | UP | 0.64 | open |  |
| 10-31 17:49 | +5 | XRP | UP | 0.64 | open |  |
| 10-31 17:48 | +5 | ZEC | UP | 0.70 | open |  |
| 10-31 17:48 | +5 | HYPE | UP | 0.63 | open |  |
| 10-31 17:48 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.71 |
| 10-31 17:48 | +20 | XRP | UP | 0.58 | open |  |
| 10-31 17:48 | +15 | XRP | UP | 0.58 | open |  |
| 10-31 17:48 | +10 | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-31 17:48 | +5 | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-31 17:48 | +10 stop | HYPE | UP | 0.59 | open |  |
| 10-31 17:48 | +20 | HYPE | UP | 0.59 | open |  |
| 10-31 17:48 | +15 | HYPE | UP | 0.59 | open |  |
| 10-31 17:48 | +10 | HYPE | UP | 0.59 | open |  |
| 10-31 17:48 | +5 | HYPE | UP | 0.59 | 0.67 | 0.46 |
| 10-31 17:46 | +10 stop | ZEC | UP | 0.68 | open |  |
| 10-31 17:46 | +20 | ZEC | UP | 0.68 | open |  |
| 10-31 17:46 | +15 | ZEC | UP | 0.68 | open |  |
| 10-31 17:46 | +10 | ZEC | UP | 0.68 | open |  |
| 10-31 17:46 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 10-31 17:46 | +10 stop | NEAR | DOWN | 0.50 | 0.31 | -2.23 |
| 10-31 17:46 | +20 | NEAR | DOWN | 0.50 | open |  |
| 10-31 17:46 | +15 | NEAR | DOWN | 0.47 | open |  |
| 10-31 17:46 | +10 | NEAR | DOWN | 0.50 | open |  |
| 10-31 17:46 | +5 | NEAR | DOWN | 0.41 | 0.58 | 1.35 |
| 10-31 17:42 | +10 stop | NEAR | UP | 0.57 | 0.78 | 1.79 |
| 10-31 17:37 | +10 stop | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-31 17:37 | +10 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-31 17:37 | +5 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-31 17:37 | +10 stop | NEAR | DOWN | 0.60 | 0.31 | -3.22 |
| 10-31 17:37 | +20 | NEAR | DOWN | 0.60 | 0.98 | 3.61 |
| 10-31 17:37 | +15 | NEAR | DOWN | 0.60 | 0.98 | 3.61 |
| 10-31 17:37 | +10 | NEAR | DOWN | 0.60 | 0.98 | 3.61 |
| 10-31 17:37 | +5 | NEAR | DOWN | 0.60 | 0.98 | 3.61 |
| 10-31 17:35 | +10 stop | ETH | UP | 0.62 | 0.75 | 0.99 |
| 10-31 17:35 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-31 17:35 | +10 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-31 17:35 | +5 | BNB | UP | 0.59 | 0.68 | 0.57 |
| 10-31 17:34 | +10 stop | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 10-31 17:34 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.93 |
