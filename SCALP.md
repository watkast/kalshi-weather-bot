# Range-Scalp Bot

*Updated Wed Oct 07 02:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5796 | 5016 | 780 (9) | 0 | $-1832.99 | -5.0% |
| **+10¢** | 4417 | 3500 | 917 (16) | 0 | $-1747.53 | -6.3% |
| **+15¢** | 3705 | 2733 | 972 (20) | 0 | $-1538.67 | -6.6% |
| **+20¢** | 3309 | 2295 | 1014 (27) | 0 | $-1290.05 | -6.2% |
| **+10¢ (15¢ stop)** | 7051 | 7036 | 15 (9) | 0 | $-2519.26 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 01:51 | +5 | XRP | DOWN | 0.59 | 0.70 | 0.75 |
| 10-07 01:51 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-07 01:51 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-07 01:51 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-07 01:51 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-07 01:50 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-07 01:49 | +10 stop | ETH | UP | 0.52 | 0.37 | -1.85 |
| 10-07 01:49 | +10 | ETH | UP | 0.52 | no | -5.38 |
| 10-07 01:49 | +5 | ETH | UP | 0.52 | no | -5.38 |
| 10-07 01:49 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 10-07 01:48 | +10 stop | BTC | UP | 0.56 | 0.37 | -2.25 |
| 10-07 01:48 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-07 01:48 | +5 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 01:48 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-07 01:47 | +10 stop | NEAR | UP | 0.59 | 0.72 | 0.98 |
| 10-07 01:47 | +10 stop | ETH | UP | 0.49 | 0.62 | 0.95 |
| 10-07 01:47 | +20 | ETH | UP | 0.49 | no | -5.08 |
| 10-07 01:47 | +15 | ETH | UP | 0.49 | no | -5.08 |
| 10-07 01:47 | +10 | ETH | UP | 0.49 | 0.62 | 0.95 |
| 10-07 01:47 | +5 | ETH | UP | 0.49 | 0.62 | 0.95 |
| 10-07 01:47 | +10 stop | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 10-07 01:47 | +20 | SOL | DOWN | 0.56 | 0.82 | 2.31 |
| 10-07 01:47 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-07 01:47 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 10-07 01:47 | +5 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 10-07 01:47 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-07 01:47 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.41 |
| 10-07 01:47 | +10 | ZEC | DOWN | 0.66 | 0.78 | 0.92 |
| 10-07 01:47 | +5 | ZEC | DOWN | 0.67 | 0.78 | 0.78 |
| 10-07 01:47 | +10 stop | XRP | DOWN | 0.55 | 0.39 | -1.96 |
| 10-07 01:47 | +20 | XRP | DOWN | 0.55 | 0.80 | 2.19 |
| 10-07 01:47 | +15 | XRP | DOWN | 0.55 | 0.71 | 1.26 |
| 10-07 01:47 | +10 | XRP | DOWN | 0.55 | 0.70 | 1.16 |
| 10-07 01:47 | +5 | XRP | DOWN | 0.55 | 0.61 | 0.24 |
| 10-07 01:47 | +10 stop | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-07 01:47 | +20 | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 10-07 01:47 | +15 | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-07 01:47 | +10 | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-07 01:47 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-07 01:47 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
