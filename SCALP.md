# Range-Scalp Bot

*Updated Mon Oct 05 16:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3964 | 3402 | 562 (4) | 4 | $-1450.63 | -5.8% |
| **+10¢** | 3066 | 2419 | 647 (5) | 6 | $-1344.70 | -7.0% |
| **+15¢** | 2577 | 1897 | 680 (8) | 7 | $-1161.53 | -7.2% |
| **+20¢** | 2299 | 1590 | 709 (13) | 7 | $-1005.02 | -7.0% |
| **+10¢ (15¢ stop)** | 4902 | 4897 | 5 (2) | 3 | $-1827.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 16:07 | +10 stop | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 10-05 16:07 | +15 | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 10-05 16:07 | +10 | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 10-05 16:07 | +5 | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 10-05 16:07 | +10 stop | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-05 16:07 | +15 | ZEC | DOWN | 0.46 | open |  |
| 10-05 16:07 | +5 | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-05 16:07 | +10 stop | SOL | UP | 0.70 | open |  |
| 10-05 16:07 | +10 | SOL | UP | 0.70 | open |  |
| 10-05 16:07 | +10 stop | ETH | DOWN | 0.56 | open |  |
| 10-05 16:07 | +20 | ETH | DOWN | 0.56 | open |  |
| 10-05 16:07 | +15 | ETH | DOWN | 0.56 | open |  |
| 10-05 16:07 | +10 | ETH | DOWN | 0.56 | open |  |
| 10-05 16:07 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 10-05 16:07 | +10 stop | BNB | DOWN | 0.50 | open |  |
| 10-05 16:07 | +10 | BNB | DOWN | 0.50 | open |  |
| 10-05 16:06 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-05 16:06 | +10 stop | BTC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-05 16:06 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-05 16:06 | +10 stop | XRP | UP | 0.54 | 0.67 | 0.96 |
| 10-05 16:06 | +10 stop | ZEC | UP | 0.46 | 0.27 | -2.22 |
| 10-05 16:06 | +10 | ZEC | UP | 0.46 | open |  |
| 10-05 16:06 | +5 | ZEC | UP | 0.46 | 0.53 | 0.34 |
| 10-05 16:05 | +10 stop | BNB | DOWN | 0.53 | 0.65 | 0.82 |
| 10-05 16:05 | +20 | BNB | DOWN | 0.53 | open |  |
| 10-05 16:05 | +15 | BNB | DOWN | 0.53 | open |  |
| 10-05 16:05 | +10 | BNB | DOWN | 0.53 | 0.65 | 0.82 |
| 10-05 16:05 | +5 | BNB | DOWN | 0.53 | 0.62 | 0.55 |
| 10-05 16:05 | +10 stop | ZEC | DOWN | 0.45 | 0.57 | 0.84 |
| 10-05 16:05 | +15 | ZEC | DOWN | 0.47 | 0.71 | 2.07 |
| 10-05 16:05 | +10 | ZEC | DOWN | 0.47 | 0.57 | 0.64 |
| 10-05 16:05 | +5 | ZEC | DOWN | 0.47 | 0.57 | 0.64 |
| 10-05 16:05 | +5 | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 10-05 16:05 | +10 stop | DOGE | DOWN | 0.49 | 0.64 | 1.15 |
| 10-05 16:05 | +20 | DOGE | DOWN | 0.50 | open |  |
| 10-05 16:05 | +15 | DOGE | DOWN | 0.52 | 0.67 | 1.16 |
| 10-05 16:05 | +10 | DOGE | DOWN | 0.52 | 0.64 | 0.85 |
| 10-05 16:05 | +5 | DOGE | DOWN | 0.52 | 0.64 | 0.85 |
| 10-05 16:05 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-05 16:05 | +10 stop | XRP | DOWN | 0.59 | 0.33 | -2.93 |
