# Range-Scalp Bot

*Updated Fri Oct 23 00:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29535 | 25709 | 3826 (39) | 0 | $-8708.24 | -4.7% |
| **+10¢** | 22144 | 17714 | 4430 (55) | 0 | $-7848.52 | -5.6% |
| **+15¢** | 18540 | 13784 | 4756 (78) | 2 | $-7022.79 | -6.0% |
| **+20¢** | 16404 | 11419 | 4985 (100) | 5 | $-6367.34 | -6.2% |
| **+10¢ (15¢ stop)** | 36263 | 36204 | 59 (32) | 0 | $-13702.63 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 00:31 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-23 00:31 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-23 00:31 | +20 | BNB | UP | 0.70 | open |  |
| 10-23 00:31 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-23 00:31 | +10 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-23 00:31 | +5 | BNB | UP | 0.70 | 0.79 | 0.63 |
| 10-23 00:31 | +10 stop | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-23 00:31 | +20 | XRP | UP | 0.62 | open |  |
| 10-23 00:31 | +15 | XRP | UP | 0.62 | 0.77 | 1.20 |
| 10-23 00:31 | +10 | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-23 00:31 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 10-23 00:31 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +20 | SOL | UP | 0.69 | open |  |
| 10-23 00:31 | +15 | SOL | UP | 0.69 | open |  |
| 10-23 00:31 | +10 | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 10-23 00:31 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +20 | ETH | UP | 0.69 | 0.89 | 1.78 |
| 10-23 00:31 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-23 00:31 | +10 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +5 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-23 00:31 | +20 | DOGE | UP | 0.71 | open |  |
| 10-23 00:31 | +15 | DOGE | UP | 0.71 | open |  |
| 10-23 00:31 | +5 | DOGE | UP | 0.71 | 0.80 | 0.63 |
| 10-23 00:31 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-23 00:31 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 10-23 00:31 | +15 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 10-23 00:31 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-23 00:31 | +5 | BTC | UP | 0.67 | 0.74 | 0.40 |
| 10-23 00:31 | +10 stop | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:31 | +20 | HYPE | UP | 0.69 | open |  |
| 10-23 00:31 | +15 | HYPE | UP | 0.69 | 0.84 | 1.25 |
| 10-23 00:31 | +10 | HYPE | UP | 0.71 | 0.84 | 1.07 |
| 10-23 00:31 | +5 | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-23 00:26 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-23 00:26 | +10 stop | DOGE | DOWN | 0.60 | 0.24 | -3.90 |
| 10-23 00:26 | +10 stop | BNB | DOWN | 0.68 | 0.25 | -4.60 |
| 10-23 00:26 | +5 | HYPE | UP | 0.65 | 0.83 | 1.50 |
| 10-23 00:25 | +10 stop | DOGE | UP | 0.57 | 0.40 | -2.05 |
