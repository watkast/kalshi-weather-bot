# Range-Scalp Bot

*Updated Sun Oct 25 05:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32633 | 28457 | 4176 (42) | 4 | $-9271.18 | -4.5% |
| **+10¢** | 24428 | 19591 | 4837 (60) | 4 | $-8301.78 | -5.4% |
| **+15¢** | 20449 | 15246 | 5203 (83) | 4 | $-7449.78 | -5.8% |
| **+20¢** | 18114 | 12669 | 5445 (105) | 4 | $-6590.37 | -5.8% |
| **+10¢ (15¢ stop)** | 40102 | 40042 | 60 (32) | 1 | $-15356.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 05:23 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-25 05:23 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 05:22 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 05:22 | +5 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 05:22 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-25 05:22 | +10 | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-25 05:22 | +5 | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-25 05:22 | +10 stop | HYPE | UP | 0.63 | 0.48 | -1.85 |
| 10-25 05:21 | +10 stop | XRP | DOWN | 0.71 | 0.90 | 1.72 |
| 10-25 05:21 | +15 | XRP | DOWN | 0.71 | 0.90 | 1.72 |
| 10-25 05:21 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-25 05:21 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-25 05:21 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-25 05:21 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-25 05:21 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 05:21 | +5 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 05:21 | +15 | DOGE | DOWN | 0.53 | 0.69 | 1.27 |
| 10-25 05:21 | +10 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-25 05:21 | +5 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-25 05:21 | +10 stop | ZEC | UP | 0.66 | 0.51 | -1.84 |
| 10-25 05:20 | +10 stop | XRP | DOWN | 0.69 | 0.53 | -1.93 |
| 10-25 05:20 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 05:20 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-25 05:20 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-25 05:20 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 05:20 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-25 05:20 | +10 stop | NEAR | UP | 0.66 | 0.40 | -2.93 |
| 10-25 05:20 | +15 | NEAR | UP | 0.66 | open |  |
| 10-25 05:20 | +10 | NEAR | UP | 0.66 | open |  |
| 10-25 05:20 | +5 | NEAR | UP | 0.66 | open |  |
| 10-25 05:19 | +5 | ZEC | UP | 0.63 | open |  |
| 10-25 05:19 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 10-25 05:19 | +10 stop | DOGE | UP | 0.67 | 0.45 | -2.54 |
| 10-25 05:18 | +10 stop | HYPE | UP | 0.66 | 0.48 | -2.14 |
| 10-25 05:18 | +10 | HYPE | UP | 0.66 | open |  |
| 10-25 05:18 | +5 | HYPE | UP | 0.66 | open |  |
| 10-25 05:18 | +10 stop | SOL | UP | 0.67 | 0.46 | -2.44 |
| 10-25 05:18 | +10 stop | XRP | UP | 0.63 | 0.47 | -1.95 |
| 10-25 05:18 | +10 stop | ETH | UP | 0.59 | 0.44 | -1.85 |
| 10-25 05:18 | +20 | ETH | UP | 0.59 | open |  |
