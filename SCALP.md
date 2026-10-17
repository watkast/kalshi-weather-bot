# Range-Scalp Bot

*Updated Sat Oct 17 13:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21040 | 18308 | 2732 (29) | 1 | $-6156.38 | -4.6% |
| **+10¢** | 15838 | 12687 | 3151 (41) | 2 | $-5477.51 | -5.5% |
| **+15¢** | 13243 | 9852 | 3391 (61) | 2 | $-4950.67 | -6.0% |
| **+20¢** | 11739 | 8186 | 3553 (80) | 3 | $-4386.56 | -6.0% |
| **+10¢ (15¢ stop)** | 25853 | 25803 | 50 (29) | 0 | $-9836.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 13:42 | +10 | ZEC | DOWN | 0.68 | 0.90 | 1.98 |
| 10-17 13:42 | +5 | ZEC | DOWN | 0.69 | 0.90 | 1.89 |
| 10-17 13:42 | +10 stop | ZEC | DOWN | 0.68 | 0.90 | 1.98 |
| 10-17 13:42 | +15 | ZEC | DOWN | 0.68 | 0.90 | 1.98 |
| 10-17 13:39 | +10 stop | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 10-17 13:38 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-17 13:38 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-17 13:38 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-17 13:38 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-17 13:37 | +10 stop | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 10-17 13:36 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 10-17 13:36 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-17 13:36 | +5 | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 10-17 13:35 | +10 stop | HYPE | UP | 0.60 | 0.35 | -2.83 |
| 10-17 13:35 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 10-17 13:34 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 13:34 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.87 |
| 10-17 13:34 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 13:34 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 13:34 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-17 13:34 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-17 13:34 | +10 stop | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 10-17 13:34 | +15 | ZEC | UP | 0.61 | 0.76 | 1.20 |
| 10-17 13:34 | +10 | ZEC | UP | 0.60 | 0.73 | 0.99 |
| 10-17 13:34 | +5 | ZEC | UP | 0.60 | 0.67 | 0.37 |
| 10-17 13:34 | +10 stop | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-17 13:32 | +10 stop | NEAR | UP | 0.66 | 0.40 | -2.93 |
| 10-17 13:32 | +5 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-17 13:32 | +10 stop | XRP | UP | 0.63 | 0.47 | -1.95 |
| 10-17 13:32 | +20 | XRP | UP | 0.63 | open |  |
| 10-17 13:32 | +15 | XRP | UP | 0.64 | open |  |
| 10-17 13:32 | +10 | XRP | UP | 0.64 | open |  |
| 10-17 13:32 | +5 | XRP | UP | 0.64 | open |  |
| 10-17 13:32 | +10 stop | HYPE | DOWN | 0.60 | 0.44 | -1.99 |
| 10-17 13:32 | +20 | HYPE | DOWN | 0.60 | 0.86 | 2.30 |
| 10-17 13:32 | +15 | HYPE | DOWN | 0.61 | 0.86 | 2.24 |
| 10-17 13:32 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.74 |
| 10-17 13:32 | +5 | HYPE | DOWN | 0.60 | 0.71 | 0.74 |
| 10-17 13:31 | +10 stop | ZEC | UP | 0.60 | 0.72 | 0.90 |
| 10-17 13:31 | +20 | ZEC | UP | 0.60 | open |  |
