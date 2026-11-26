# Range-Scalp Bot

*Updated Thu Nov 26 14:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72805 | 63542 | 9263 (158) | 0 | $-19415.76 | -4.2% |
| **+10¢** | 54282 | 43468 | 10814 (203) | 0 | $-18001.73 | -5.3% |
| **+15¢** | 45454 | 33804 | 11650 (261) | 0 | $-16113.08 | -5.7% |
| **+20¢** | 40457 | 28190 | 12267 (327) | 0 | $-14506.41 | -5.7% |
| **+10¢ (15¢ stop)** | 88664 | 88455 | 209 (128) | 0 | $-32670.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 14:25 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-26 14:24 | +10 stop | SOL | DOWN | 0.65 | 0.83 | 1.52 |
| 11-26 14:24 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-26 14:24 | +10 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-26 14:24 | +5 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-26 14:23 | +10 stop | DOGE | UP | 0.54 | 0.70 | 1.27 |
| 11-26 14:22 | +10 stop | DOGE | DOWN | 0.60 | 0.42 | -2.15 |
| 11-26 14:20 | +10 stop | DOGE | UP | 0.50 | 0.35 | -1.84 |
| 11-26 14:19 | +5 | HYPE | UP | 0.54 | 0.61 | 0.35 |
| 11-26 14:19 | +10 stop | DOGE | DOWN | 0.55 | 0.33 | -2.54 |
| 11-26 14:18 | +10 stop | HYPE | DOWN | 0.52 | 0.37 | -1.85 |
| 11-26 14:18 | +20 | HYPE | DOWN | 0.52 | 0.81 | 2.63 |
| 11-26 14:18 | +15 | HYPE | DOWN | 0.53 | 0.81 | 2.51 |
| 11-26 14:18 | +10 | HYPE | DOWN | 0.53 | 0.81 | 2.51 |
| 11-26 14:18 | +5 | HYPE | DOWN | 0.49 | 0.61 | 0.85 |
| 11-26 14:17 | +10 stop | DOGE | UP | 0.68 | 0.53 | -1.84 |
| 11-26 14:17 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-26 14:17 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-26 14:17 | +20 | BTC | DOWN | 0.69 | 0.91 | 1.95 |
| 11-26 14:17 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-26 14:17 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-26 14:17 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-26 14:17 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-26 14:17 | +20 | BNB | DOWN | 0.70 | 0.92 | 2.00 |
| 11-26 14:17 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 14:17 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-26 14:17 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 11-26 14:16 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 11-26 14:16 | +20 | SOL | DOWN | 0.70 | 0.96 | 2.47 |
| 11-26 14:16 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 14:16 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 14:16 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-26 14:16 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.85 |
| 11-26 14:16 | +20 | DOGE | DOWN | 0.61 | yes | -6.27 |
| 11-26 14:16 | +15 | DOGE | DOWN | 0.61 | yes | -6.27 |
| 11-26 14:16 | +10 | DOGE | DOWN | 0.62 | yes | -6.37 |
| 11-26 14:16 | +5 | DOGE | DOWN | 0.62 | yes | -6.37 |
| 11-26 14:16 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-26 14:16 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
| 11-26 14:16 | +15 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
