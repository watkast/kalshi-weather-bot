# Range-Scalp Bot

*Updated Sun Oct 25 12:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33149 | 28929 | 4220 (42) | 1 | $-9258.30 | -4.4% |
| **+10¢** | 24810 | 19924 | 4886 (60) | 4 | $-8225.90 | -5.3% |
| **+15¢** | 20764 | 15503 | 5261 (83) | 6 | $-7401.58 | -5.7% |
| **+20¢** | 18397 | 12888 | 5509 (105) | 7 | $-6516.63 | -5.6% |
| **+10¢ (15¢ stop)** | 40659 | 40599 | 60 (32) | 3 | $-15504.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 12:47 | +10 stop | HYPE | UP | 0.63 | open |  |
| 10-25 12:47 | +5 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-25 12:47 | +5 | XRP | UP | 0.64 | 0.80 | 1.31 |
| 10-25 12:46 | +10 stop | HYPE | DOWN | 0.62 | 0.38 | -2.78 |
| 10-25 12:46 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-25 12:46 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-25 12:46 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-25 12:46 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-25 12:46 | +10 stop | ZEC | UP | 0.63 | 0.77 | 1.11 |
| 10-25 12:46 | +20 | ZEC | UP | 0.62 | open |  |
| 10-25 12:46 | +15 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-25 12:46 | +10 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-25 12:46 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 10-25 12:46 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-25 12:46 | +20 | BNB | UP | 0.61 | open |  |
| 10-25 12:46 | +15 | BNB | UP | 0.61 | open |  |
| 10-25 12:46 | +10 | BNB | UP | 0.61 | open |  |
| 10-25 12:46 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 10-25 12:46 | +10 stop | XRP | UP | 0.60 | 0.80 | 1.71 |
| 10-25 12:46 | +10 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 10-25 12:46 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-25 12:46 | +10 stop | DOGE | UP | 0.57 | 0.84 | 2.42 |
| 10-25 12:46 | +20 | DOGE | UP | 0.57 | 0.84 | 2.42 |
| 10-25 12:46 | +15 | DOGE | UP | 0.57 | 0.84 | 2.42 |
| 10-25 12:46 | +10 | DOGE | UP | 0.57 | 0.84 | 2.42 |
| 10-25 12:46 | +5 | DOGE | UP | 0.57 | 0.84 | 2.42 |
| 10-25 12:46 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-25 12:46 | +20 | NEAR | UP | 0.68 | open |  |
| 10-25 12:46 | +15 | NEAR | UP | 0.68 | open |  |
| 10-25 12:46 | +10 | NEAR | UP | 0.68 | open |  |
| 10-25 12:46 | +5 | NEAR | UP | 0.68 | 0.75 | 0.40 |
| 10-25 12:46 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-25 12:46 | +20 | ETH | UP | 0.66 | open |  |
| 10-25 12:46 | +15 | ETH | UP | 0.66 | open |  |
| 10-25 12:46 | +10 | ETH | UP | 0.66 | open |  |
| 10-25 12:46 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-25 12:46 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-25 12:46 | +20 | BTC | UP | 0.60 | open |  |
| 10-25 12:46 | +15 | BTC | UP | 0.60 | open |  |
| 10-25 12:46 | +10 | BTC | UP | 0.60 | 0.71 | 0.78 |
