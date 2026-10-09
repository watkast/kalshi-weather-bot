# Range-Scalp Bot

*Updated Fri Oct 09 12:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9049 | 7820 | 1229 (14) | 8 | $-3012.81 | -5.3% |
| **+10¢** | 6852 | 5413 | 1439 (26) | 8 | $-2877.02 | -6.7% |
| **+15¢** | 5778 | 4261 | 1517 (38) | 8 | $-2358.95 | -6.5% |
| **+20¢** | 5143 | 3569 | 1574 (46) | 8 | $-1953.04 | -6.1% |
| **+10¢ (15¢ stop)** | 11064 | 11034 | 30 (19) | 0 | $-4184.25 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 12:21 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-09 12:20 | +10 stop | HYPE | UP | 0.56 | 0.35 | -2.44 |
| 10-09 12:19 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-09 12:18 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.44 |
| 10-09 12:17 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-09 12:17 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-09 12:17 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-09 12:17 | +10 stop | XRP | DOWN | 0.59 | 0.70 | 0.78 |
| 10-09 12:17 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-09 12:17 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-09 12:17 | +10 stop | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 10-09 12:16 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.13 |
| 10-09 12:16 | +20 | NEAR | DOWN | 0.59 | 0.82 | 2.06 |
| 10-09 12:16 | +15 | NEAR | DOWN | 0.58 | 0.73 | 1.20 |
| 10-09 12:16 | +10 | NEAR | DOWN | 0.58 | 0.73 | 1.20 |
| 10-09 12:16 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.25 |
| 10-09 12:16 | +5 | BNB | UP | 0.62 | open |  |
| 10-09 12:16 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 10-09 12:16 | +20 | DOGE | UP | 0.57 | open |  |
| 10-09 12:16 | +15 | DOGE | UP | 0.57 | open |  |
| 10-09 12:16 | +10 | DOGE | UP | 0.57 | open |  |
| 10-09 12:16 | +5 | DOGE | UP | 0.57 | open |  |
| 10-09 12:15 | +10 stop | BTC | UP | 0.61 | 0.37 | -2.74 |
| 10-09 12:15 | +20 | BTC | UP | 0.61 | open |  |
| 10-09 12:15 | +15 | BTC | UP | 0.61 | open |  |
| 10-09 12:15 | +10 | BTC | UP | 0.61 | open |  |
| 10-09 12:15 | +5 | BTC | UP | 0.61 | open |  |
| 10-09 12:15 | +10 stop | XRP | UP | 0.58 | 0.34 | -2.74 |
| 10-09 12:15 | +20 | XRP | UP | 0.58 | open |  |
| 10-09 12:15 | +15 | XRP | UP | 0.58 | open |  |
| 10-09 12:15 | +10 | XRP | UP | 0.57 | open |  |
| 10-09 12:15 | +5 | XRP | UP | 0.58 | open |  |
| 10-09 12:15 | +10 stop | ZEC | UP | 0.61 | 0.46 | -1.88 |
| 10-09 12:15 | +20 | ZEC | UP | 0.61 | open |  |
| 10-09 12:15 | +15 | ZEC | UP | 0.61 | open |  |
| 10-09 12:15 | +10 | ZEC | UP | 0.61 | open |  |
| 10-09 12:15 | +5 | ZEC | UP | 0.61 | open |  |
| 10-09 12:15 | +10 stop | ETH | UP | 0.63 | 0.41 | -2.52 |
| 10-09 12:15 | +20 | ETH | UP | 0.63 | open |  |
| 10-09 12:15 | +15 | ETH | UP | 0.63 | open |  |
