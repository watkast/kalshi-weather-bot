# Range-Scalp Bot

*Updated Mon Oct 26 07:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34503 | 30117 | 4386 (43) | 1 | $-9595.92 | -4.4% |
| **+10¢** | 25823 | 20752 | 5071 (65) | 4 | $-8419.51 | -5.2% |
| **+15¢** | 21597 | 16138 | 5459 (89) | 4 | $-7543.55 | -5.6% |
| **+20¢** | 19139 | 13415 | 5724 (112) | 6 | $-6677.31 | -5.6% |
| **+10¢ (15¢ stop)** | 42273 | 42211 | 62 (33) | 0 | $-16109.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 07:55 | +10 stop | NEAR | DOWN | 0.65 | 0.41 | -2.73 |
| 10-26 07:52 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.26 |
| 10-26 07:52 | +10 stop | NEAR | DOWN | 0.49 | 0.61 | 0.85 |
| 10-26 07:51 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-26 07:51 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-26 07:51 | +5 | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 10-26 07:51 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-26 07:51 | +5 | SOL | UP | 0.45 | 0.55 | 0.64 |
| 10-26 07:50 | +10 stop | NEAR | UP | 0.59 | 0.39 | -2.34 |
| 10-26 07:50 | +5 | XRP | DOWN | 0.57 | 0.66 | 0.56 |
| 10-26 07:50 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-26 07:50 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-26 07:50 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 10-26 07:50 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-26 07:50 | +10 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-26 07:50 | +5 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-26 07:49 | +10 stop | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 10-26 07:49 | +10 stop | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-26 07:49 | +10 stop | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-26 07:49 | +10 stop | NEAR | DOWN | 0.52 | 0.35 | -2.04 |
| 10-26 07:49 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 07:49 | +20 | ETH | DOWN | 0.63 | 0.87 | 2.15 |
| 10-26 07:49 | +15 | ETH | DOWN | 0.63 | 0.87 | 2.15 |
| 10-26 07:49 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 07:49 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 07:49 | +10 stop | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-26 07:49 | +20 | BNB | DOWN | 0.67 | 0.89 | 1.97 |
| 10-26 07:49 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.65 |
| 10-26 07:49 | +10 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-26 07:49 | +5 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-26 07:49 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-26 07:48 | +10 stop | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-26 07:48 | +15 | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 10-26 07:48 | +10 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-26 07:48 | +5 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-26 07:48 | +5 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 10-26 07:48 | +10 stop | NEAR | UP | 0.64 | 0.40 | -2.74 |
| 10-26 07:48 | +10 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 10-26 07:48 | +5 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 10-26 07:48 | +5 | SOL | UP | 0.48 | 0.55 | 0.34 |
