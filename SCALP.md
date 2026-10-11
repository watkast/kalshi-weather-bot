# Range-Scalp Bot

*Updated Sun Oct 11 13:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11961 | 10321 | 1640 (24) | 3 | $-3985.14 | -5.3% |
| **+10¢** | 9075 | 7168 | 1907 (37) | 3 | $-3790.04 | -6.6% |
| **+15¢** | 7645 | 5621 | 2024 (54) | 4 | $-3234.58 | -6.7% |
| **+20¢** | 6810 | 4705 | 2105 (67) | 7 | $-2719.74 | -6.4% |
| **+10¢ (15¢ stop)** | 14718 | 14677 | 41 (25) | 3 | $-5812.73 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 13:03 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-11 13:03 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-11 13:03 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-11 13:03 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-11 13:03 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-11 13:03 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-11 13:02 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.93 |
| 10-11 13:02 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 13:02 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-11 13:02 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-11 13:02 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 13:02 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-11 13:01 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +5 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 0.99 |
| 10-11 13:01 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-11 13:01 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.41 |
| 10-11 13:01 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.92 |
| 10-11 13:01 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.30 |
| 10-11 13:01 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 13:01 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-11 13:01 | +15 | BNB | DOWN | 0.64 | 0.82 | 1.52 |
| 10-11 13:01 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 13:01 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 13:01 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-11 13:01 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-11 13:01 | +20 | ZEC | DOWN | 0.59 | open |  |
| 10-11 13:01 | +15 | ZEC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-11 13:01 | +10 | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-11 13:01 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-11 13:01 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-11 13:01 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-11 13:01 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-11 13:01 | +10 | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-11 13:01 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-11 13:01 | +10 stop | NEAR | DOWN | 0.65 | 0.45 | -2.34 |
| 10-11 13:01 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-11 13:01 | +15 | NEAR | DOWN | 0.65 | open |  |
