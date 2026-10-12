# Range-Scalp Bot

*Updated Mon Oct 12 04:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13074 | 11291 | 1783 (25) | 3 | $-4294.63 | -5.2% |
| **+10¢** | 9912 | 7851 | 2061 (37) | 4 | $-4001.16 | -6.4% |
| **+15¢** | 8333 | 6132 | 2201 (55) | 5 | $-3517.24 | -6.7% |
| **+20¢** | 7420 | 5126 | 2294 (69) | 6 | $-3006.97 | -6.5% |
| **+10¢ (15¢ stop)** | 16119 | 16078 | 41 (25) | 0 | $-6368.55 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 04:55 | +10 stop | BTC | UP | 0.64 | 0.86 | 1.94 |
| 10-12 04:54 | +10 stop | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 10-12 04:53 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-12 04:52 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.05 |
| 10-12 04:52 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-12 04:52 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-12 04:52 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-12 04:52 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-12 04:52 | +15 | HYPE | UP | 0.66 | 0.85 | 1.65 |
| 10-12 04:51 | +10 | HYPE | UP | 0.68 | 0.79 | 0.78 |
| 10-12 04:51 | +5 | HYPE | UP | 0.68 | 0.75 | 0.36 |
| 10-12 04:51 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-12 04:51 | +10 stop | HYPE | UP | 0.63 | 0.75 | 0.85 |
| 10-12 04:51 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 10-12 04:51 | +10 stop | DOGE | UP | 0.56 | 0.67 | 0.77 |
| 10-12 04:50 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-12 04:50 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-12 04:49 | +10 stop | DOGE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-12 04:49 | +10 stop | BTC | DOWN | 0.70 | 0.44 | -2.93 |
| 10-12 04:49 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 10-12 04:49 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |
| 10-12 04:49 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-12 04:49 | +10 stop | XRP | DOWN | 0.65 | 0.48 | -2.04 |
| 10-12 04:49 | +5 | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 10-12 04:48 | +10 stop | HYPE | UP | 0.53 | 0.36 | -2.05 |
| 10-12 04:48 | +10 | HYPE | UP | 0.53 | 0.66 | 0.96 |
| 10-12 04:48 | +5 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 10-12 04:48 | +5 | HYPE | UP | 0.60 | 0.66 | 0.27 |
| 10-12 04:48 | +10 stop | SOL | UP | 0.64 | 0.47 | -2.05 |
| 10-12 04:48 | +10 stop | DOGE | UP | 0.64 | 0.44 | -2.35 |
| 10-12 04:48 | +10 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 10-12 04:48 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 10-12 04:47 | +10 stop | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-12 04:47 | +10 stop | BNB | DOWN | 0.67 | 0.47 | -2.34 |
| 10-12 04:47 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 04:47 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 04:47 | +10 stop | BTC | UP | 0.66 | 0.46 | -2.34 |
| 10-12 04:47 | +5 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 10-12 04:47 | +10 stop | HYPE | UP | 0.52 | 0.63 | 0.75 |
| 10-12 04:47 | +20 | HYPE | UP | 0.52 | 0.75 | 1.98 |
