# Range-Scalp Bot

*Updated Sun Nov 22 12:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68650 | 59901 | 8749 (142) | 2 | $-18481.17 | -4.3% |
| **+10¢** | 51258 | 41039 | 10219 (186) | 0 | $-17138.00 | -5.3% |
| **+15¢** | 42959 | 31944 | 11015 (237) | 1 | $-15374.89 | -5.7% |
| **+20¢** | 38245 | 26671 | 11574 (295) | 1 | $-13690.87 | -5.7% |
| **+10¢ (15¢ stop)** | 83617 | 83432 | 185 (116) | 0 | $-30784.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 12:41 | +10 stop | DOGE | UP | 0.69 | 0.83 | 1.15 |
| 11-22 12:41 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 11-22 12:41 | +10 stop | DOGE | UP | 0.61 | 0.74 | 0.99 |
| 11-22 12:40 | +10 stop | BTC | UP | 0.67 | 0.83 | 1.34 |
| 11-22 12:40 | +10 stop | SOL | UP | 0.59 | 0.75 | 1.29 |
| 11-22 12:40 | +10 | SOL | UP | 0.59 | 0.75 | 1.29 |
| 11-22 12:40 | +5 | ETH | UP | 0.56 | 0.79 | 2.00 |
| 11-22 12:40 | +10 stop | NEAR | UP | 0.65 | 0.81 | 1.33 |
| 11-22 12:38 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-22 12:38 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-22 12:38 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-22 12:38 | +10 stop | BTC | DOWN | 0.65 | 0.37 | -3.13 |
| 11-22 12:38 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-22 12:38 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 11-22 12:38 | +10 stop | BNB | UP | 0.57 | 0.70 | 0.97 |
| 11-22 12:38 | +20 | BNB | UP | 0.57 | 0.82 | 2.21 |
| 11-22 12:38 | +15 | BNB | UP | 0.57 | 0.82 | 2.21 |
| 11-22 12:38 | +10 | BNB | UP | 0.57 | 0.70 | 0.97 |
| 11-22 12:38 | +5 | BNB | UP | 0.57 | 0.70 | 0.97 |
| 11-22 12:38 | +10 stop | HYPE | UP | 0.64 | 0.82 | 1.52 |
| 11-22 12:38 | +20 | HYPE | UP | 0.63 | 0.89 | 2.36 |
| 11-22 12:38 | +15 | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 11-22 12:38 | +10 | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 11-22 12:38 | +5 | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 11-22 12:38 | +10 stop | DOGE | DOWN | 0.68 | 0.47 | -2.43 |
| 11-22 12:37 | +10 stop | ETH | UP | 0.53 | 0.79 | 2.30 |
| 11-22 12:37 | +20 | ETH | UP | 0.54 | 0.79 | 2.20 |
| 11-22 12:37 | +15 | ETH | UP | 0.54 | 0.79 | 2.20 |
| 11-22 12:37 | +10 | ETH | UP | 0.54 | 0.79 | 2.20 |
| 11-22 12:37 | +5 | ETH | UP | 0.53 | 0.59 | 0.25 |
| 11-22 12:37 | +10 stop | SOL | UP | 0.47 | 0.61 | 1.05 |
| 11-22 12:37 | +10 | SOL | UP | 0.49 | 0.61 | 0.85 |
| 11-22 12:37 | +5 | SOL | UP | 0.50 | 0.56 | 0.24 |
| 11-22 12:37 | +5 | BTC | UP | 0.51 | 0.56 | 0.14 |
| 11-22 12:37 | +5 | XRP | UP | 0.53 | 0.75 | 1.88 |
| 11-22 12:36 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-22 12:36 | +10 stop | DOGE | UP | 0.69 | 0.50 | -2.23 |
| 11-22 12:36 | +10 | DOGE | UP | 0.69 | 0.83 | 1.15 |
| 11-22 12:36 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 11-22 12:36 | +10 stop | BTC | UP | 0.62 | 0.46 | -1.95 |
