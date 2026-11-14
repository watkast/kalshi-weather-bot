# Range-Scalp Bot

*Updated Sat Nov 14 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58866 | 51367 | 7499 (106) | 0 | $-15863.59 | -4.3% |
| **+10¢** | 43981 | 35210 | 8771 (139) | 0 | $-14838.84 | -5.4% |
| **+15¢** | 36855 | 27404 | 9451 (174) | 0 | $-13436.04 | -5.8% |
| **+20¢** | 32832 | 22910 | 9922 (226) | 0 | $-11813.01 | -5.7% |
| **+10¢ (15¢ stop)** | 71666 | 71528 | 138 (82) | 0 | $-26345.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 01:54 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.18 |
| 11-14 01:52 | +10 stop | ZEC | DOWN | 0.51 | 0.68 | 1.36 |
| 11-14 01:52 | +15 | ZEC | DOWN | 0.51 | 0.68 | 1.36 |
| 11-14 01:52 | +10 | ZEC | DOWN | 0.51 | 0.68 | 1.36 |
| 11-14 01:52 | +5 | ZEC | DOWN | 0.51 | 0.58 | 0.34 |
| 11-14 01:50 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-14 01:50 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 01:50 | +5 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 01:50 | +5 | SOL | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 01:49 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 11-14 01:49 | +20 | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 11-14 01:49 | +15 | BNB | DOWN | 0.56 | 0.73 | 1.36 |
| 11-14 01:49 | +10 | BNB | DOWN | 0.56 | 0.70 | 1.05 |
| 11-14 01:49 | +5 | BNB | DOWN | 0.56 | 0.64 | 0.43 |
| 11-14 01:49 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:49 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:49 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-14 01:49 | +10 stop | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-14 01:47 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 01:47 | +20 | SOL | DOWN | 0.71 | 0.93 | 2.00 |
| 11-14 01:47 | +15 | SOL | DOWN | 0.71 | 0.88 | 1.47 |
| 11-14 01:47 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 01:47 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 01:47 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-14 01:47 | +20 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 11-14 01:47 | +15 | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 11-14 01:47 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-14 01:47 | +5 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-14 01:46 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:46 | +20 | NEAR | DOWN | 0.70 | 0.92 | 1.94 |
| 11-14 01:46 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 01:46 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:46 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:46 | +10 stop | BTC | DOWN | 0.67 | 0.47 | -2.34 |
| 11-14 01:46 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 11-14 01:46 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 01:46 | +10 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 01:46 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-14 01:46 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 01:46 | +20 | XRP | DOWN | 0.70 | 0.93 | 2.09 |
