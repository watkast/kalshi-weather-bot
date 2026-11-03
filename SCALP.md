# Range-Scalp Bot

*Updated Tue Nov 03 01:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45439 | 39560 | 5879 (67) | 0 | $-13167.01 | -4.6% |
| **+10¢** | 33913 | 27102 | 6811 (89) | 0 | $-12049.72 | -5.7% |
| **+15¢** | 28367 | 21039 | 7328 (116) | 1 | $-11091.52 | -6.2% |
| **+20¢** | 25190 | 17516 | 7674 (151) | 4 | $-9857.58 | -6.2% |
| **+10¢ (15¢ stop)** | 55443 | 55356 | 87 (51) | 1 | $-20931.82 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 01:35 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-03 01:35 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.28 |
| 11-03 01:35 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 11-03 01:34 | +10 stop | BNB | UP | 0.52 | 0.35 | -1.99 |
| 11-03 01:34 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-03 01:34 | +5 | BNB | UP | 0.50 | 0.57 | 0.34 |
| 11-03 01:34 | +10 stop | HYPE | DOWN | 0.54 | 0.67 | 0.92 |
| 11-03 01:34 | +20 | HYPE | DOWN | 0.54 | 0.77 | 1.95 |
| 11-03 01:34 | +15 | HYPE | DOWN | 0.54 | 0.70 | 1.23 |
| 11-03 01:34 | +10 | HYPE | DOWN | 0.54 | 0.67 | 0.92 |
| 11-03 01:34 | +5 | HYPE | DOWN | 0.54 | 0.67 | 0.92 |
| 11-03 01:34 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-03 01:34 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-03 01:34 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-03 01:34 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-03 01:34 | +5 | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
| 11-03 01:34 | +10 stop | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-03 01:34 | +10 | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-03 01:34 | +5 | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-03 01:34 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-03 01:33 | +5 | BTC | DOWN | 0.51 | 0.69 | 1.47 |
| 11-03 01:33 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-03 01:32 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-03 01:32 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-03 01:31 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 01:31 | +20 | NEAR | DOWN | 0.67 | 0.90 | 2.08 |
| 11-03 01:31 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 11-03 01:31 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 01:31 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-03 01:31 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-03 01:31 | +20 | ZEC | DOWN | 0.61 | 0.85 | 2.14 |
| 11-03 01:31 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-03 01:31 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-03 01:31 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.27 |
| 11-03 01:31 | +10 stop | BNB | DOWN | 0.65 | 0.42 | -2.64 |
| 11-03 01:31 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-03 01:31 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-03 01:31 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-03 01:31 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 01:31 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
