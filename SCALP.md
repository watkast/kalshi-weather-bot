# Range-Scalp Bot

*Updated Sat Oct 24 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31273 | 27253 | 4020 (40) | 4 | $-9037.09 | -4.6% |
| **+10¢** | 23403 | 18759 | 4644 (58) | 4 | $-8030.36 | -5.5% |
| **+15¢** | 19583 | 14590 | 4993 (81) | 3 | $-7189.77 | -5.8% |
| **+20¢** | 17348 | 12119 | 5229 (103) | 3 | $-6418.00 | -5.9% |
| **+10¢ (15¢ stop)** | 38376 | 38317 | 59 (32) | 1 | $-14600.99 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 02:14 | +10 stop | SOL | UP | 0.65 | 0.80 | 1.19 |
| 10-24 02:12 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-24 02:12 | +10 stop | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 10-24 02:11 | +10 stop | BTC | DOWN | 0.65 | open |  |
| 10-24 02:11 | +10 stop | SOL | UP | 0.57 | 0.70 | 0.97 |
| 10-24 02:08 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-24 02:08 | +20 | HYPE | UP | 0.67 | 0.91 | 2.12 |
| 10-24 02:08 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-24 02:08 | +10 stop | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-24 02:08 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-24 02:08 | +10 stop | SOL | DOWN | 0.56 | 0.29 | -3.04 |
| 10-24 02:08 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-24 02:08 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-24 02:07 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.95 |
| 10-24 02:07 | +15 | NEAR | DOWN | 0.63 | 0.80 | 1.41 |
| 10-24 02:07 | +10 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-24 02:07 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-24 02:07 | +15 | BNB | UP | 0.68 | 0.87 | 1.66 |
| 10-24 02:07 | +5 | BNB | UP | 0.68 | 0.87 | 1.66 |
| 10-24 02:07 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-24 02:07 | +20 | ETH | UP | 0.58 | 0.78 | 1.69 |
| 10-24 02:07 | +15 | ETH | UP | 0.57 | 0.78 | 1.79 |
| 10-24 02:07 | +10 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-24 02:07 | +5 | ETH | UP | 0.58 | 0.63 | 0.15 |
| 10-24 02:06 | +10 stop | BTC | DOWN | 0.65 | 0.41 | -2.73 |
| 10-24 02:06 | +5 | ZEC | UP | 0.58 | 0.70 | 0.88 |
| 10-24 02:06 | +15 | ZEC | UP | 0.56 | 0.82 | 2.31 |
| 10-24 02:06 | +10 stop | BTC | UP | 0.39 | 0.54 | 1.15 |
| 10-24 02:06 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-24 02:06 | +15 | DOGE | UP | 0.57 | 0.77 | 1.69 |
| 10-24 02:06 | +10 | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-24 02:06 | +10 stop | ZEC | UP | 0.56 | 0.70 | 1.07 |
| 10-24 02:06 | +10 stop | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-24 02:06 | +10 | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-24 02:06 | +5 | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-24 02:05 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-24 02:05 | +10 | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-24 02:05 | +5 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-24 02:05 | +10 stop | ETH | UP | 0.56 | 0.68 | 0.86 |
| 10-24 02:05 | +10 | ETH | UP | 0.56 | 0.68 | 0.86 |
