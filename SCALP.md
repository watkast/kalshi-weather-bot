# Range-Scalp Bot

*Updated Fri Oct 09 05:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8623 | 7456 | 1167 (13) | 1 | $-2847.61 | -5.2% |
| **+10¢** | 6530 | 5157 | 1373 (25) | 1 | $-2761.80 | -6.7% |
| **+15¢** | 5513 | 4069 | 1444 (37) | 1 | $-2227.81 | -6.4% |
| **+20¢** | 4907 | 3409 | 1498 (45) | 1 | $-1826.03 | -5.9% |
| **+10¢ (15¢ stop)** | 10489 | 10459 | 30 (19) | 0 | $-3898.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 05:47 | +10 stop | DOGE | DOWN | 0.67 | 0.83 | 1.39 |
| 10-09 05:47 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.29 |
| 10-09 05:47 | +5 | DOGE | DOWN | 0.68 | 0.83 | 1.29 |
| 10-09 05:47 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-09 05:47 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 05:47 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-09 05:47 | +10 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-09 05:47 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-09 05:46 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 05:46 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-09 05:46 | +15 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-09 05:46 | +10 | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 05:46 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-09 05:46 | +10 stop | ETH | UP | 0.51 | 0.26 | -2.82 |
| 10-09 05:46 | +20 | ETH | UP | 0.51 | open |  |
| 10-09 05:46 | +15 | ETH | UP | 0.51 | open |  |
| 10-09 05:46 | +10 | ETH | UP | 0.51 | open |  |
| 10-09 05:46 | +5 | ETH | UP | 0.51 | open |  |
| 10-09 05:46 | +10 stop | XRP | DOWN | 0.54 | 0.72 | 1.47 |
| 10-09 05:46 | +20 | XRP | DOWN | 0.54 | 0.74 | 1.68 |
| 10-09 05:46 | +15 | XRP | DOWN | 0.54 | 0.72 | 1.47 |
| 10-09 05:46 | +10 | XRP | DOWN | 0.54 | 0.72 | 1.47 |
| 10-09 05:46 | +5 | XRP | DOWN | 0.54 | 0.72 | 1.47 |
| 10-09 05:46 | +10 stop | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-09 05:46 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-09 05:46 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-09 05:46 | +10 | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-09 05:46 | +5 | ZEC | DOWN | 0.63 | 0.72 | 0.60 |
| 10-09 05:46 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-09 05:46 | +20 | DOGE | DOWN | 0.55 | 0.83 | 2.52 |
| 10-09 05:46 | +15 | DOGE | DOWN | 0.55 | 0.83 | 2.52 |
| 10-09 05:46 | +10 | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-09 05:46 | +5 | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-09 05:44 | +10 stop | SOL | UP | 0.63 | 0.98 | 3.27 |
| 10-09 05:44 | +20 | SOL | UP | 0.63 | 0.98 | 3.27 |
| 10-09 05:43 | +10 stop | DOGE | DOWN | 0.47 | 0.18 | -3.19 |
| 10-09 05:43 | +10 stop | SOL | DOWN | 0.68 | 0.36 | -3.53 |
| 10-09 05:43 | +15 | SOL | DOWN | 0.68 | yes | -6.96 |
| 10-09 05:43 | +10 | SOL | DOWN | 0.68 | yes | -6.96 |
| 10-09 05:43 | +5 | SOL | DOWN | 0.68 | yes | -6.96 |
