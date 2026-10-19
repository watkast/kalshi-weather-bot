# Range-Scalp Bot

*Updated Mon Oct 19 18:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24391 | 21221 | 3170 (31) | 1 | $-7200.11 | -4.7% |
| **+10¢** | 18337 | 14676 | 3661 (46) | 1 | $-6434.37 | -5.6% |
| **+15¢** | 15357 | 11417 | 3940 (69) | 1 | $-5796.86 | -6.0% |
| **+20¢** | 13591 | 9466 | 4125 (87) | 1 | $-5198.31 | -6.1% |
| **+10¢ (15¢ stop)** | 29994 | 29942 | 52 (30) | 1 | $-11369.92 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 18:34 | +5 | ZEC | UP | 0.68 | open |  |
| 10-19 18:31 | +10 stop | ZEC | UP | 0.69 | open |  |
| 10-19 18:31 | +20 | ZEC | UP | 0.70 | open |  |
| 10-19 18:31 | +15 | ZEC | UP | 0.70 | open |  |
| 10-19 18:31 | +10 | ZEC | UP | 0.70 | open |  |
| 10-19 18:31 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 10-19 18:30 | +10 stop | NEAR | UP | 0.65 | 0.79 | 1.15 |
| 10-19 18:30 | +20 | NEAR | UP | 0.65 | 0.87 | 1.99 |
| 10-19 18:30 | +15 | NEAR | UP | 0.65 | 0.83 | 1.57 |
| 10-19 18:30 | +10 | NEAR | UP | 0.65 | 0.79 | 1.15 |
| 10-19 18:30 | +5 | NEAR | UP | 0.65 | 0.73 | 0.53 |
| 10-19 18:30 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-19 18:30 | +20 | HYPE | UP | 0.64 | 0.86 | 1.94 |
| 10-19 18:30 | +15 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-19 18:30 | +10 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-19 18:30 | +5 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-19 18:30 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-19 18:30 | +20 | BNB | UP | 0.64 | 0.87 | 2.05 |
| 10-19 18:30 | +15 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 10-19 18:30 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-19 18:30 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-19 18:19 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-19 18:19 | +10 | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-19 18:19 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 18:19 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:19 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:19 | +5 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:17 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-19 18:16 | +5 | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-19 18:16 | +10 stop | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +15 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +10 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-19 18:16 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +20 | NEAR | DOWN | 0.62 | 0.83 | 1.83 |
| 10-19 18:16 | +15 | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 18:16 | +10 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +5 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +10 stop | BTC | DOWN | 0.59 | 0.72 | 0.98 |
