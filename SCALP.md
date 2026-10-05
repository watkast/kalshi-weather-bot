# Range-Scalp Bot

*Updated Mon Oct 05 05:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3373 | 2897 | 476 (3) | 7 | $-1206.26 | -5.7% |
| **+10¢** | 2603 | 2062 | 541 (4) | 9 | $-1068.78 | -6.5% |
| **+15¢** | 2189 | 1616 | 573 (5) | 9 | $-963.84 | -7.0% |
| **+20¢** | 1952 | 1353 | 599 (10) | 9 | $-839.29 | -6.9% |
| **+10¢ (15¢ stop)** | 4196 | 4195 | 1 (1) | 0 | $-1629.42 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 05:36 | +10 stop | ZEC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 05:35 | +10 stop | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-05 05:34 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-05 05:34 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 10-05 05:34 | +10 stop | BNB | DOWN | 0.54 | 0.38 | -1.98 |
| 10-05 05:34 | +5 | BNB | DOWN | 0.54 | open |  |
| 10-05 05:34 | +10 stop | BTC | UP | 0.60 | 0.73 | 0.99 |
| 10-05 05:33 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-05 05:33 | +10 stop | DOGE | DOWN | 0.62 | 0.42 | -2.35 |
| 10-05 05:33 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-05 05:33 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.92 |
| 10-05 05:33 | +10 stop | ZEC | DOWN | 0.60 | 0.40 | -2.34 |
| 10-05 05:33 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-05 05:33 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-05 05:33 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-05 05:33 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-05 05:33 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-05 05:33 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-05 05:33 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-05 05:33 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-05 05:33 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-05 05:33 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 10-05 05:33 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-05 05:33 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-05 05:33 | +5 | XRP | DOWN | 0.53 | 0.61 | 0.45 |
| 10-05 05:32 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-05 05:32 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-05 05:31 | +10 stop | HYPE | DOWN | 0.57 | 0.39 | -2.15 |
| 10-05 05:31 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-05 05:31 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-05 05:31 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-05 05:31 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-05 05:31 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 10-05 05:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-05 05:31 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-05 05:31 | +10 | ETH | DOWN | 0.69 | open |  |
| 10-05 05:31 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-05 05:31 | +10 stop | BTC | DOWN | 0.67 | 0.50 | -2.04 |
| 10-05 05:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-05 05:31 | +15 | BTC | DOWN | 0.67 | open |  |
