# Range-Scalp Bot

*Updated Thu Nov 05 01:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47822 | 41642 | 6180 (73) | 1 | $-13784.61 | -4.6% |
| **+10¢** | 35734 | 28562 | 7172 (98) | 1 | $-12614.09 | -5.6% |
| **+15¢** | 29941 | 22217 | 7724 (126) | 1 | $-11552.20 | -6.1% |
| **+20¢** | 26602 | 18512 | 8090 (166) | 3 | $-10195.27 | -6.1% |
| **+10¢ (15¢ stop)** | 58313 | 58220 | 93 (56) | 1 | $-21697.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 01:37 | +10 stop | HYPE | UP | 0.50 | open |  |
| 11-05 01:37 | +10 | HYPE | UP | 0.50 | open |  |
| 11-05 01:37 | +5 | HYPE | UP | 0.50 | open |  |
| 11-05 01:31 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.75 |
| 11-05 01:31 | +20 | HYPE | UP | 0.64 | open |  |
| 11-05 01:31 | +15 | HYPE | UP | 0.64 | open |  |
| 11-05 01:31 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 01:31 | +5 | HYPE | UP | 0.65 | 0.71 | 0.25 |
| 11-05 01:31 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-05 01:31 | +20 | SOL | UP | 0.71 | open |  |
| 11-05 01:31 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 11-05 01:31 | +10 | SOL | UP | 0.70 | 0.80 | 0.73 |
| 11-05 01:31 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 11-05 01:31 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-05 01:31 | +20 | BTC | UP | 0.71 | open |  |
| 11-05 01:31 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-05 01:31 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-05 01:31 | +5 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-05 01:31 | +10 stop | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 11-05 01:31 | +20 | NEAR | UP | 0.64 | 0.86 | 1.94 |
| 11-05 01:31 | +15 | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 11-05 01:31 | +10 | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 11-05 01:31 | +5 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-05 01:27 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 01:27 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 01:27 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 11-05 01:24 | +10 stop | NEAR | DOWN | 0.67 | 0.51 | -1.94 |
| 11-05 01:24 | +20 | NEAR | DOWN | 0.68 | yes | -6.96 |
| 11-05 01:24 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 11-05 01:24 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 01:24 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 01:24 | +10 stop | ZEC | DOWN | 0.55 | 0.36 | -2.25 |
| 11-05 01:24 | +20 | ZEC | DOWN | 0.55 | yes | -5.68 |
| 11-05 01:24 | +15 | ZEC | DOWN | 0.55 | yes | -5.68 |
| 11-05 01:24 | +10 | ZEC | DOWN | 0.55 | yes | -5.68 |
| 11-05 01:24 | +5 | ZEC | DOWN | 0.56 | yes | -5.78 |
| 11-05 01:18 | +10 stop | NEAR | DOWN | 0.70 | 0.92 | 1.99 |
| 11-05 01:18 | +10 | NEAR | DOWN | 0.70 | 0.92 | 1.99 |
| 11-05 01:18 | +5 | NEAR | DOWN | 0.70 | 0.78 | 0.52 |
| 11-05 01:16 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
