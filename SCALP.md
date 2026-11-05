# Range-Scalp Bot

*Updated Thu Nov 05 16:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48542 | 42302 | 6240 (73) | 2 | $-13775.09 | -4.5% |
| **+10¢** | 36229 | 28981 | 7248 (99) | 7 | $-12604.95 | -5.5% |
| **+15¢** | 30346 | 22539 | 7807 (127) | 7 | $-11510.85 | -6.0% |
| **+20¢** | 26961 | 18780 | 8181 (166) | 7 | $-10171.79 | -6.0% |
| **+10¢ (15¢ stop)** | 59150 | 59057 | 93 (56) | 1 | $-21915.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 16:10 | +10 stop | XRP | UP | 0.64 | 0.86 | 1.94 |
| 11-05 16:10 | +10 stop | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 11-05 16:10 | +15 | DOGE | UP | 0.71 | 0.88 | 1.47 |
| 11-05 16:10 | +10 | DOGE | UP | 0.71 | 0.88 | 1.47 |
| 11-05 16:10 | +5 | DOGE | UP | 0.71 | 0.88 | 1.47 |
| 11-05 16:10 | +10 stop | XRP | UP | 0.71 | 0.53 | -2.13 |
| 11-05 16:10 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-05 16:10 | +10 | XRP | UP | 0.69 | 0.86 | 1.46 |
| 11-05 16:10 | +5 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-05 16:10 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-05 16:10 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-05 16:10 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-05 16:10 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-05 16:10 | +5 | ETH | DOWN | 0.65 | open |  |
| 11-05 16:08 | +10 stop | XRP | UP | 0.59 | 0.77 | 1.50 |
| 11-05 16:08 | +10 | XRP | UP | 0.59 | 0.77 | 1.50 |
| 11-05 16:08 | +10 stop | DOGE | UP | 0.51 | 0.64 | 0.95 |
| 11-05 16:08 | +10 stop | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 11-05 16:08 | +5 | XRP | UP | 0.59 | 0.77 | 1.50 |
| 11-05 16:07 | +5 | ZEC | DOWN | 0.40 | 0.53 | 0.95 |
| 11-05 16:07 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-05 16:07 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-05 16:07 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 11-05 16:07 | +10 stop | DOGE | DOWN | 0.63 | 0.40 | -2.64 |
| 11-05 16:07 | +10 stop | ZEC | UP | 0.45 | 0.71 | 2.27 |
| 11-05 16:07 | +5 | ZEC | UP | 0.45 | 0.54 | 0.54 |
| 11-05 16:06 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 11-05 16:06 | +10 stop | BNB | UP | 0.58 | 0.71 | 0.97 |
| 11-05 16:06 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-05 16:05 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-05 16:05 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 11-05 16:05 | +5 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 11-05 16:05 | +10 stop | XRP | DOWN | 0.52 | 0.64 | 0.85 |
| 11-05 16:05 | +10 stop | ETH | DOWN | 0.53 | 0.74 | 1.78 |
| 11-05 16:05 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-05 16:05 | +10 stop | SOL | DOWN | 0.67 | 0.49 | -2.13 |
| 11-05 16:05 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-05 16:05 | +5 | ETH | DOWN | 0.55 | 0.63 | 0.45 |
| 11-05 16:05 | +10 stop | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-05 16:04 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.02 |
