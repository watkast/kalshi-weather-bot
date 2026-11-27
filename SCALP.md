# Range-Scalp Bot

*Updated Fri Nov 27 18:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73919 | 64513 | 9406 (171) | 3 | $-19652.11 | -4.2% |
| **+10¢** | 55069 | 44083 | 10986 (216) | 3 | $-18288.34 | -5.3% |
| **+15¢** | 46114 | 34284 | 11830 (274) | 4 | $-16346.68 | -5.6% |
| **+20¢** | 41037 | 28576 | 12461 (341) | 5 | $-14772.87 | -5.7% |
| **+10¢ (15¢ stop)** | 90005 | 89786 | 219 (135) | 2 | $-33330.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 18:39 | +5 | BTC | UP | 0.65 | open |  |
| 11-27 18:39 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-27 18:39 | +5 | BTC | UP | 0.61 | 0.69 | 0.48 |
| 11-27 18:39 | +10 stop | ETH | UP | 0.70 | open |  |
| 11-27 18:39 | +10 | ETH | UP | 0.70 | open |  |
| 11-27 18:38 | +10 stop | DOGE | DOWN | 0.69 | 0.46 | -2.63 |
| 11-27 18:38 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-27 18:38 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-27 18:37 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 11-27 18:37 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 11-27 18:37 | +5 | BTC | UP | 0.55 | 0.66 | 0.76 |
| 11-27 18:37 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-27 18:37 | +10 stop | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 11-27 18:36 | +10 stop | NEAR | DOWN | 0.50 | 0.32 | -2.14 |
| 11-27 18:36 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 11-27 18:36 | +5 | BTC | UP | 0.47 | 0.59 | 0.85 |
| 11-27 18:35 | +10 stop | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-27 18:35 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-27 18:35 | +5 | BTC | UP | 0.54 | 0.60 | 0.25 |
| 11-27 18:35 | +10 stop | HYPE | UP | 0.65 | 0.47 | -2.14 |
| 11-27 18:35 | +20 | HYPE | UP | 0.65 | open |  |
| 11-27 18:35 | +15 | HYPE | UP | 0.65 | 0.81 | 1.33 |
| 11-27 18:35 | +10 | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 11-27 18:35 | +5 | HYPE | UP | 0.65 | 0.74 | 0.60 |
| 11-27 18:35 | +10 stop | ZEC | DOWN | 0.61 | 0.32 | -3.23 |
| 11-27 18:34 | +5 | BTC | UP | 0.55 | 0.64 | 0.55 |
| 11-27 18:34 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 11-27 18:34 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 11-27 18:34 | +10 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 11-27 18:34 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 11-27 18:34 | +5 | ZEC | UP | 0.48 | 0.59 | 0.75 |
| 11-27 18:34 | +10 stop | NEAR | UP | 0.56 | 0.39 | -2.09 |
| 11-27 18:34 | +10 | NEAR | UP | 0.56 | 0.67 | 0.72 |
| 11-27 18:33 | +10 stop | DOGE | UP | 0.64 | 0.46 | -2.11 |
| 11-27 18:33 | +5 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 11-27 18:33 | +10 stop | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 11-27 18:33 | +20 | NEAR | UP | 0.54 | 0.78 | 2.09 |
| 11-27 18:33 | +15 | NEAR | UP | 0.54 | 0.70 | 1.27 |
| 11-27 18:33 | +10 | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 11-27 18:33 | +5 | NEAR | UP | 0.55 | 0.60 | 0.15 |
