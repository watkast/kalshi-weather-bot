# Range-Scalp Bot

*Updated Wed Nov 18 02:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63491 | 55370 | 8121 (118) | 1 | $-17381.07 | -4.3% |
| **+10¢** | 47426 | 37921 | 9505 (159) | 2 | $-16311.83 | -5.5% |
| **+15¢** | 39764 | 29515 | 10249 (203) | 2 | $-14804.34 | -5.9% |
| **+20¢** | 35420 | 24664 | 10756 (258) | 4 | $-13078.16 | -5.9% |
| **+10¢ (15¢ stop)** | 77266 | 77108 | 158 (93) | 2 | $-28441.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 02:36 | +5 | ZEC | DOWN | 0.68 | open |  |
| 11-18 02:35 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-18 02:35 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-18 02:35 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-18 02:35 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-18 02:35 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-18 02:35 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 11-18 02:35 | +20 | ZEC | DOWN | 0.57 | open |  |
| 11-18 02:35 | +15 | ZEC | DOWN | 0.57 | open |  |
| 11-18 02:35 | +10 | ZEC | DOWN | 0.57 | open |  |
| 11-18 02:35 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.46 |
| 11-18 02:31 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.82 |
| 11-18 02:31 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-18 02:31 | +15 | BNB | DOWN | 0.71 | 0.90 | 1.68 |
| 11-18 02:31 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 02:31 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-18 02:31 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-18 02:31 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.78 |
| 11-18 02:31 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.46 |
| 11-18 02:31 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.80 |
| 11-18 02:31 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 11-18 02:31 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 02:31 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-18 02:31 | +15 | SOL | DOWN | 0.71 | 0.88 | 1.47 |
| 11-18 02:31 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-18 02:30 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-18 02:30 | +20 | XRP | DOWN | 0.59 | 0.82 | 2.02 |
| 11-18 02:30 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 11-18 02:30 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-18 02:30 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 11-18 02:27 | +5 | BNB | DOWN | 0.27 | 0.54 | 2.38 |
| 11-18 02:26 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 11-18 02:26 | +10 stop | ZEC | UP | 0.70 | 0.47 | -2.63 |
| 11-18 02:25 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-18 02:25 | +20 | XRP | DOWN | 0.55 | 0.78 | 1.99 |
| 11-18 02:25 | +15 | XRP | DOWN | 0.55 | 0.72 | 1.37 |
| 11-18 02:25 | +10 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-18 02:25 | +5 | XRP | DOWN | 0.56 | 0.66 | 0.71 |
| 11-18 02:25 | +5 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 11-18 02:25 | +10 stop | ETH | UP | 0.61 | 0.97 | 3.37 |
