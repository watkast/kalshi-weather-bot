# Range-Scalp Bot

*Updated Thu Nov 19 19:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65383 | 57088 | 8295 (124) | 0 | $-17405.33 | -4.2% |
| **+10¢** | 48822 | 39113 | 9709 (165) | 0 | $-16229.89 | -5.3% |
| **+15¢** | 40941 | 30468 | 10473 (211) | 0 | $-14603.40 | -5.7% |
| **+20¢** | 36458 | 25454 | 11004 (266) | 0 | $-12919.14 | -5.6% |
| **+10¢ (15¢ stop)** | 79584 | 79420 | 164 (98) | 0 | $-29278.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 19:04 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-19 19:03 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 19:03 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 19:03 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.89 |
| 11-19 19:03 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-19 19:03 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 19:03 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 19:03 | +10 stop | NEAR | DOWN | 0.49 | 0.59 | 0.65 |
| 11-19 19:02 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 19:02 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-19 19:02 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-19 19:02 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 19:02 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-19 19:01 | +10 stop | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-19 19:01 | +20 | ZEC | DOWN | 0.70 | 0.94 | 2.15 |
| 11-19 19:01 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-19 19:01 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 19:01 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-19 19:00 | +10 stop | NEAR | DOWN | 0.70 | 0.47 | -2.63 |
| 11-19 19:00 | +20 | NEAR | DOWN | 0.70 | 0.93 | 2.06 |
| 11-19 19:00 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-19 19:00 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-19 19:00 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-19 19:00 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 19:00 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.80 |
| 11-19 19:00 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-19 19:00 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 19:00 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-19 18:54 | +10 stop | NEAR | DOWN | 0.70 | 0.89 | 1.65 |
| 11-19 18:54 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.14 |
| 11-19 18:54 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 11-19 18:54 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 18:54 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 18:49 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.18 |
| 11-19 18:47 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-19 18:47 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-19 18:47 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-19 18:47 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-19 18:47 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-19 18:47 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
