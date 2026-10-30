# Range-Scalp Bot

*Updated Fri Oct 30 23:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41443 | 36167 | 5276 (54) | 3 | $-11597.56 | -4.4% |
| **+10¢** | 30890 | 24786 | 6104 (78) | 3 | $-10329.68 | -5.3% |
| **+15¢** | 25821 | 19242 | 6579 (106) | 4 | $-9399.67 | -5.8% |
| **+20¢** | 22920 | 16030 | 6890 (137) | 4 | $-8270.61 | -5.7% |
| **+10¢ (15¢ stop)** | 50510 | 50435 | 75 (41) | 1 | $-19090.88 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 23:58 | +5 | DOGE | DOWN | 0.64 | open |  |
| 10-30 23:58 | +10 stop | XRP | UP | 0.58 | 0.80 | 1.90 |
| 10-30 23:57 | +10 stop | DOGE | DOWN | 0.57 | open |  |
| 10-30 23:57 | +10 stop | XRP | DOWN | 0.59 | 0.42 | -2.05 |
| 10-30 23:56 | +10 stop | XRP | UP | 0.46 | 0.56 | 0.64 |
| 10-30 23:56 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-30 23:56 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.68 |
| 10-30 23:56 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.58 |
| 10-30 23:56 | +10 stop | BTC | DOWN | 0.55 | 0.88 | 3.04 |
| 10-30 23:56 | +15 | BTC | DOWN | 0.55 | 0.88 | 3.04 |
| 10-30 23:56 | +10 | BTC | DOWN | 0.55 | 0.88 | 3.04 |
| 10-30 23:56 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-30 23:54 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.36 |
| 10-30 23:54 | +10 stop | XRP | UP | 0.64 | 0.42 | -2.55 |
| 10-30 23:54 | +15 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 23:54 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 10-30 23:54 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.44 |
| 10-30 23:53 | +10 stop | HYPE | UP | 0.68 | 0.82 | 1.09 |
| 10-30 23:52 | +10 stop | XRP | UP | 0.64 | 0.49 | -1.85 |
| 10-30 23:52 | +5 | ZEC | DOWN | 0.50 | 0.62 | 0.85 |
| 10-30 23:51 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-30 23:51 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-30 23:51 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 10-30 23:50 | +10 stop | HYPE | UP | 0.58 | 0.42 | -1.96 |
| 10-30 23:50 | +5 | ZEC | DOWN | 0.57 | 0.64 | 0.35 |
| 10-30 23:50 | +10 stop | XRP | UP | 0.49 | 0.62 | 0.95 |
| 10-30 23:49 | +5 | ZEC | DOWN | 0.53 | 0.60 | 0.35 |
| 10-30 23:49 | +5 | NEAR | DOWN | 0.56 | 0.64 | 0.45 |
| 10-30 23:48 | +10 stop | ZEC | DOWN | 0.58 | 0.37 | -2.45 |
| 10-30 23:48 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-30 23:48 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-30 23:47 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-30 23:47 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-30 23:47 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-30 23:46 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-30 23:46 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-30 23:46 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-30 23:46 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 23:46 | +5 | DOGE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-30 23:46 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
