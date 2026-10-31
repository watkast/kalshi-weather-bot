# Range-Scalp Bot

*Updated Sat Oct 31 11:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42156 | 36778 | 5378 (55) | 8 | $-11849.72 | -4.5% |
| **+10¢** | 31432 | 25208 | 6224 (79) | 8 | $-10586.21 | -5.4% |
| **+15¢** | 26284 | 19572 | 6712 (107) | 8 | $-9686.93 | -5.9% |
| **+20¢** | 23342 | 16313 | 7029 (138) | 8 | $-8522.05 | -5.8% |
| **+10¢ (15¢ stop)** | 51413 | 51338 | 75 (41) | 4 | $-19402.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 11:04 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 10-31 11:04 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-31 11:04 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-31 11:04 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-31 11:03 | +5 | HYPE | UP | 0.51 | 0.60 | 0.55 |
| 10-31 11:02 | +10 stop | HYPE | UP | 0.66 | 0.42 | -2.75 |
| 10-31 11:02 | +20 | HYPE | UP | 0.67 | open |  |
| 10-31 11:02 | +15 | HYPE | UP | 0.67 | open |  |
| 10-31 11:02 | +10 | HYPE | UP | 0.66 | open |  |
| 10-31 11:02 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-31 11:02 | +10 stop | DOGE | UP | 0.62 | 0.47 | -1.85 |
| 10-31 11:02 | +20 | DOGE | UP | 0.62 | open |  |
| 10-31 11:02 | +15 | DOGE | UP | 0.62 | open |  |
| 10-31 11:02 | +10 | DOGE | UP | 0.62 | open |  |
| 10-31 11:02 | +5 | DOGE | UP | 0.62 | open |  |
| 10-31 11:02 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 10-31 11:02 | +20 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +15 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +10 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +5 | XRP | UP | 0.59 | open |  |
| 10-31 11:02 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-31 11:02 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-31 11:02 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-31 11:02 | +10 stop | BTC | UP | 0.63 | open |  |
| 10-31 11:02 | +20 | BTC | UP | 0.63 | open |  |
| 10-31 11:02 | +15 | BTC | UP | 0.63 | open |  |
| 10-31 11:02 | +10 | BTC | UP | 0.64 | open |  |
| 10-31 11:02 | +5 | BTC | UP | 0.66 | open |  |
| 10-31 11:02 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 10-31 11:02 | +20 | ZEC | UP | 0.67 | open |  |
| 10-31 11:02 | +15 | ZEC | UP | 0.67 | open |  |
| 10-31 11:02 | +10 | ZEC | UP | 0.67 | open |  |
| 10-31 11:02 | +5 | ZEC | UP | 0.67 | open |  |
| 10-31 11:02 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 10-31 11:02 | +20 | NEAR | UP | 0.62 | open |  |
| 10-31 11:02 | +15 | NEAR | UP | 0.63 | open |  |
| 10-31 11:02 | +10 | NEAR | UP | 0.63 | open |  |
| 10-31 11:02 | +5 | NEAR | UP | 0.63 | open |  |
| 10-31 11:01 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-31 11:01 | +20 | ETH | UP | 0.67 | open |  |
