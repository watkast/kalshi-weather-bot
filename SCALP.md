# Range-Scalp Bot

*Updated Sat Oct 10 11:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10321 | 8897 | 1424 (22) | 4 | $-3528.80 | -5.4% |
| **+10¢** | 7806 | 6147 | 1659 (35) | 5 | $-3382.00 | -6.9% |
| **+15¢** | 6585 | 4826 | 1759 (51) | 5 | $-2861.75 | -6.9% |
| **+20¢** | 5854 | 4023 | 1831 (65) | 5 | $-2431.73 | -6.6% |
| **+10¢ (15¢ stop)** | 12671 | 12633 | 38 (25) | 3 | $-4960.59 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 11:01 | +5 | DOGE | DOWN | 0.40 | 0.57 | 1.35 |
| 10-10 11:01 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 10-10 11:01 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-10 11:01 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-10 11:01 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-10 11:01 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-10 11:01 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-10 11:01 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-10 11:01 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-10 11:01 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-10 11:01 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-10 11:01 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-10 11:01 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-10 11:01 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-10 11:01 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-10 11:01 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-10 11:01 | +10 stop | XRP | DOWN | 0.60 | 0.40 | -2.37 |
| 10-10 11:01 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-10 11:01 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-10 11:01 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-10 11:01 | +5 | XRP | DOWN | 0.60 | open |  |
| 10-10 11:01 | +10 stop | DOGE | DOWN | 0.57 | 0.39 | -2.15 |
| 10-10 11:01 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-10 11:01 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-10 11:01 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-10 11:01 | +5 | DOGE | DOWN | 0.57 | 0.65 | 0.46 |
| 10-10 10:55 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-10 10:55 | +20 | DOGE | UP | 0.64 | 0.87 | 2.05 |
| 10-10 10:55 | +15 | DOGE | UP | 0.64 | 0.83 | 1.63 |
| 10-10 10:55 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-10 10:55 | +5 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-10 10:50 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-10 10:50 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-10 10:49 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-10 10:49 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-10 10:49 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-10 10:47 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-10 10:47 | +10 stop | NEAR | UP | 0.65 | 0.49 | -1.94 |
| 10-10 10:47 | +20 | NEAR | UP | 0.65 | no | -6.66 |
| 10-10 10:47 | +15 | NEAR | UP | 0.65 | no | -6.66 |
