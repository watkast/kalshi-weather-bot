# Range-Scalp Bot

*Updated Tue Nov 10 15:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54687 | 47702 | 6985 (91) | 0 | $-14895.02 | -4.3% |
| **+10¢** | 40860 | 32708 | 8152 (121) | 0 | $-13832.91 | -5.4% |
| **+15¢** | 34255 | 25469 | 8786 (155) | 0 | $-12571.96 | -5.9% |
| **+20¢** | 30501 | 21283 | 9218 (204) | 0 | $-10985.72 | -5.7% |
| **+10¢ (15¢ stop)** | 66617 | 66503 | 114 (70) | 0 | $-24613.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 15:33 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-10 15:32 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 15:32 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-10 15:32 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-10 15:32 | +10 | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 15:32 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-10 15:32 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 11-10 15:32 | +20 | ETH | DOWN | 0.70 | 0.95 | 2.30 |
| 11-10 15:32 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 15:32 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 11-10 15:32 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-10 15:32 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 15:32 | +20 | NEAR | DOWN | 0.64 | 0.87 | 2.05 |
| 11-10 15:32 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 11-10 15:32 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-10 15:32 | +5 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-10 15:32 | +10 stop | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-10 15:32 | +20 | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-10 15:32 | +15 | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-10 15:32 | +10 | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-10 15:32 | +5 | SOL | DOWN | 0.53 | 0.60 | 0.35 |
| 11-10 15:31 | +10 stop | HYPE | DOWN | 0.71 | 0.52 | -2.23 |
| 11-10 15:31 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.83 |
| 11-10 15:31 | +15 | HYPE | DOWN | 0.71 | 0.90 | 1.70 |
| 11-10 15:31 | +10 | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 15:31 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 15:31 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 11-10 15:31 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 11-10 15:31 | +15 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-10 15:31 | +10 | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 11-10 15:31 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 11-10 15:30 | +10 stop | DOGE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-10 15:30 | +20 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-10 15:30 | +15 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 11-10 15:30 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-10 15:30 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-10 15:25 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-10 15:25 | +10 stop | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 11-10 15:25 | +20 | BTC | DOWN | 0.56 | 0.77 | 1.79 |
| 11-10 15:25 | +15 | BTC | DOWN | 0.56 | 0.77 | 1.79 |
