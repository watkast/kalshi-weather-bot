# Range-Scalp Bot

*Updated Sat Oct 03 14:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 885 | 774 | 111 (1) | 5 | $-239.96 | -4.3% |
| **+10¢** | 672 | 550 | 122 (3) | 5 | $-128.54 | -3.0% |
| **+15¢** | 567 | 434 | 133 (4) | 7 | $-118.84 | -3.3% |
| **+20¢** | 497 | 358 | 139 (4) | 8 | $-100.67 | -3.2% |
| **+10¢ (15¢ stop)** | 1127 | 1126 | 1 (1) | 0 | $-566.53 | -8.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 14:36 | +10 stop | NEAR | DOWN | 0.68 | 0.50 | -2.14 |
| 10-03 14:36 | +5 | NEAR | UP | 0.62 | open |  |
| 10-03 14:35 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-03 14:35 | +10 stop | ETH | DOWN | 0.63 | 0.85 | 1.94 |
| 10-03 14:34 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-03 14:34 | +5 | BNB | UP | 0.70 | 0.79 | 0.60 |
| 10-03 14:34 | +5 | DOGE | UP | 0.57 | open |  |
| 10-03 14:34 | +10 stop | ETH | UP | 0.46 | 0.57 | 0.74 |
| 10-03 14:33 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-03 14:33 | +10 stop | DOGE | UP | 0.56 | 0.28 | -3.08 |
| 10-03 14:33 | +10 stop | ETH | UP | 0.69 | 0.52 | -2.03 |
| 10-03 14:33 | +20 | ETH | UP | 0.69 | open |  |
| 10-03 14:33 | +15 | ETH | UP | 0.69 | open |  |
| 10-03 14:33 | +10 | ETH | UP | 0.69 | open |  |
| 10-03 14:33 | +5 | ETH | UP | 0.69 | open |  |
| 10-03 14:33 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 10-03 14:33 | +10 stop | XRP | DOWN | 0.64 | 0.47 | -2.05 |
| 10-03 14:33 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-03 14:33 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-03 14:33 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-03 14:33 | +5 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-03 14:33 | +10 stop | NEAR | UP | 0.66 | 0.43 | -2.64 |
| 10-03 14:33 | +10 | NEAR | UP | 0.66 | open |  |
| 10-03 14:33 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 10-03 14:32 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-03 14:32 | +20 | BTC | DOWN | 0.67 | 0.91 | 2.18 |
| 10-03 14:32 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-03 14:32 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-03 14:32 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-03 14:32 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.95 |
| 10-03 14:32 | +20 | SOL | UP | 0.56 | open |  |
| 10-03 14:32 | +15 | SOL | UP | 0.56 | open |  |
| 10-03 14:32 | +10 | SOL | UP | 0.56 | open |  |
| 10-03 14:32 | +5 | SOL | UP | 0.56 | open |  |
| 10-03 14:31 | +10 stop | HYPE | UP | 0.57 | 0.30 | -3.03 |
| 10-03 14:31 | +20 | HYPE | UP | 0.57 | open |  |
| 10-03 14:31 | +15 | HYPE | UP | 0.57 | open |  |
| 10-03 14:31 | +10 | HYPE | UP | 0.57 | open |  |
| 10-03 14:31 | +5 | HYPE | UP | 0.57 | open |  |
| 10-03 14:31 | +10 stop | DOGE | UP | 0.70 | 0.54 | -1.93 |
