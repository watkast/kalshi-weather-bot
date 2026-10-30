# Range-Scalp Bot

*Updated Fri Oct 30 16:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40966 | 35759 | 5207 (53) | 0 | $-11411.11 | -4.4% |
| **+10¢** | 30519 | 24496 | 6023 (76) | 1 | $-10154.81 | -5.3% |
| **+15¢** | 25517 | 19028 | 6489 (103) | 1 | $-9206.55 | -5.7% |
| **+20¢** | 22651 | 15851 | 6800 (133) | 1 | $-8115.69 | -5.7% |
| **+10¢ (15¢ stop)** | 49951 | 49881 | 70 (37) | 0 | $-18919.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 16:27 | +10 stop | HYPE | DOWN | 0.64 | 0.39 | -2.84 |
| 10-30 16:26 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.33 |
| 10-30 16:26 | +10 stop | XRP | UP | 0.44 | 0.62 | 1.45 |
| 10-30 16:25 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-30 16:25 | +10 stop | DOGE | UP | 0.68 | 0.51 | -2.04 |
| 10-30 16:24 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 16:24 | +10 stop | SOL | DOWN | 0.47 | 0.19 | -3.09 |
| 10-30 16:24 | +15 | SOL | DOWN | 0.47 | open |  |
| 10-30 16:24 | +10 | SOL | DOWN | 0.47 | open |  |
| 10-30 16:24 | +5 | SOL | DOWN | 0.47 | 0.54 | 0.34 |
| 10-30 16:24 | +10 stop | XRP | DOWN | 0.64 | 0.45 | -2.25 |
| 10-30 16:24 | +10 stop | DOGE | DOWN | 0.69 | 0.52 | -2.03 |
| 10-30 16:22 | +5 | ETH | UP | 0.52 | 0.64 | 0.85 |
| 10-30 16:22 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-30 16:22 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-30 16:22 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-30 16:22 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 16:22 | +5 | SOL | DOWN | 0.63 | 0.72 | 0.58 |
| 10-30 16:22 | +10 stop | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 10-30 16:22 | +10 stop | ETH | UP | 0.58 | 0.37 | -2.45 |
| 10-30 16:22 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 10-30 16:21 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-30 16:21 | +10 stop | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-30 16:18 | +20 | ETH | UP | 0.71 | 0.96 | 2.32 |
| 10-30 16:18 | +15 | ETH | UP | 0.71 | 0.89 | 1.58 |
| 10-30 16:18 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 10-30 16:18 | +5 | NEAR | UP | 0.66 | 0.80 | 1.12 |
| 10-30 16:17 | +5 | HYPE | UP | 0.57 | 0.95 | 3.50 |
| 10-30 16:17 | +10 stop | ETH | UP | 0.68 | 0.53 | -1.84 |
| 10-30 16:17 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-30 16:17 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 10-30 16:17 | +10 stop | HYPE | UP | 0.52 | 0.34 | -2.14 |
| 10-30 16:17 | +20 | HYPE | UP | 0.52 | 0.95 | 4.04 |
| 10-30 16:17 | +15 | HYPE | UP | 0.52 | 0.95 | 4.04 |
| 10-30 16:17 | +10 | HYPE | UP | 0.52 | 0.95 | 4.04 |
| 10-30 16:17 | +5 | HYPE | UP | 0.52 | 0.59 | 0.35 |
| 10-30 16:17 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 10-30 16:17 | +20 | BTC | UP | 0.62 | 0.95 | 3.06 |
| 10-30 16:17 | +15 | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-30 16:17 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
