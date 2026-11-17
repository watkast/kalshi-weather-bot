# Range-Scalp Bot

*Updated Tue Nov 17 14:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62916 | 54879 | 8037 (117) | 0 | $-17142.77 | -4.3% |
| **+10¢** | 46989 | 37585 | 9404 (159) | 0 | $-16021.02 | -5.4% |
| **+15¢** | 39384 | 29242 | 10142 (201) | 0 | $-14558.70 | -5.9% |
| **+20¢** | 35097 | 24462 | 10635 (256) | 0 | $-12732.52 | -5.8% |
| **+10¢ (15¢ stop)** | 76564 | 76408 | 156 (92) | 0 | $-28231.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 14:51 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.34 |
| 11-17 14:51 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-17 14:51 | +5 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-17 14:51 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 11-17 14:51 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 11-17 14:51 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.22 |
| 11-17 14:51 | +10 stop | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 14:51 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-17 14:51 | +10 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 14:51 | +5 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 14:51 | +10 stop | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 11-17 14:51 | +15 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-17 14:51 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-17 14:51 | +5 | DOGE | DOWN | 0.59 | 0.75 | 1.24 |
| 11-17 14:48 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.56 |
| 11-17 14:48 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-17 14:48 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-17 14:47 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-17 14:47 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 14:47 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-17 14:47 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.22 |
| 11-17 14:47 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-17 14:47 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 11-17 14:47 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 14:47 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.56 |
| 11-17 14:46 | +10 stop | XRP | DOWN | 0.56 | 0.69 | 0.97 |
| 11-17 14:46 | +20 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 11-17 14:46 | +15 | XRP | DOWN | 0.55 | 0.75 | 1.68 |
| 11-17 14:46 | +10 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-17 14:46 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 11-17 14:46 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-17 14:46 | +20 | HYPE | DOWN | 0.57 | 0.77 | 1.69 |
| 11-17 14:46 | +15 | HYPE | DOWN | 0.57 | 0.73 | 1.28 |
| 11-17 14:46 | +10 | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-17 14:46 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-17 14:46 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-17 14:46 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-17 14:46 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 14:46 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-17 14:46 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
