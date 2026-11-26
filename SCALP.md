# Range-Scalp Bot

*Updated Thu Nov 26 23:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73069 | 63777 | 9292 (158) | 4 | $-19470.38 | -4.2% |
| **+10¢** | 54473 | 43627 | 10846 (203) | 5 | $-18044.39 | -5.3% |
| **+15¢** | 45611 | 33925 | 11686 (261) | 5 | $-16157.36 | -5.6% |
| **+20¢** | 40586 | 28281 | 12305 (327) | 6 | $-14557.62 | -5.7% |
| **+10¢ (15¢ stop)** | 88974 | 88765 | 209 (128) | 0 | $-32813.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 23:26 | +10 stop | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-26 23:26 | +5 | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-26 23:26 | +10 stop | SOL | UP | 0.56 | 0.20 | -3.90 |
| 11-26 23:26 | +10 | SOL | UP | 0.57 | open |  |
| 11-26 23:26 | +5 | SOL | UP | 0.57 | open |  |
| 11-26 23:26 | +10 stop | BTC | UP | 0.67 | 0.35 | -3.52 |
| 11-26 23:26 | +10 | BTC | UP | 0.67 | open |  |
| 11-26 23:26 | +5 | BTC | UP | 0.67 | open |  |
| 11-26 23:25 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-26 23:25 | +10 stop | NEAR | DOWN | 0.67 | 0.91 | 2.27 |
| 11-26 23:24 | +5 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 11-26 23:24 | +10 stop | BNB | DOWN | 0.57 | 0.39 | -2.15 |
| 11-26 23:24 | +10 stop | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-26 23:24 | +10 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-26 23:24 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-26 23:24 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-26 23:24 | +10 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-26 23:24 | +10 stop | BTC | UP | 0.56 | 0.74 | 1.48 |
| 11-26 23:24 | +10 stop | HYPE | DOWN | 0.57 | 0.38 | -2.25 |
| 11-26 23:24 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-26 23:24 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-26 23:23 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-26 23:22 | +5 | DOGE | UP | 0.71 | 0.80 | 0.63 |
| 11-26 23:22 | +10 stop | NEAR | UP | 0.49 | 0.29 | -2.37 |
| 11-26 23:22 | +10 stop | XRP | UP | 0.60 | 0.45 | -1.85 |
| 11-26 23:22 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-26 23:22 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 11-26 23:22 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-26 23:22 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-26 23:22 | +15 | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 11-26 23:22 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-26 23:22 | +5 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-26 23:21 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.18 |
| 11-26 23:21 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 11-26 23:21 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-26 23:21 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-26 23:21 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-26 23:21 | +10 stop | NEAR | DOWN | 0.50 | 0.31 | -2.23 |
| 11-26 23:20 | +10 stop | DOGE | DOWN | 0.60 | 0.44 | -1.95 |
| 11-26 23:20 | +10 stop | ZEC | DOWN | 0.54 | 0.38 | -1.95 |
