# Range-Scalp Bot

*Updated Sun Nov 01 22:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44033 | 38353 | 5680 (65) | 3 | $-12673.93 | -4.6% |
| **+10¢** | 32859 | 26298 | 6561 (86) | 3 | $-11407.24 | -5.5% |
| **+15¢** | 27500 | 20439 | 7061 (113) | 3 | $-10412.55 | -6.0% |
| **+20¢** | 24428 | 17034 | 7394 (147) | 3 | $-9169.98 | -6.0% |
| **+10¢ (15¢ stop)** | 53712 | 53626 | 86 (51) | 0 | $-20329.92 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 22:51 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-01 22:51 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 11-01 22:51 | +15 | NEAR | UP | 0.58 | 0.73 | 1.18 |
| 11-01 22:51 | +10 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-01 22:51 | +5 | NEAR | UP | 0.59 | 0.68 | 0.57 |
| 11-01 22:51 | +5 | ZEC | UP | 0.70 | 0.83 | 1.02 |
| 11-01 22:51 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-01 22:50 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-01 22:50 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-01 22:49 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-01 22:49 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-01 22:49 | +10 stop | ETH | DOWN | 0.58 | 0.30 | -3.13 |
| 11-01 22:48 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-01 22:47 | +10 stop | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 11-01 22:47 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-01 22:47 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-01 22:47 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-01 22:47 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-01 22:47 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-01 22:46 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 11-01 22:46 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-01 22:46 | +15 | ETH | DOWN | 0.67 | open |  |
| 11-01 22:46 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-01 22:46 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-01 22:46 | +10 stop | HYPE | DOWN | 0.65 | 0.50 | -1.84 |
| 11-01 22:46 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-01 22:46 | +15 | HYPE | DOWN | 0.65 | open |  |
| 11-01 22:46 | +10 | HYPE | DOWN | 0.65 | open |  |
| 11-01 22:46 | +5 | HYPE | DOWN | 0.65 | open |  |
| 11-01 22:46 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 11-01 22:46 | +20 | SOL | UP | 0.61 | 0.81 | 1.72 |
| 11-01 22:46 | +15 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 11-01 22:46 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-01 22:46 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-01 22:46 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-01 22:46 | +20 | BTC | UP | 0.61 | 0.81 | 1.72 |
| 11-01 22:46 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 11-01 22:46 | +10 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-01 22:46 | +5 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-01 22:46 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
