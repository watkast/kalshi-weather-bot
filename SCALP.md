# Range-Scalp Bot

*Updated Thu Nov 19 01:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64540 | 56299 | 8241 (124) | 1 | $-17558.24 | -4.3% |
| **+10¢** | 48219 | 38582 | 9637 (165) | 1 | $-16358.02 | -5.4% |
| **+15¢** | 40437 | 30050 | 10387 (210) | 1 | $-14758.53 | -5.8% |
| **+20¢** | 36011 | 25107 | 10904 (265) | 2 | $-13042.03 | -5.8% |
| **+10¢ (15¢ stop)** | 78552 | 78388 | 164 (98) | 0 | $-28887.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 01:32 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-19 01:32 | +10 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-19 01:32 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-19 01:32 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-19 01:32 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-19 01:32 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-19 01:32 | +15 | XRP | DOWN | 0.60 | 0.82 | 1.92 |
| 11-19 01:32 | +10 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-19 01:32 | +5 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-19 01:32 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-19 01:32 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 11-19 01:32 | +15 | HYPE | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 01:32 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-19 01:32 | +5 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-19 01:31 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-19 01:31 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 01:31 | +20 | ETH | DOWN | 0.69 | 0.91 | 2.01 |
| 11-19 01:31 | +15 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 11-19 01:31 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 01:31 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-19 01:31 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-19 01:31 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-19 01:31 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.32 |
| 11-19 01:31 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 01:31 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-19 01:31 | +20 | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 11-19 01:31 | +15 | BTC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-19 01:31 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-19 01:31 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-19 01:30 | +10 stop | DOGE | UP | 0.57 | 0.38 | -2.25 |
| 11-19 01:30 | +20 | DOGE | UP | 0.57 | open |  |
| 11-19 01:30 | +15 | DOGE | UP | 0.58 | open |  |
| 11-19 01:30 | +10 | DOGE | UP | 0.59 | open |  |
| 11-19 01:30 | +5 | DOGE | UP | 0.60 | open |  |
| 11-19 01:16 | +10 stop | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 11-19 01:16 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-19 01:16 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-19 01:16 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-19 01:16 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-19 01:12 | +10 stop | HYPE | DOWN | 0.68 | 0.27 | -4.36 |
