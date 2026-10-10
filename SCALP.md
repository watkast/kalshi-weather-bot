# Range-Scalp Bot

*Updated Sat Oct 10 02:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9795 | 8449 | 1346 (18) | 1 | $-3334.61 | -5.4% |
| **+10¢** | 7400 | 5828 | 1572 (30) | 1 | $-3224.43 | -6.9% |
| **+15¢** | 6240 | 4582 | 1658 (43) | 1 | $-2694.61 | -6.9% |
| **+20¢** | 5551 | 3826 | 1725 (55) | 1 | $-2275.89 | -6.5% |
| **+10¢ (15¢ stop)** | 12014 | 11979 | 35 (22) | 1 | $-4651.82 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 02:00 | +10 stop | DOGE | DOWN | 0.53 | open |  |
| 10-10 02:00 | +20 | DOGE | DOWN | 0.53 | open |  |
| 10-10 02:00 | +15 | DOGE | DOWN | 0.53 | open |  |
| 10-10 02:00 | +10 | DOGE | DOWN | 0.53 | open |  |
| 10-10 02:00 | +5 | DOGE | DOWN | 0.53 | open |  |
| 10-10 01:54 | +15 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 10-10 01:54 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 10-10 01:47 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.12 |
| 10-10 01:47 | +10 stop | BTC | UP | 0.69 | 0.83 | 1.15 |
| 10-10 01:47 | +10 | BTC | UP | 0.69 | 0.83 | 1.15 |
| 10-10 01:46 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-10 01:45 | +10 stop | NEAR | DOWN | 0.59 | 0.33 | -2.93 |
| 10-10 01:45 | +20 | NEAR | DOWN | 0.60 | yes | -6.17 |
| 10-10 01:45 | +15 | NEAR | DOWN | 0.60 | yes | -6.17 |
| 10-10 01:45 | +10 | NEAR | DOWN | 0.60 | yes | -6.22 |
| 10-10 01:45 | +5 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 10-10 01:45 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-10 01:45 | +20 | BTC | UP | 0.60 | 0.83 | 2.03 |
| 10-10 01:45 | +15 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 10-10 01:45 | +10 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-10 01:45 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 10-10 01:45 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-10 01:45 | +20 | HYPE | UP | 0.64 | 0.85 | 1.84 |
| 10-10 01:45 | +15 | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 10-10 01:45 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-10 01:45 | +5 | HYPE | UP | 0.64 | 0.70 | 0.28 |
| 10-10 01:40 | +10 stop | BTC | UP | 0.61 | 0.72 | 0.78 |
| 10-10 01:38 | +10 stop | BTC | UP | 0.52 | 0.63 | 0.75 |
| 10-10 01:38 | +10 stop | BNB | UP | 0.59 | 0.89 | 2.76 |
| 10-10 01:38 | +15 | BNB | UP | 0.59 | 0.89 | 2.76 |
| 10-10 01:38 | +10 | BNB | UP | 0.59 | 0.89 | 2.76 |
| 10-10 01:38 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-10 01:38 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-10 01:38 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-10 01:38 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-10 01:38 | +10 stop | XRP | UP | 0.70 | 0.86 | 1.36 |
| 10-10 01:37 | +5 | BTC | DOWN | 0.68 | yes | -6.96 |
| 10-10 01:37 | +10 stop | ETH | DOWN | 0.64 | 0.44 | -2.35 |
| 10-10 01:36 | +10 stop | ZEC | DOWN | 0.54 | 0.39 | -1.85 |
| 10-10 01:36 | +10 stop | HYPE | DOWN | 0.60 | 0.42 | -2.15 |
