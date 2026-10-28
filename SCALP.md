# Range-Scalp Bot

*Updated Wed Oct 28 04:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37577 | 32786 | 4791 (45) | 7 | $-10598.17 | -4.5% |
| **+10¢** | 28060 | 22518 | 5542 (67) | 9 | $-9443.81 | -5.3% |
| **+15¢** | 23473 | 17523 | 5950 (91) | 9 | $-8406.36 | -5.7% |
| **+20¢** | 20810 | 14581 | 6229 (116) | 9 | $-7391.09 | -5.7% |
| **+10¢ (15¢ stop)** | 46044 | 45979 | 65 (34) | 1 | $-17531.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 04:53 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 10-28 04:52 | +10 stop | HYPE | UP | 0.68 | open |  |
| 10-28 04:52 | +20 | HYPE | UP | 0.68 | open |  |
| 10-28 04:52 | +15 | HYPE | UP | 0.68 | open |  |
| 10-28 04:52 | +10 | HYPE | UP | 0.67 | open |  |
| 10-28 04:52 | +5 | HYPE | UP | 0.67 | 0.74 | 0.36 |
| 10-28 04:51 | +10 stop | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 04:50 | +10 stop | SOL | UP | 0.54 | 0.30 | -2.73 |
| 10-28 04:50 | +10 stop | ZEC | UP | 0.64 | 0.48 | -1.95 |
| 10-28 04:50 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-28 04:49 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-28 04:48 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-28 04:48 | +10 stop | DOGE | DOWN | 0.67 | 0.47 | -2.34 |
| 10-28 04:48 | +10 stop | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 10-28 04:48 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
| 10-28 04:48 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-28 04:47 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-28 04:47 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 10-28 04:47 | +20 | ETH | UP | 0.62 | open |  |
| 10-28 04:47 | +15 | ETH | UP | 0.62 | open |  |
| 10-28 04:47 | +10 | ETH | UP | 0.62 | open |  |
| 10-28 04:47 | +5 | ETH | UP | 0.62 | open |  |
| 10-28 04:47 | +5 | ZEC | UP | 0.68 | open |  |
| 10-28 04:46 | +10 stop | DOGE | UP | 0.59 | 0.37 | -2.54 |
| 10-28 04:46 | +20 | DOGE | UP | 0.59 | open |  |
| 10-28 04:46 | +15 | DOGE | UP | 0.59 | open |  |
| 10-28 04:46 | +10 | DOGE | UP | 0.59 | open |  |
| 10-28 04:46 | +5 | DOGE | UP | 0.59 | open |  |
| 10-28 04:46 | +10 stop | XRP | UP | 0.51 | 0.36 | -1.85 |
| 10-28 04:46 | +20 | XRP | UP | 0.51 | open |  |
| 10-28 04:46 | +15 | XRP | UP | 0.51 | open |  |
| 10-28 04:46 | +10 | XRP | UP | 0.51 | open |  |
| 10-28 04:46 | +5 | XRP | UP | 0.51 | 0.57 | 0.24 |
| 10-28 04:46 | +10 stop | SOL | UP | 0.69 | 0.45 | -2.73 |
| 10-28 04:46 | +20 | SOL | UP | 0.69 | open |  |
| 10-28 04:46 | +15 | SOL | UP | 0.69 | open |  |
| 10-28 04:46 | +10 | SOL | UP | 0.69 | open |  |
| 10-28 04:46 | +5 | SOL | UP | 0.69 | open |  |
| 10-28 04:46 | +10 stop | NEAR | UP | 0.55 | 0.33 | -2.54 |
| 10-28 04:46 | +20 | NEAR | UP | 0.55 | open |  |
