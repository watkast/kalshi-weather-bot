# Range-Scalp Bot

*Updated Thu Oct 08 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7830 | 6784 | 1046 (13) | 0 | $-2442.52 | -4.9% |
| **+10¢** | 5937 | 4697 | 1240 (24) | 0 | $-2425.48 | -6.5% |
| **+15¢** | 4992 | 3691 | 1301 (32) | 0 | $-1965.84 | -6.3% |
| **+20¢** | 4462 | 3112 | 1350 (40) | 0 | $-1549.86 | -5.5% |
| **+10¢ (15¢ stop)** | 9517 | 9488 | 29 (18) | 0 | $-3488.05 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 18:18 | +5 | NEAR | UP | 0.50 | 0.57 | 0.34 |
| 10-08 18:18 | +10 stop | ZEC | UP | 0.71 | 0.85 | 1.18 |
| 10-08 18:18 | +20 | ZEC | UP | 0.70 | 0.90 | 1.78 |
| 10-08 18:18 | +15 | ZEC | UP | 0.70 | 0.85 | 1.26 |
| 10-08 18:18 | +10 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 10-08 18:18 | +5 | ZEC | UP | 0.71 | 0.77 | 0.32 |
| 10-08 18:16 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.17 |
| 10-08 18:16 | +20 | NEAR | UP | 0.69 | 0.92 | 2.07 |
| 10-08 18:16 | +15 | NEAR | UP | 0.69 | 0.85 | 1.32 |
| 10-08 18:16 | +10 | NEAR | UP | 0.69 | 0.85 | 1.32 |
| 10-08 18:16 | +5 | NEAR | UP | 0.69 | 0.76 | 0.38 |
| 10-08 18:14 | +10 stop | BNB | DOWN | 0.28 | 0.60 | 2.88 |
| 10-08 18:14 | +5 | BNB | DOWN | 0.27 | 0.60 | 2.99 |
| 10-08 18:13 | +10 stop | BNB | UP | 0.26 | 0.62 | 3.29 |
| 10-08 18:13 | +5 | BNB | UP | 0.26 | 0.62 | 3.29 |
| 10-08 18:12 | +10 stop | BNB | DOWN | 0.49 | 0.59 | 0.65 |
| 10-08 18:11 | +5 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-08 18:11 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-08 18:11 | +20 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 10-08 18:11 | +15 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 10-08 18:11 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-08 18:11 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 10-08 18:10 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-08 18:09 | +10 stop | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 10-08 18:09 | +10 | SOL | DOWN | 0.62 | 0.77 | 1.22 |
| 10-08 18:09 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.24 |
| 10-08 18:08 | +10 stop | SOL | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 18:08 | +15 | SOL | DOWN | 0.52 | 0.77 | 2.19 |
| 10-08 18:08 | +10 | SOL | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 18:07 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 10-08 18:06 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-08 18:06 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-08 18:06 | +10 stop | ZEC | DOWN | 0.70 | 0.48 | -2.51 |
| 10-08 18:06 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.23 |
| 10-08 18:05 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-08 18:05 | +20 | SOL | DOWN | 0.54 | 0.77 | 1.99 |
| 10-08 18:05 | +15 | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 10-08 18:05 | +10 | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-08 18:05 | +5 | SOL | DOWN | 0.54 | 0.60 | 0.25 |
| 10-08 18:05 | +15 | DOGE | UP | 0.71 | 0.89 | 1.58 |
