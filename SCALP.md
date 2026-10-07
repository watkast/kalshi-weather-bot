# Range-Scalp Bot

*Updated Wed Oct 07 13:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6515 | 5659 | 856 (9) | 3 | $-1950.09 | -4.7% |
| **+10¢** | 4946 | 3941 | 1005 (16) | 3 | $-1830.86 | -5.9% |
| **+15¢** | 4154 | 3092 | 1062 (20) | 3 | $-1540.72 | -5.9% |
| **+20¢** | 3713 | 2603 | 1110 (27) | 4 | $-1250.32 | -5.4% |
| **+10¢ (15¢ stop)** | 7912 | 7897 | 15 (9) | 0 | $-2807.25 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 13:51 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-07 13:50 | +10 stop | BTC | DOWN | 0.40 | 0.55 | 1.15 |
| 10-07 13:50 | +20 | BTC | DOWN | 0.40 | open |  |
| 10-07 13:50 | +15 | BTC | DOWN | 0.39 | 0.55 | 1.25 |
| 10-07 13:50 | +10 | BTC | DOWN | 0.39 | 0.55 | 1.25 |
| 10-07 13:50 | +5 | BTC | DOWN | 0.39 | 0.55 | 1.25 |
| 10-07 13:50 | +10 stop | NEAR | DOWN | 0.65 | 0.31 | -3.68 |
| 10-07 13:50 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-07 13:50 | +10 stop | XRP | DOWN | 0.68 | 0.26 | -4.50 |
| 10-07 13:50 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-07 13:50 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-07 13:50 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-07 13:49 | +5 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 10-07 13:49 | +15 | DOGE | UP | 0.60 | 0.84 | 2.13 |
| 10-07 13:49 | +10 | DOGE | UP | 0.60 | 0.84 | 2.13 |
| 10-07 13:49 | +10 stop | HYPE | DOWN | 0.59 | 0.25 | -3.71 |
| 10-07 13:49 | +10 stop | NEAR | UP | 0.60 | 0.39 | -2.47 |
| 10-07 13:49 | +10 stop | DOGE | UP | 0.64 | 0.84 | 1.73 |
| 10-07 13:49 | +5 | DOGE | UP | 0.62 | 0.67 | 0.19 |
| 10-07 13:49 | +10 stop | ETH | UP | 0.67 | 0.90 | 2.08 |
| 10-07 13:49 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 10-07 13:49 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-07 13:49 | +10 stop | BNB | DOWN | 0.52 | 0.62 | 0.65 |
| 10-07 13:49 | +5 | BNB | DOWN | 0.53 | 0.58 | 0.14 |
| 10-07 13:48 | +10 stop | ETH | DOWN | 0.44 | 0.61 | 1.35 |
| 10-07 13:48 | +5 | ETH | DOWN | 0.45 | 0.61 | 1.25 |
| 10-07 13:48 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.93 |
| 10-07 13:48 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-07 13:48 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-07 13:47 | +10 stop | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 13:47 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-07 13:47 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 13:47 | +10 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 13:47 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 10-07 13:47 | +10 stop | ETH | DOWN | 0.52 | 0.64 | 0.85 |
| 10-07 13:47 | +10 stop | ZEC | DOWN | 0.56 | 0.36 | -2.35 |
| 10-07 13:47 | +5 | ETH | DOWN | 0.49 | 0.57 | 0.44 |
| 10-07 13:47 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-07 13:47 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-07 13:47 | +15 | BNB | DOWN | 0.68 | open |  |
