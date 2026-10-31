# Range-Scalp Bot

*Updated Sat Oct 31 11:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42177 | 36797 | 5380 (55) | 1 | $-11850.07 | -4.5% |
| **+10¢** | 31448 | 25221 | 6227 (79) | 1 | $-10590.74 | -5.4% |
| **+15¢** | 26298 | 19583 | 6715 (107) | 2 | $-9687.89 | -5.9% |
| **+20¢** | 23354 | 16322 | 7032 (138) | 4 | $-8522.54 | -5.8% |
| **+10¢ (15¢ stop)** | 51445 | 51370 | 75 (41) | 0 | $-19418.84 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 11:24 | +10 stop | NEAR | UP | 0.50 | 0.63 | 0.95 |
| 10-31 11:23 | +10 stop | NEAR | DOWN | 0.58 | 0.34 | -2.74 |
| 10-31 11:21 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-31 11:20 | +5 | SOL | UP | 0.58 | 0.73 | 1.18 |
| 10-31 11:20 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 10-31 11:19 | +10 stop | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-31 11:19 | +10 stop | ZEC | DOWN | 0.66 | 0.35 | -3.42 |
| 10-31 11:19 | +10 stop | SOL | UP | 0.59 | 0.73 | 1.09 |
| 10-31 11:19 | +20 | SOL | UP | 0.59 | 0.79 | 1.71 |
| 10-31 11:19 | +15 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-31 11:19 | +10 | SOL | UP | 0.59 | 0.73 | 1.09 |
| 10-31 11:19 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 10-31 11:19 | +10 stop | XRP | UP | 0.64 | 0.81 | 1.42 |
| 10-31 11:19 | +20 | XRP | UP | 0.64 | 0.84 | 1.73 |
| 10-31 11:19 | +15 | XRP | UP | 0.64 | 0.81 | 1.42 |
| 10-31 11:19 | +10 | XRP | UP | 0.64 | 0.81 | 1.42 |
| 10-31 11:19 | +5 | XRP | UP | 0.64 | 0.81 | 1.42 |
| 10-31 11:19 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +20 | ETH | UP | 0.70 | open |  |
| 10-31 11:19 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
| 10-31 11:19 | +10 | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +5 | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +5 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-31 11:19 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 10-31 11:19 | +20 | HYPE | UP | 0.63 | open |  |
| 10-31 11:19 | +15 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 10-31 11:19 | +10 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 10-31 11:19 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-31 11:18 | +10 stop | NEAR | UP | 0.69 | 0.43 | -2.93 |
| 10-31 11:18 | +20 | NEAR | UP | 0.69 | open |  |
| 10-31 11:18 | +15 | NEAR | UP | 0.69 | open |  |
| 10-31 11:18 | +10 | NEAR | UP | 0.69 | open |  |
| 10-31 11:18 | +5 | NEAR | UP | 0.69 | open |  |
| 10-31 11:16 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 10-31 11:16 | +20 | ZEC | UP | 0.71 | open |  |
| 10-31 11:16 | +15 | ZEC | UP | 0.69 | open |  |
| 10-31 11:16 | +10 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 10-31 11:16 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
