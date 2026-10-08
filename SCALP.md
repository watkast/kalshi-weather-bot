# Range-Scalp Bot

*Updated Thu Oct 08 17:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7766 | 6727 | 1039 (13) | 0 | $-2437.17 | -5.0% |
| **+10¢** | 5892 | 4662 | 1230 (24) | 0 | $-2403.55 | -6.5% |
| **+15¢** | 4952 | 3661 | 1291 (32) | 0 | $-1954.67 | -6.3% |
| **+20¢** | 4429 | 3089 | 1340 (40) | 0 | $-1539.62 | -5.5% |
| **+10¢ (15¢ stop)** | 9438 | 9409 | 29 (18) | 0 | $-3461.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 17:20 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-08 17:18 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 17:18 | +10 stop | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-08 17:18 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-08 17:18 | +5 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-08 17:18 | +10 stop | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 10-08 17:18 | +10 | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 10-08 17:16 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-08 17:16 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 17:16 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.81 |
| 10-08 17:16 | +15 | BTC | DOWN | 0.71 | 0.91 | 1.81 |
| 10-08 17:16 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 17:16 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-08 17:16 | +10 stop | ZEC | DOWN | 0.70 | 0.50 | -2.36 |
| 10-08 17:16 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.89 |
| 10-08 17:16 | +15 | ZEC | DOWN | 0.70 | 0.89 | 1.65 |
| 10-08 17:16 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 17:16 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 17:16 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.32 |
| 10-08 17:16 | +10 | HYPE | DOWN | 0.70 | 0.84 | 1.11 |
| 10-08 17:16 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.28 |
| 10-08 17:16 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 17:16 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.81 |
| 10-08 17:16 | +15 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 10-08 17:16 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-08 17:16 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-08 17:16 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-08 17:16 | +20 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 10-08 17:16 | +15 | ETH | DOWN | 0.59 | 0.77 | 1.50 |
| 10-08 17:16 | +10 | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 10-08 17:16 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 10-08 17:16 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 17:16 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 17:16 | +15 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 17:16 | +10 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 17:16 | +5 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 17:16 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 17:16 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-08 17:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-08 17:16 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
