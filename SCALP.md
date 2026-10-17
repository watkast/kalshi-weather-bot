# Range-Scalp Bot

*Updated Sat Oct 17 01:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20177 | 17546 | 2631 (29) | 2 | $-5993.22 | -4.7% |
| **+10¢** | 15198 | 12160 | 3038 (41) | 2 | $-5369.70 | -5.6% |
| **+15¢** | 12708 | 9439 | 3269 (60) | 3 | $-4869.65 | -6.1% |
| **+20¢** | 11267 | 7842 | 3425 (79) | 4 | $-4333.69 | -6.1% |
| **+10¢ (15¢ stop)** | 24810 | 24760 | 50 (29) | 0 | $-9419.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 01:27 | +10 stop | ZEC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-17 01:26 | +10 stop | BTC | UP | 0.64 | 0.43 | -2.45 |
| 10-17 01:25 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-17 01:25 | +20 | ETH | DOWN | 0.54 | 0.79 | 2.19 |
| 10-17 01:25 | +15 | ETH | DOWN | 0.55 | 0.79 | 2.10 |
| 10-17 01:25 | +10 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-17 01:25 | +5 | ETH | DOWN | 0.56 | 0.65 | 0.58 |
| 10-17 01:24 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-17 01:24 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 01:24 | +10 stop | BTC | DOWN | 0.58 | 0.40 | -2.15 |
| 10-17 01:24 | +15 | BTC | DOWN | 0.57 | 0.87 | 2.74 |
| 10-17 01:24 | +10 | BTC | DOWN | 0.57 | 0.87 | 2.74 |
| 10-17 01:24 | +5 | BTC | DOWN | 0.57 | 0.87 | 2.74 |
| 10-17 01:23 | +10 stop | BNB | UP | 0.59 | 0.84 | 2.23 |
| 10-17 01:23 | +10 | BNB | UP | 0.59 | 0.84 | 2.23 |
| 10-17 01:23 | +5 | BNB | UP | 0.59 | 0.84 | 2.23 |
| 10-17 01:23 | +5 | SOL | UP | 0.49 | 0.64 | 1.15 |
| 10-17 01:23 | +10 stop | ZEC | DOWN | 0.70 | 0.46 | -2.73 |
| 10-17 01:23 | +10 | ZEC | DOWN | 0.70 | 0.89 | 1.68 |
| 10-17 01:23 | +5 | ZEC | DOWN | 0.69 | 0.89 | 1.82 |
| 10-17 01:23 | +10 stop | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 10-17 01:23 | +10 stop | HYPE | DOWN | 0.69 | 0.32 | -4.01 |
| 10-17 01:23 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-17 01:23 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 01:23 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 01:23 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-17 01:22 | +10 stop | XRP | DOWN | 0.69 | 0.53 | -1.93 |
| 10-17 01:21 | +10 stop | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 10-17 01:21 | +15 | ZEC | DOWN | 0.57 | 0.89 | 2.95 |
| 10-17 01:21 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-17 01:21 | +5 | ZEC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-17 01:20 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
| 10-17 01:20 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-17 01:20 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-17 01:20 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-17 01:20 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-17 01:20 | +10 stop | DOGE | DOWN | 0.60 | 0.41 | -2.24 |
| 10-17 01:20 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-17 01:20 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-17 01:19 | +10 stop | BNB | DOWN | 0.52 | 0.66 | 1.06 |
