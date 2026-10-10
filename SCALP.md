# Range-Scalp Bot

*Updated Sat Oct 10 09:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10215 | 8803 | 1412 (22) | 4 | $-3507.64 | -5.4% |
| **+10¢** | 7722 | 6080 | 1642 (34) | 4 | $-3354.57 | -6.9% |
| **+15¢** | 6521 | 4783 | 1738 (49) | 5 | $-2817.73 | -6.9% |
| **+20¢** | 5794 | 3987 | 1807 (63) | 5 | $-2376.98 | -6.5% |
| **+10¢ (15¢ stop)** | 12547 | 12510 | 37 (24) | 2 | $-4933.98 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 09:20 | +5 | NEAR | DOWN | 0.55 | open |  |
| 10-10 09:20 | +10 stop | ETH | DOWN | 0.70 | 0.55 | -1.87 |
| 10-10 09:20 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-10 09:20 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-10 09:20 | +10 | ETH | DOWN | 0.69 | open |  |
| 10-10 09:20 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-10 09:19 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-10 09:19 | +20 | BNB | UP | 0.59 | open |  |
| 10-10 09:19 | +15 | BNB | UP | 0.59 | open |  |
| 10-10 09:19 | +10 | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-10 09:19 | +5 | BNB | UP | 0.59 | 0.68 | 0.57 |
| 10-10 09:19 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-10 09:19 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-10 09:19 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-10 09:19 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-10 09:19 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-10 09:19 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 10-10 09:19 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-10 09:19 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-10 09:19 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-10 09:19 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-10 09:18 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-10 09:16 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 10-10 09:16 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-10 09:16 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-10 09:16 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-10 09:16 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 09:16 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-10 09:16 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.79 |
| 10-10 09:16 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-10 09:16 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-10 09:16 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-10 09:16 | +10 stop | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-10 09:16 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-10 09:16 | +15 | XRP | DOWN | 0.66 | 0.84 | 1.54 |
| 10-10 09:16 | +10 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-10 09:16 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-10 09:10 | +10 stop | DOGE | UP | 0.56 | 0.68 | 0.86 |
| 10-10 09:10 | +10 stop | HYPE | UP | 0.60 | 0.78 | 1.50 |
| 10-10 09:10 | +20 | HYPE | UP | 0.60 | 0.83 | 2.03 |
