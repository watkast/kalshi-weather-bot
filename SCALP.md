# Range-Scalp Bot

*Updated Fri Oct 09 02:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8415 | 7282 | 1133 (13) | 6 | $-2726.60 | -5.1% |
| **+10¢** | 6375 | 5036 | 1339 (25) | 7 | $-2680.26 | -6.7% |
| **+15¢** | 5379 | 3969 | 1410 (37) | 7 | $-2170.78 | -6.4% |
| **+20¢** | 4785 | 3322 | 1463 (45) | 7 | $-1791.90 | -6.0% |
| **+10¢ (15¢ stop)** | 10231 | 10201 | 30 (19) | 1 | $-3757.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 02:49 | +5 | NEAR | UP | 0.62 | open |  |
| 10-09 02:49 | +10 stop | XRP | UP | 0.69 | open |  |
| 10-09 02:48 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 10-09 02:48 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-09 02:47 | +10 stop | HYPE | UP | 0.48 | 0.60 | 0.81 |
| 10-09 02:47 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 10-09 02:47 | +20 | NEAR | UP | 0.57 | open |  |
| 10-09 02:47 | +15 | NEAR | UP | 0.57 | open |  |
| 10-09 02:47 | +10 | NEAR | UP | 0.57 | open |  |
| 10-09 02:47 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-09 02:47 | +5 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-09 02:47 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-09 02:47 | +10 stop | ETH | DOWN | 0.52 | 0.31 | -2.43 |
| 10-09 02:47 | +20 | ETH | DOWN | 0.52 | open |  |
| 10-09 02:47 | +15 | ETH | DOWN | 0.52 | open |  |
| 10-09 02:47 | +10 | ETH | DOWN | 0.52 | open |  |
| 10-09 02:47 | +5 | ETH | DOWN | 0.52 | open |  |
| 10-09 02:47 | +10 stop | DOGE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-09 02:47 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-09 02:47 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-09 02:47 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-09 02:47 | +5 | DOGE | DOWN | 0.56 | open |  |
| 10-09 02:47 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-09 02:47 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-09 02:47 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-09 02:47 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-09 02:47 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-09 02:47 | +10 stop | BTC | DOWN | 0.57 | 0.35 | -2.54 |
| 10-09 02:47 | +20 | BTC | DOWN | 0.57 | open |  |
| 10-09 02:47 | +15 | BTC | DOWN | 0.57 | open |  |
| 10-09 02:47 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-09 02:47 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-09 02:46 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +20 | ZEC | UP | 0.70 | 0.92 | 1.96 |
| 10-09 02:46 | +15 | ZEC | UP | 0.70 | 0.85 | 1.26 |
| 10-09 02:46 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +5 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
| 10-09 02:46 | +20 | BNB | UP | 0.54 | 0.74 | 1.68 |
| 10-09 02:46 | +15 | BNB | UP | 0.54 | 0.74 | 1.68 |
