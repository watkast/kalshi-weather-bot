# Range-Scalp Bot

*Updated Fri Oct 30 08:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40463 | 35328 | 5135 (51) | 7 | $-11221.64 | -4.4% |
| **+10¢** | 30149 | 24208 | 5941 (74) | 7 | $-9982.83 | -5.3% |
| **+15¢** | 25208 | 18813 | 6395 (101) | 8 | $-9004.52 | -5.7% |
| **+20¢** | 22374 | 15672 | 6702 (130) | 8 | $-7911.10 | -5.6% |
| **+10¢ (15¢ stop)** | 49356 | 49286 | 70 (37) | 5 | $-18671.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 08:21 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 10-30 08:20 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-30 08:20 | +10 stop | HYPE | UP | 0.63 | open |  |
| 10-30 08:20 | +10 | HYPE | UP | 0.63 | open |  |
| 10-30 08:20 | +5 | HYPE | UP | 0.63 | open |  |
| 10-30 08:20 | +5 | XRP | UP | 0.68 | open |  |
| 10-30 08:20 | +5 | NEAR | UP | 0.62 | open |  |
| 10-30 08:20 | +5 | BNB | UP | 0.66 | open |  |
| 10-30 08:19 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 10-30 08:19 | +10 stop | DOGE | UP | 0.55 | 0.39 | -1.95 |
| 10-30 08:19 | +10 stop | ETH | UP | 0.57 | 0.41 | -1.95 |
| 10-30 08:19 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-30 08:18 | +10 stop | BTC | DOWN | 0.56 | 0.39 | -2.05 |
| 10-30 08:18 | +10 stop | DOGE | DOWN | 0.54 | 0.39 | -1.85 |
| 10-30 08:18 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 10-30 08:18 | +10 stop | SOL | UP | 0.63 | 0.77 | 1.10 |
| 10-30 08:18 | +20 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-30 08:18 | +15 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-30 08:18 | +10 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-30 08:18 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-30 08:17 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-30 08:17 | +20 | HYPE | UP | 0.67 | open |  |
| 10-30 08:17 | +15 | HYPE | UP | 0.67 | open |  |
| 10-30 08:17 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-30 08:17 | +5 | HYPE | UP | 0.67 | 0.76 | 0.61 |
| 10-30 08:17 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 10-30 08:17 | +20 | BTC | UP | 0.69 | open |  |
| 10-30 08:17 | +15 | BTC | UP | 0.70 | open |  |
| 10-30 08:17 | +10 | BTC | UP | 0.71 | open |  |
| 10-30 08:17 | +5 | BTC | UP | 0.71 | open |  |
| 10-30 08:16 | +10 stop | BNB | UP | 0.71 | 0.52 | -2.20 |
| 10-30 08:16 | +20 | BNB | UP | 0.71 | open |  |
| 10-30 08:16 | +15 | BNB | UP | 0.71 | open |  |
| 10-30 08:16 | +10 | BNB | UP | 0.71 | open |  |
| 10-30 08:16 | +5 | BNB | UP | 0.71 | 0.77 | 0.35 |
| 10-30 08:16 | +10 stop | ZEC | UP | 0.70 | 0.53 | -2.03 |
| 10-30 08:16 | +20 | ZEC | UP | 0.70 | open |  |
| 10-30 08:16 | +15 | ZEC | UP | 0.70 | open |  |
| 10-30 08:16 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-30 08:16 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
