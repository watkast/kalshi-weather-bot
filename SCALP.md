# Range-Scalp Bot

*Updated Wed Nov 11 20:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56204 | 49018 | 7186 (94) | 1 | $-15341.11 | -4.3% |
| **+10¢** | 41995 | 33608 | 8387 (124) | 2 | $-14313.37 | -5.4% |
| **+15¢** | 35217 | 26178 | 9039 (158) | 0 | $-12998.44 | -5.9% |
| **+20¢** | 31369 | 21886 | 9483 (208) | 4 | $-11352.66 | -5.8% |
| **+10¢ (15¢ stop)** | 68481 | 68360 | 121 (73) | 1 | $-25242.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 20:48 | +10 stop | DOGE | UP | 0.66 | open |  |
| 11-11 20:48 | +10 | DOGE | UP | 0.66 | open |  |
| 11-11 20:48 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 11-11 20:47 | +10 stop | NEAR | DOWN | 0.64 | 0.41 | -2.68 |
| 11-11 20:47 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-11 20:47 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-11 20:47 | +10 stop | ZEC | UP | 0.63 | 0.78 | 1.20 |
| 11-11 20:47 | +10 | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 11-11 20:47 | +5 | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 11-11 20:46 | +10 stop | DOGE | UP | 0.59 | 0.71 | 0.88 |
| 11-11 20:46 | +20 | DOGE | UP | 0.57 | open |  |
| 11-11 20:46 | +15 | DOGE | UP | 0.57 | 0.72 | 1.17 |
| 11-11 20:46 | +10 | DOGE | UP | 0.57 | 0.71 | 1.07 |
| 11-11 20:46 | +5 | DOGE | UP | 0.57 | 0.65 | 0.46 |
| 11-11 20:46 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 11-11 20:46 | +20 | XRP | UP | 0.63 | open |  |
| 11-11 20:46 | +15 | XRP | UP | 0.63 | 0.79 | 1.31 |
| 11-11 20:46 | +10 | XRP | UP | 0.63 | 0.76 | 1.00 |
| 11-11 20:46 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 11-11 20:46 | +10 stop | BNB | UP | 0.62 | 0.41 | -2.44 |
| 11-11 20:46 | +20 | BNB | UP | 0.62 | 0.86 | 2.14 |
| 11-11 20:46 | +15 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-11 20:46 | +10 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-11 20:46 | +5 | BNB | UP | 0.62 | 0.71 | 0.58 |
| 11-11 20:46 | +10 stop | HYPE | UP | 0.56 | 0.69 | 0.97 |
| 11-11 20:46 | +20 | HYPE | UP | 0.56 | 0.80 | 2.10 |
| 11-11 20:46 | +15 | HYPE | UP | 0.56 | 0.80 | 2.10 |
| 11-11 20:46 | +10 | HYPE | UP | 0.56 | 0.69 | 0.95 |
| 11-11 20:46 | +5 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 11-11 20:46 | +10 stop | BTC | UP | 0.61 | 0.41 | -2.34 |
| 11-11 20:46 | +20 | BTC | UP | 0.61 | 0.91 | 2.73 |
| 11-11 20:46 | +15 | BTC | UP | 0.61 | 0.79 | 1.51 |
| 11-11 20:46 | +10 | BTC | UP | 0.61 | 0.79 | 1.51 |
| 11-11 20:46 | +5 | BTC | UP | 0.61 | 0.69 | 0.48 |
| 11-11 20:46 | +10 stop | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 11-11 20:46 | +20 | NEAR | UP | 0.54 | 0.77 | 1.99 |
| 11-11 20:46 | +15 | NEAR | UP | 0.54 | 0.73 | 1.56 |
| 11-11 20:46 | +10 | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 11-11 20:46 | +5 | NEAR | UP | 0.54 | 0.61 | 0.30 |
| 11-11 20:46 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
