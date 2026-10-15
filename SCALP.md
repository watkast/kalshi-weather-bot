# Range-Scalp Bot

*Updated Thu Oct 15 13:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17616 | 15303 | 2313 (28) | 0 | $-5302.48 | -4.8% |
| **+10¢** | 13312 | 10633 | 2679 (40) | 0 | $-4793.76 | -5.7% |
| **+15¢** | 11169 | 8289 | 2880 (59) | 0 | $-4271.95 | -6.1% |
| **+20¢** | 9926 | 6911 | 3015 (77) | 0 | $-3708.08 | -6.0% |
| **+10¢ (15¢ stop)** | 21665 | 21615 | 50 (29) | 0 | $-8342.22 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 13:49 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 10-15 13:49 | +20 | SOL | DOWN | 0.69 | 0.91 | 1.96 |
| 10-15 13:49 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.60 |
| 10-15 13:49 | +10 | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 10-15 13:49 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-15 13:48 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 13:48 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 10-15 13:46 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-15 13:46 | +10 stop | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 13:46 | +20 | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 13:46 | +15 | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 13:46 | +10 | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 13:46 | +5 | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 13:46 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-15 13:46 | +20 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 10-15 13:46 | +15 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 10-15 13:46 | +10 | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-15 13:46 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 10-15 13:46 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-15 13:46 | +20 | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-15 13:46 | +15 | SOL | DOWN | 0.59 | 0.77 | 1.50 |
| 10-15 13:46 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-15 13:46 | +5 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-15 13:46 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 13:46 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-15 13:46 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-15 13:46 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 13:46 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 13:46 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-15 13:46 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-15 13:46 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-15 13:46 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-15 13:46 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-15 13:46 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-15 13:46 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 13:46 | +15 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 13:46 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-15 13:46 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-15 13:46 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-15 13:46 | +20 | DOGE | DOWN | 0.69 | 0.91 | 2.01 |
