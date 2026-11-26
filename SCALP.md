# Range-Scalp Bot

*Updated Thu Nov 26 22:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73020 | 63734 | 9286 (158) | 6 | $-19454.83 | -4.2% |
| **+10¢** | 54434 | 43594 | 10840 (203) | 6 | $-18041.00 | -5.3% |
| **+15¢** | 45586 | 33908 | 11678 (261) | 7 | $-16133.96 | -5.6% |
| **+20¢** | 40562 | 28267 | 12295 (327) | 9 | $-14524.56 | -5.7% |
| **+10¢ (15¢ stop)** | 88916 | 88707 | 209 (128) | 0 | $-32790.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 22:54 | +5 | HYPE | UP | 0.65 | open |  |
| 11-26 22:54 | +10 stop | ETH | UP | 0.47 | 0.11 | -3.85 |
| 11-26 22:53 | +10 stop | HYPE | UP | 0.60 | 0.33 | -3.03 |
| 11-26 22:53 | +15 | HYPE | UP | 0.60 | open |  |
| 11-26 22:53 | +10 | HYPE | UP | 0.60 | open |  |
| 11-26 22:53 | +5 | HYPE | UP | 0.60 | 0.65 | 0.17 |
| 11-26 22:53 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.77 |
| 11-26 22:52 | +5 | ETH | UP | 0.67 | open |  |
| 11-26 22:51 | +10 stop | SOL | UP | 0.57 | 0.38 | -2.25 |
| 11-26 22:51 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.93 |
| 11-26 22:51 | +15 | NEAR | UP | 0.70 | open |  |
| 11-26 22:51 | +10 | NEAR | UP | 0.70 | open |  |
| 11-26 22:51 | +10 stop | ZEC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-26 22:51 | +5 | NEAR | UP | 0.71 | open |  |
| 11-26 22:50 | +10 stop | ETH | UP | 0.69 | 0.51 | -2.13 |
| 11-26 22:50 | +10 | ETH | UP | 0.69 | open |  |
| 11-26 22:50 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-26 22:50 | +5 | XRP | UP | 0.62 | open |  |
| 11-26 22:49 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-26 22:49 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-26 22:49 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-26 22:48 | +10 stop | SOL | UP | 0.64 | 0.48 | -1.95 |
| 11-26 22:48 | +15 | SOL | UP | 0.64 | open |  |
| 11-26 22:48 | +10 | SOL | UP | 0.64 | open |  |
| 11-26 22:48 | +5 | SOL | UP | 0.64 | open |  |
| 11-26 22:47 | +10 stop | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-26 22:47 | +20 | BTC | UP | 0.66 | open |  |
| 11-26 22:47 | +15 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-26 22:47 | +10 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-26 22:47 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 11-26 22:47 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-26 22:47 | +20 | ETH | UP | 0.62 | open |  |
| 11-26 22:47 | +15 | ETH | UP | 0.62 | open |  |
| 11-26 22:47 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-26 22:47 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-26 22:47 | +5 | ZEC | UP | 0.67 | open |  |
| 11-26 22:47 | +10 stop | XRP | UP | 0.58 | 0.28 | -3.35 |
| 11-26 22:47 | +20 | XRP | UP | 0.58 | open |  |
| 11-26 22:47 | +15 | XRP | UP | 0.58 | open |  |
| 11-26 22:47 | +10 | XRP | UP | 0.58 | open |  |
