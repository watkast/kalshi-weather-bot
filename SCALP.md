# Range-Scalp Bot

*Updated Wed Oct 07 13:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6506 | 5650 | 856 (9) | 4 | $-1958.23 | -4.8% |
| **+10¢** | 4939 | 3934 | 1005 (16) | 7 | $-1839.89 | -5.9% |
| **+15¢** | 4147 | 3085 | 1062 (20) | 7 | $-1552.26 | -6.0% |
| **+20¢** | 3708 | 2598 | 1110 (27) | 8 | $-1261.35 | -5.4% |
| **+10¢ (15¢ stop)** | 7903 | 7888 | 15 (9) | 0 | $-2796.55 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
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
| 10-07 13:47 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-07 13:47 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 10-07 13:47 | +10 stop | SOL | DOWN | 0.61 | 0.43 | -2.15 |
| 10-07 13:46 | +5 | HYPE | UP | 0.62 | open |  |
| 10-07 13:46 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 13:46 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-07 13:46 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-07 13:46 | +10 | NEAR | DOWN | 0.62 | 0.72 | 0.70 |
| 10-07 13:46 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.40 |
| 10-07 13:46 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 10-07 13:46 | +20 | ZEC | UP | 0.59 | open |  |
| 10-07 13:46 | +15 | ZEC | UP | 0.59 | open |  |
| 10-07 13:46 | +10 | ZEC | UP | 0.59 | open |  |
| 10-07 13:46 | +5 | ZEC | UP | 0.60 | open |  |
| 10-07 13:46 | +10 stop | SOL | UP | 0.62 | 0.42 | -2.35 |
| 10-07 13:46 | +20 | SOL | UP | 0.62 | open |  |
| 10-07 13:46 | +15 | SOL | UP | 0.62 | open |  |
| 10-07 13:46 | +10 | SOL | UP | 0.62 | open |  |
| 10-07 13:46 | +5 | SOL | UP | 0.62 | open |  |
| 10-07 13:45 | +10 stop | ETH | UP | 0.62 | 0.35 | -3.03 |
| 10-07 13:45 | +20 | ETH | UP | 0.62 | open |  |
| 10-07 13:45 | +15 | ETH | UP | 0.62 | open |  |
| 10-07 13:45 | +10 | ETH | UP | 0.63 | open |  |
| 10-07 13:45 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
