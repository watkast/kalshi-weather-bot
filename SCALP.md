# Range-Scalp Bot

*Updated Sat Oct 10 04:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9941 | 8581 | 1360 (18) | 3 | $-3341.33 | -5.3% |
| **+10¢** | 7511 | 5925 | 1586 (30) | 4 | $-3211.03 | -6.8% |
| **+15¢** | 6341 | 4668 | 1673 (43) | 4 | $-2651.00 | -6.7% |
| **+20¢** | 5634 | 3896 | 1738 (55) | 4 | $-2215.02 | -6.3% |
| **+10¢ (15¢ stop)** | 12204 | 12169 | 35 (22) | 3 | $-4773.82 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 04:18 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-10 04:18 | +10 stop | ETH | DOWN | 0.56 | open |  |
| 10-10 04:17 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.17 |
| 10-10 04:17 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +5 | ZEC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-10 04:17 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-10 04:17 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 10-10 04:17 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-10 04:17 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-10 04:17 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-10 04:17 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-10 04:16 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-10 04:16 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-10 04:16 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-10 04:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-10 04:16 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-10 04:12 | +10 stop | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +20 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +15 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +10 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +5 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:01 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-10 04:01 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-10 04:01 | +20 | HYPE | UP | 0.67 | 0.90 | 2.10 |
| 10-10 04:01 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-10 04:01 | +10 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-10 04:01 | +5 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-10 04:01 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-10 04:01 | +20 | BTC | UP | 0.65 | 0.87 | 1.96 |
| 10-10 04:01 | +15 | BTC | UP | 0.64 | 0.79 | 1.21 |
| 10-10 04:01 | +10 | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-10 04:01 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-10 04:01 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-10 04:01 | +20 | DOGE | UP | 0.71 | 0.93 | 1.96 |
