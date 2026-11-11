# Range-Scalp Bot

*Updated Wed Nov 11 22:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56315 | 49111 | 7204 (95) | 8 | $-15395.74 | -4.3% |
| **+10¢** | 42079 | 33672 | 8407 (125) | 9 | $-14363.37 | -5.4% |
| **+15¢** | 35285 | 26225 | 9060 (159) | 9 | $-13047.37 | -5.9% |
| **+20¢** | 31435 | 21929 | 9506 (209) | 9 | $-11404.47 | -5.8% |
| **+10¢ (15¢ stop)** | 68634 | 68513 | 121 (73) | 0 | $-25315.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 22:50 | +5 | XRP | UP | 0.45 | 0.55 | 0.64 |
| 11-11 22:50 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 11-11 22:49 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.95 |
| 11-11 22:49 | +15 | XRP | UP | 0.54 | open |  |
| 11-11 22:49 | +10 | XRP | UP | 0.55 | open |  |
| 11-11 22:49 | +5 | XRP | UP | 0.55 | 0.61 | 0.25 |
| 11-11 22:49 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-11 22:49 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 22:49 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 11-11 22:49 | +10 stop | ETH | DOWN | 0.52 | 0.66 | 1.06 |
| 11-11 22:49 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-11 22:49 | +10 stop | XRP | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 22:49 | +15 | XRP | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 22:49 | +10 | XRP | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 22:49 | +5 | XRP | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 22:48 | +10 stop | ETH | UP | 0.50 | 0.18 | -3.49 |
| 11-11 22:48 | +10 | ETH | UP | 0.50 | open |  |
| 11-11 22:48 | +5 | SOL | UP | 0.53 | open |  |
| 11-11 22:47 | +5 | BTC | UP | 0.69 | open |  |
| 11-11 22:47 | +5 | ETH | UP | 0.68 | open |  |
| 11-11 22:47 | +5 | HYPE | UP | 0.62 | open |  |
| 11-11 22:47 | +5 | ZEC | UP | 0.64 | open |  |
| 11-11 22:46 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 11-11 22:46 | +5 | DOGE | UP | 0.63 | open |  |
| 11-11 22:46 | +10 stop | XRP | UP | 0.55 | 0.71 | 1.27 |
| 11-11 22:46 | +20 | XRP | UP | 0.55 | open |  |
| 11-11 22:46 | +15 | XRP | UP | 0.55 | 0.71 | 1.27 |
| 11-11 22:46 | +10 | XRP | UP | 0.55 | 0.71 | 1.27 |
| 11-11 22:46 | +5 | XRP | UP | 0.55 | 0.61 | 0.25 |
| 11-11 22:46 | +10 stop | NEAR | UP | 0.61 | 0.24 | -4.00 |
| 11-11 22:46 | +20 | NEAR | UP | 0.61 | open |  |
| 11-11 22:46 | +15 | NEAR | UP | 0.61 | open |  |
| 11-11 22:46 | +10 | NEAR | UP | 0.61 | open |  |
| 11-11 22:46 | +5 | NEAR | UP | 0.61 | open |  |
| 11-11 22:46 | +10 stop | SOL | UP | 0.52 | 0.17 | -3.78 |
| 11-11 22:46 | +20 | SOL | UP | 0.52 | open |  |
| 11-11 22:46 | +15 | SOL | UP | 0.52 | open |  |
| 11-11 22:46 | +10 | SOL | UP | 0.52 | open |  |
| 11-11 22:46 | +5 | SOL | UP | 0.52 | 0.57 | 0.14 |
| 11-11 22:46 | +10 stop | HYPE | UP | 0.58 | 0.43 | -1.86 |
