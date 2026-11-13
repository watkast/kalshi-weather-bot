# Range-Scalp Bot

*Updated Fri Nov 13 12:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58272 | 50850 | 7422 (102) | 5 | $-15702.09 | -4.3% |
| **+10¢** | 43545 | 34866 | 8679 (134) | 5 | $-14667.38 | -5.4% |
| **+15¢** | 36505 | 27160 | 9345 (169) | 5 | $-13215.49 | -5.8% |
| **+20¢** | 32522 | 22709 | 9813 (220) | 5 | $-11605.08 | -5.7% |
| **+10¢ (15¢ stop)** | 71006 | 70877 | 129 (79) | 3 | $-26118.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 12:26 | +5 | BNB | UP | 0.58 | open |  |
| 11-13 12:26 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-13 12:26 | +10 stop | DOGE | DOWN | 0.70 | open |  |
| 11-13 12:26 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-13 12:26 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-13 12:26 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-13 12:26 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-13 12:26 | +10 stop | BNB | UP | 0.58 | open |  |
| 11-13 12:26 | +10 | BNB | UP | 0.58 | open |  |
| 11-13 12:26 | +5 | BNB | UP | 0.58 | 0.64 | 0.25 |
| 11-13 12:25 | +10 stop | BNB | DOWN | 0.38 | 0.62 | 2.06 |
| 11-13 12:25 | +10 | BNB | DOWN | 0.39 | 0.62 | 1.96 |
| 11-13 12:25 | +5 | BNB | DOWN | 0.41 | 0.62 | 1.76 |
| 11-13 12:25 | +10 | BNB | UP | 0.50 | 0.66 | 1.26 |
| 11-13 12:25 | +5 | BNB | UP | 0.51 | 0.66 | 1.16 |
| 11-13 12:24 | +10 | HYPE | DOWN | 0.56 | 0.75 | 1.58 |
| 11-13 12:23 | +10 stop | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 11-13 12:23 | +10 stop | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-13 12:23 | +15 | HYPE | DOWN | 0.62 | 0.84 | 1.93 |
| 11-13 12:23 | +10 | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 11-13 12:23 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-13 12:22 | +10 stop | BNB | UP | 0.64 | 0.30 | -3.70 |
| 11-13 12:21 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.00 |
| 11-13 12:21 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-13 12:21 | +5 | XRP | DOWN | 0.70 | 0.83 | 1.00 |
| 11-13 12:21 | +10 stop | DOGE | DOWN | 0.70 | 0.51 | -2.23 |
| 11-13 12:21 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.87 |
| 11-13 12:21 | +15 | DOGE | DOWN | 0.70 | 0.91 | 1.87 |
| 11-13 12:21 | +10 | DOGE | DOWN | 0.70 | 0.91 | 1.87 |
| 11-13 12:21 | +5 | DOGE | DOWN | 0.70 | 0.91 | 1.87 |
| 11-13 12:21 | +10 stop | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-13 12:21 | +10 stop | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-13 12:21 | +5 | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-13 12:20 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.13 |
| 11-13 12:19 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 12:19 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 12:19 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 12:19 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-13 12:19 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 12:19 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
