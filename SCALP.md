# Range-Scalp Bot

*Updated Sat Oct 31 11:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42165 | 36787 | 5378 (55) | 2 | $-11845.19 | -4.5% |
| **+10¢** | 31437 | 25213 | 6224 (79) | 3 | $-10581.08 | -5.4% |
| **+15¢** | 26289 | 19577 | 6712 (107) | 3 | $-9677.64 | -5.9% |
| **+20¢** | 23347 | 16318 | 7029 (138) | 3 | $-8511.70 | -5.8% |
| **+10¢ (15¢ stop)** | 51432 | 51357 | 75 (41) | 0 | $-19416.89 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 11:12 | +5 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 11:11 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.23 |
| 10-31 11:10 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 10-31 11:10 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.73 |
| 10-31 11:09 | +10 stop | HYPE | UP | 0.43 | 0.60 | 1.35 |
| 10-31 11:09 | +10 stop | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-31 11:08 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-31 11:08 | +10 stop | ETH | UP | 0.65 | 0.46 | -2.24 |
| 10-31 11:07 | +10 stop | ETH | DOWN | 0.57 | 0.36 | -2.45 |
| 10-31 11:07 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-31 11:07 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-31 11:06 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-31 11:06 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-31 11:06 | +10 stop | SOL | UP | 0.60 | 0.73 | 0.99 |
| 10-31 11:05 | +10 stop | ETH | DOWN | 0.69 | 0.46 | -2.63 |
| 10-31 11:05 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 10-31 11:05 | +10 stop | NEAR | DOWN | 0.66 | 0.44 | -2.54 |
| 10-31 11:05 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 10-31 11:04 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 11:04 | +5 | HYPE | DOWN | 0.56 | 0.65 | 0.56 |
| 10-31 11:04 | +10 stop | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-31 11:04 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-31 11:03 | +5 | HYPE | UP | 0.51 | 0.60 | 0.55 |
| 10-31 11:02 | +10 stop | HYPE | UP | 0.66 | 0.42 | -2.75 |
| 10-31 11:02 | +20 | HYPE | UP | 0.67 | open |  |
| 10-31 11:02 | +15 | HYPE | UP | 0.67 | open |  |
| 10-31 11:02 | +10 | HYPE | UP | 0.66 | open |  |
| 10-31 11:02 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-31 11:02 | +10 stop | DOGE | UP | 0.62 | 0.47 | -1.85 |
| 10-31 11:02 | +20 | DOGE | UP | 0.62 | 0.84 | 1.93 |
| 10-31 11:02 | +15 | DOGE | UP | 0.62 | 0.81 | 1.62 |
| 10-31 11:02 | +10 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-31 11:02 | +5 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-31 11:02 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 10-31 11:02 | +20 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +15 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +10 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +5 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-31 11:02 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
