# Range-Scalp Bot

*Updated Fri Oct 16 13:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19299 | 16768 | 2531 (29) | 1 | $-5832.97 | -4.8% |
| **+10¢** | 14546 | 11620 | 2926 (41) | 1 | $-5262.66 | -5.8% |
| **+15¢** | 12179 | 9029 | 3150 (60) | 1 | $-4779.59 | -6.3% |
| **+20¢** | 10800 | 7499 | 3301 (79) | 2 | $-4259.80 | -6.3% |
| **+10¢ (15¢ stop)** | 23735 | 23685 | 50 (29) | 0 | $-9140.47 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 13:42 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 10-16 13:41 | +10 stop | NEAR | DOWN | 0.68 | 0.42 | -2.94 |
| 10-16 13:40 | +10 stop | NEAR | UP | 0.48 | 0.59 | 0.75 |
| 10-16 13:40 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-16 13:40 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-16 13:40 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-16 13:40 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-16 13:40 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-16 13:39 | +10 stop | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-16 13:39 | +20 | ETH | DOWN | 0.57 | 0.78 | 1.79 |
| 10-16 13:39 | +15 | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-16 13:39 | +10 | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-16 13:39 | +5 | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 10-16 13:39 | +10 stop | DOGE | DOWN | 0.56 | 0.77 | 1.84 |
| 10-16 13:39 | +15 | DOGE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-16 13:39 | +10 | DOGE | DOWN | 0.55 | 0.77 | 1.89 |
| 10-16 13:39 | +5 | DOGE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-16 13:39 | +10 stop | XRP | DOWN | 0.49 | 0.62 | 0.95 |
| 10-16 13:39 | +10 | XRP | DOWN | 0.49 | 0.62 | 0.95 |
| 10-16 13:39 | +5 | XRP | DOWN | 0.49 | 0.54 | 0.14 |
| 10-16 13:38 | +10 stop | NEAR | DOWN | 0.68 | 0.49 | -2.28 |
| 10-16 13:38 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-16 13:38 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-16 13:37 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.81 |
| 10-16 13:37 | +15 | NEAR | DOWN | 0.60 | open |  |
| 10-16 13:37 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-16 13:37 | +5 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-16 13:35 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 13:34 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-16 13:33 | +10 stop | HYPE | UP | 0.70 | 0.44 | -2.93 |
| 10-16 13:33 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-16 13:33 | +15 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-16 13:33 | +10 | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 10-16 13:33 | +5 | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-16 13:33 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-16 13:33 | +5 | ZEC | UP | 0.58 | 0.70 | 0.87 |
| 10-16 13:33 | +10 stop | HYPE | UP | 0.53 | 0.64 | 0.71 |
| 10-16 13:32 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 13:32 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.73 |
| 10-16 13:32 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.78 |
