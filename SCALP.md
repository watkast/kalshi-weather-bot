# Range-Scalp Bot

*Updated Sat Oct 10 06:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10043 | 8666 | 1377 (18) | 5 | $-3403.45 | -5.4% |
| **+10¢** | 7588 | 5983 | 1605 (30) | 6 | $-3271.55 | -6.8% |
| **+15¢** | 6405 | 4713 | 1692 (43) | 7 | $-2701.94 | -6.7% |
| **+20¢** | 5692 | 3935 | 1757 (55) | 8 | $-2257.39 | -6.3% |
| **+10¢ (15¢ stop)** | 12342 | 12307 | 35 (22) | 0 | $-4844.07 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 06:04 | +10 stop | ZEC | DOWN | 0.57 | 0.73 | 1.27 |
| 10-10 06:04 | +5 | ZEC | DOWN | 0.57 | 0.64 | 0.34 |
| 10-10 06:03 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 06:02 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 06:02 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 06:02 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-10 06:02 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-10 06:02 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-10 06:02 | +10 stop | ZEC | UP | 0.70 | 0.46 | -2.73 |
| 10-10 06:02 | +20 | ZEC | UP | 0.70 | open |  |
| 10-10 06:02 | +15 | ZEC | UP | 0.70 | open |  |
| 10-10 06:02 | +10 | ZEC | UP | 0.70 | open |  |
| 10-10 06:02 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
| 10-10 06:02 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-10 06:02 | +10 stop | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-10 06:02 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.88 |
| 10-10 06:02 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-10 06:02 | +10 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-10 06:02 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-10 06:01 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 10-10 06:01 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-10 06:01 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-10 06:01 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-10 06:01 | +10 stop | HYPE | UP | 0.61 | 0.46 | -1.89 |
| 10-10 06:01 | +20 | HYPE | UP | 0.63 | open |  |
| 10-10 06:01 | +15 | HYPE | UP | 0.63 | open |  |
| 10-10 06:01 | +10 | HYPE | UP | 0.63 | open |  |
| 10-10 06:01 | +5 | HYPE | UP | 0.63 | open |  |
| 10-10 06:01 | +5 | ETH | UP | 0.56 | open |  |
| 10-10 06:01 | +10 stop | XRP | UP | 0.62 | 0.40 | -2.54 |
| 10-10 06:01 | +20 | XRP | UP | 0.62 | open |  |
| 10-10 06:01 | +15 | XRP | UP | 0.62 | open |  |
| 10-10 06:01 | +10 | XRP | UP | 0.62 | open |  |
| 10-10 06:01 | +5 | XRP | UP | 0.62 | open |  |
| 10-10 06:01 | +10 stop | ETH | UP | 0.60 | 0.36 | -2.74 |
| 10-10 06:01 | +20 | ETH | UP | 0.60 | open |  |
| 10-10 06:01 | +15 | ETH | UP | 0.60 | open |  |
| 10-10 06:01 | +10 | ETH | UP | 0.60 | open |  |
| 10-10 06:01 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-10 06:01 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.89 |
