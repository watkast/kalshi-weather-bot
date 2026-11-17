# Range-Scalp Bot

*Updated Tue Nov 17 16:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63035 | 54984 | 8051 (117) | 1 | $-17168.57 | -4.3% |
| **+10¢** | 47084 | 37667 | 9417 (159) | 1 | $-16016.96 | -5.4% |
| **+15¢** | 39468 | 29314 | 10154 (201) | 1 | $-14526.91 | -5.9% |
| **+20¢** | 35168 | 24520 | 10648 (256) | 1 | $-12699.36 | -5.8% |
| **+10¢ (15¢ stop)** | 76708 | 76552 | 156 (92) | 0 | $-28262.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 16:54 | +10 stop | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-17 16:54 | +20 | ZEC | DOWN | 0.64 | 0.92 | 2.54 |
| 11-17 16:54 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-17 16:54 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 16:54 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 16:50 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-17 16:50 | +10 | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-17 16:50 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-17 16:50 | +10 stop | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-17 16:50 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-17 16:50 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-17 16:50 | +5 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-17 16:49 | +5 | ZEC | DOWN | 0.61 | 0.69 | 0.48 |
| 11-17 16:49 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 16:49 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 16:49 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 11-17 16:49 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-17 16:48 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 11-17 16:48 | +20 | XRP | DOWN | 0.57 | 0.80 | 2.00 |
| 11-17 16:48 | +15 | XRP | DOWN | 0.57 | 0.80 | 2.00 |
| 11-17 16:48 | +10 | XRP | DOWN | 0.56 | 0.71 | 1.17 |
| 11-17 16:48 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 11-17 16:48 | +10 stop | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-17 16:48 | +20 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-17 16:48 | +15 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-17 16:48 | +10 | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-17 16:48 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-17 16:47 | +10 stop | ZEC | UP | 0.53 | 0.36 | -2.05 |
| 11-17 16:47 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.94 |
| 11-17 16:47 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 11-17 16:47 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
| 11-17 16:47 | +10 stop | ETH | UP | 0.55 | 0.31 | -2.71 |
| 11-17 16:47 | +10 stop | BTC | UP | 0.53 | 0.37 | -1.95 |
| 11-17 16:47 | +10 stop | BNB | UP | 0.54 | 0.31 | -2.61 |
| 11-17 16:47 | +20 | BNB | UP | 0.52 | open |  |
| 11-17 16:47 | +15 | BNB | UP | 0.51 | open |  |
| 11-17 16:47 | +10 | BNB | UP | 0.51 | open |  |
| 11-17 16:47 | +5 | BNB | UP | 0.51 | open |  |
| 11-17 16:46 | +10 stop | XRP | DOWN | 0.47 | 0.68 | 1.76 |
| 11-17 16:46 | +20 | XRP | DOWN | 0.48 | 0.68 | 1.66 |
