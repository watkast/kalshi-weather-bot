# Range-Scalp Bot

*Updated Thu Oct 15 01:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16889 | 14654 | 2235 (28) | 1 | $-5197.88 | -4.9% |
| **+10¢** | 12777 | 10185 | 2592 (40) | 0 | $-4731.87 | -5.9% |
| **+15¢** | 10735 | 7947 | 2788 (59) | 0 | $-4256.12 | -6.3% |
| **+20¢** | 9538 | 6616 | 2922 (76) | 0 | $-3763.11 | -6.3% |
| **+10¢ (15¢ stop)** | 20801 | 20751 | 50 (29) | 0 | $-8040.60 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 01:55 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-15 01:55 | +10 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-15 01:55 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-15 01:55 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-15 01:55 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-15 01:52 | +20 | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-15 01:51 | +5 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 01:51 | +5 | BNB | UP | 0.61 | open |  |
| 10-15 01:51 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.05 |
| 10-15 01:51 | +15 | DOGE | DOWN | 0.68 | 0.87 | 1.68 |
| 10-15 01:51 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.05 |
| 10-15 01:51 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.22 |
| 10-15 01:51 | +5 | BNB | UP | 0.53 | 0.58 | 0.14 |
| 10-15 01:51 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-15 01:51 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-15 01:51 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-15 01:51 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-15 01:51 | +5 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-15 01:51 | +10 stop | NEAR | DOWN | 0.70 | 0.49 | -2.43 |
| 10-15 01:51 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-15 01:51 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-15 01:51 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.74 |
| 10-15 01:51 | +10 stop | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 01:51 | +15 | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 01:51 | +10 | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 01:51 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 10-15 01:50 | +10 stop | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-15 01:50 | +15 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-15 01:50 | +10 | BTC | DOWN | 0.58 | 0.72 | 1.07 |
| 10-15 01:50 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-15 01:50 | +10 stop | SOL | DOWN | 0.53 | 0.64 | 0.79 |
| 10-15 01:50 | +20 | SOL | DOWN | 0.52 | 0.72 | 1.71 |
| 10-15 01:50 | +15 | SOL | DOWN | 0.53 | 0.72 | 1.57 |
| 10-15 01:50 | +10 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 01:50 | +5 | SOL | DOWN | 0.49 | 0.54 | 0.14 |
| 10-15 01:50 | +10 stop | BNB | DOWN | 0.51 | 0.71 | 1.67 |
| 10-15 01:50 | +10 | BNB | DOWN | 0.51 | 0.71 | 1.67 |
| 10-15 01:50 | +5 | BNB | DOWN | 0.50 | 0.56 | 0.24 |
| 10-15 01:50 | +10 stop | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-15 01:50 | +10 | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
