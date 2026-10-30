# Range-Scalp Bot

*Updated Fri Oct 30 01:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40000 | 34940 | 5060 (51) | 0 | $-10957.02 | -4.3% |
| **+10¢** | 29812 | 23959 | 5853 (74) | 0 | $-9689.97 | -5.2% |
| **+15¢** | 24931 | 18635 | 6296 (101) | 0 | $-8670.23 | -5.5% |
| **+20¢** | 22123 | 15520 | 6603 (130) | 0 | $-7598.67 | -5.5% |
| **+10¢ (15¢ stop)** | 48813 | 48743 | 70 (37) | 0 | $-18441.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 01:16 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-30 01:16 | +20 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-30 01:16 | +15 | ZEC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-30 01:16 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-30 01:16 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-30 01:16 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-30 01:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-30 01:16 | +15 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-30 01:16 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-30 01:16 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-30 01:16 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 01:16 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 10-30 01:16 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-30 01:16 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 01:16 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 01:10 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 10-30 01:09 | +10 stop | DOGE | DOWN | 0.65 | 0.43 | -2.58 |
| 10-30 01:09 | +10 stop | NEAR | UP | 0.54 | 0.65 | 0.76 |
| 10-30 01:08 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 10-30 01:07 | +10 stop | BNB | UP | 0.61 | 0.75 | 1.09 |
| 10-30 01:07 | +15 | BNB | UP | 0.61 | 0.78 | 1.40 |
| 10-30 01:07 | +10 | BNB | UP | 0.62 | 0.75 | 0.95 |
| 10-30 01:07 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-30 01:07 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-30 01:05 | +10 stop | NEAR | DOWN | 0.52 | 0.34 | -2.14 |
| 10-30 01:05 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 01:05 | +10 stop | ZEC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 01:03 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:03 | +20 | BNB | DOWN | 0.59 | yes | -6.12 |
| 10-30 01:03 | +15 | BNB | DOWN | 0.60 | 0.78 | 1.51 |
| 10-30 01:03 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 01:03 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.58 |
| 10-30 01:02 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 01:02 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-30 01:02 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-30 01:02 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-30 01:02 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-30 01:02 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-30 01:02 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-30 01:02 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
