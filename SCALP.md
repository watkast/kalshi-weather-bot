# Range-Scalp Bot

*Updated Fri Oct 23 12:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30355 | 26443 | 3912 (39) | 1 | $-8832.69 | -4.6% |
| **+10¢** | 22740 | 18213 | 4527 (56) | 1 | $-7897.52 | -5.5% |
| **+15¢** | 19031 | 14162 | 4869 (79) | 2 | $-7134.16 | -6.0% |
| **+20¢** | 16850 | 11748 | 5102 (102) | 2 | $-6422.63 | -6.1% |
| **+10¢ (15¢ stop)** | 37212 | 37153 | 59 (32) | 0 | $-14053.20 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 12:57 | +10 stop | BTC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-23 12:57 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-23 12:55 | +10 stop | NEAR | DOWN | 0.60 | 0.38 | -2.54 |
| 10-23 12:53 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-23 12:52 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 12:51 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 10-23 12:50 | +10 stop | HYPE | DOWN | 0.66 | 0.85 | 1.61 |
| 10-23 12:50 | +10 | HYPE | DOWN | 0.66 | 0.85 | 1.61 |
| 10-23 12:50 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.25 |
| 10-23 12:50 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-23 12:50 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 10-23 12:50 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 12:50 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
| 10-23 12:49 | +10 stop | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 12:49 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-23 12:49 | +10 | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 12:49 | +10 stop | NEAR | DOWN | 0.63 | 0.43 | -2.35 |
| 10-23 12:49 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 12:49 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-23 12:49 | +15 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-23 12:49 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 12:49 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 10-23 12:49 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-23 12:49 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-23 12:49 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 12:49 | +10 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 12:49 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.20 |
| 10-23 12:48 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 10-23 12:48 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-23 12:48 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-23 12:48 | +10 | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-23 12:48 | +5 | XRP | DOWN | 0.57 | 0.63 | 0.25 |
| 10-23 12:48 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-23 12:48 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 10-23 12:48 | +5 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 12:48 | +10 stop | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 10-23 12:48 | +20 | XRP | DOWN | 0.53 | 0.77 | 2.09 |
| 10-23 12:48 | +15 | XRP | DOWN | 0.53 | 0.71 | 1.47 |
| 10-23 12:48 | +10 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 10-23 12:48 | +5 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
