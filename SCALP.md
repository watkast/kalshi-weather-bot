# Range-Scalp Bot

*Updated Thu Oct 22 12:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28685 | 24997 | 3688 (39) | 1 | $-8244.10 | -4.6% |
| **+10¢** | 21532 | 17264 | 4268 (55) | 1 | $-7339.11 | -5.4% |
| **+15¢** | 18026 | 13437 | 4589 (78) | 1 | $-6546.61 | -5.8% |
| **+20¢** | 15949 | 11136 | 4813 (100) | 1 | $-5896.57 | -5.9% |
| **+10¢ (15¢ stop)** | 35184 | 35125 | 59 (32) | 0 | $-13158.09 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 11:52 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-22 11:52 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-22 11:49 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-22 11:48 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.87 |
| 10-22 11:48 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-22 11:48 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 11:48 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-22 11:48 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-22 11:48 | +15 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 10-22 11:48 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 11:48 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-22 11:48 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-22 11:48 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 10-22 11:48 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 10-22 11:48 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-22 11:48 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-22 11:47 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:47 | +20 | DOGE | DOWN | 0.67 | 0.91 | 2.18 |
| 10-22 11:47 | +15 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-22 11:47 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:47 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-22 11:47 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-22 11:47 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-22 11:47 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-22 11:47 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 11:47 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +20 | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 10-22 11:47 | +15 | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-22 11:47 | +10 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +5 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-22 11:47 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-22 11:47 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 11:47 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-22 11:47 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-22 11:47 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 10-22 11:47 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
