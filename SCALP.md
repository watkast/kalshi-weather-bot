# Range-Scalp Bot

*Updated Sun Nov 01 23:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44088 | 38403 | 5685 (65) | 5 | $-12677.50 | -4.6% |
| **+10¢** | 32900 | 26332 | 6568 (86) | 7 | $-11414.62 | -5.5% |
| **+15¢** | 27535 | 20467 | 7068 (113) | 8 | $-10412.82 | -6.0% |
| **+20¢** | 24461 | 17060 | 7401 (147) | 7 | $-9159.95 | -6.0% |
| **+10¢ (15¢ stop)** | 53775 | 53689 | 86 (51) | 3 | $-20335.19 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 23:54 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 11-01 23:54 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-01 23:54 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-01 23:54 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-01 23:53 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-01 23:52 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 23:51 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 11-01 23:51 | +10 stop | HYPE | UP | 0.69 | 0.89 | 1.74 |
| 11-01 23:51 | +5 | HYPE | UP | 0.69 | 0.75 | 0.27 |
| 11-01 23:51 | +10 stop | DOGE | UP | 0.71 | 0.42 | -3.23 |
| 11-01 23:51 | +10 stop | XRP | UP | 0.60 | 0.44 | -1.95 |
| 11-01 23:51 | +10 stop | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-01 23:51 | +5 | NEAR | UP | 0.66 | 0.75 | 0.60 |
| 11-01 23:50 | +5 | HYPE | DOWN | 0.48 | 0.61 | 0.91 |
| 11-01 23:50 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-01 23:50 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-01 23:50 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 11-01 23:50 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-01 23:50 | +5 | ETH | DOWN | 0.64 | open |  |
| 11-01 23:49 | +10 stop | BTC | DOWN | 0.71 | 0.45 | -2.93 |
| 11-01 23:49 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-01 23:48 | +10 stop | ETH | DOWN | 0.64 | 0.48 | -1.95 |
| 11-01 23:48 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-01 23:48 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 11-01 23:48 | +10 stop | ZEC | DOWN | 0.68 | 0.47 | -2.44 |
| 11-01 23:47 | +10 | ZEC | DOWN | 0.67 | open |  |
| 11-01 23:47 | +10 stop | SOL | DOWN | 0.58 | 0.41 | -2.05 |
| 11-01 23:47 | +20 | SOL | DOWN | 0.58 | open |  |
| 11-01 23:47 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-01 23:47 | +10 | SOL | DOWN | 0.58 | open |  |
| 11-01 23:47 | +5 | SOL | DOWN | 0.58 | open |  |
| 11-01 23:47 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-01 23:47 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-01 23:47 | +5 | BTC | DOWN | 0.70 | open |  |
| 11-01 23:47 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 11-01 23:47 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-01 23:47 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-01 23:47 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-01 23:47 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-01 23:47 | +10 stop | XRP | DOWN | 0.61 | 0.30 | -3.42 |
