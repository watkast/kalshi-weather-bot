# Range-Scalp Bot

*Updated Wed Oct 07 11:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6328 | 5496 | 832 (9) | 0 | $-1889.50 | -4.7% |
| **+10¢** | 4814 | 3839 | 975 (16) | 0 | $-1741.01 | -5.7% |
| **+15¢** | 4050 | 3020 | 1030 (20) | 0 | $-1443.02 | -5.7% |
| **+20¢** | 3622 | 2545 | 1077 (27) | 1 | $-1158.65 | -5.1% |
| **+10¢ (15¢ stop)** | 7676 | 7661 | 15 (9) | 0 | $-2692.00 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 11:26 | +10 stop | NEAR | DOWN | 0.41 | 0.58 | 1.35 |
| 10-07 11:26 | +20 | NEAR | DOWN | 0.41 | open |  |
| 10-07 11:26 | +15 | NEAR | DOWN | 0.41 | 0.58 | 1.35 |
| 10-07 11:26 | +10 | NEAR | DOWN | 0.41 | 0.58 | 1.35 |
| 10-07 11:26 | +5 | NEAR | DOWN | 0.41 | 0.58 | 1.35 |
| 10-07 11:19 | +10 stop | NEAR | DOWN | 0.52 | 0.68 | 1.27 |
| 10-07 11:19 | +5 | NEAR | DOWN | 0.52 | 0.68 | 1.27 |
| 10-07 11:17 | +10 stop | NEAR | UP | 0.53 | 0.30 | -2.63 |
| 10-07 11:17 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-07 11:17 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-07 11:17 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-07 11:17 | +5 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 11:17 | +10 stop | DOGE | DOWN | 0.63 | 0.77 | 1.11 |
| 10-07 11:17 | +20 | DOGE | DOWN | 0.63 | 0.86 | 2.05 |
| 10-07 11:17 | +15 | DOGE | DOWN | 0.63 | 0.86 | 2.05 |
| 10-07 11:17 | +10 | DOGE | DOWN | 0.63 | 0.77 | 1.13 |
| 10-07 11:17 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.61 |
| 10-07 11:16 | +5 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-07 11:16 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-07 11:16 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-07 11:16 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 10-07 11:16 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-07 11:16 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-07 11:16 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.89 |
| 10-07 11:16 | +20 | NEAR | DOWN | 0.60 | 0.86 | 2.30 |
| 10-07 11:16 | +15 | NEAR | DOWN | 0.60 | 0.86 | 2.30 |
| 10-07 11:16 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.05 |
| 10-07 11:16 | +5 | NEAR | DOWN | 0.60 | 0.69 | 0.54 |
| 10-07 11:16 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 11:16 | +20 | ZEC | DOWN | 0.69 | 0.90 | 1.88 |
| 10-07 11:16 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 10-07 11:16 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 11:16 | +5 | ZEC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-07 11:16 | +10 stop | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-07 11:16 | +20 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-07 11:16 | +15 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 10-07 11:16 | +10 | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-07 11:16 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 10-07 11:16 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 10-07 11:16 | +20 | SOL | DOWN | 0.60 | 0.80 | 1.71 |
