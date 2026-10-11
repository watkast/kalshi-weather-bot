# Range-Scalp Bot

*Updated Sun Oct 11 20:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12468 | 10764 | 1704 (25) | 2 | $-4103.05 | -5.2% |
| **+10¢** | 9465 | 7491 | 1974 (37) | 2 | $-3851.55 | -6.5% |
| **+15¢** | 7969 | 5870 | 2099 (55) | 2 | $-3296.30 | -6.6% |
| **+20¢** | 7102 | 4915 | 2187 (69) | 2 | $-2785.31 | -6.2% |
| **+10¢ (15¢ stop)** | 15356 | 15315 | 41 (25) | 0 | $-6029.98 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 20:23 | +10 stop | DOGE | DOWN | 0.69 | 0.91 | 1.93 |
| 10-11 20:23 | +10 | DOGE | DOWN | 0.70 | 0.91 | 1.83 |
| 10-11 20:23 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.64 |
| 10-11 20:22 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-11 20:20 | +10 stop | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-11 20:20 | +10 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-11 20:20 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 20:20 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-11 20:20 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 10-11 20:20 | +15 | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-11 20:20 | +10 | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-11 20:20 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.58 |
| 10-11 20:20 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-11 20:20 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-11 20:20 | +10 stop | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 20:20 | +20 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 20:20 | +15 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 20:20 | +10 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 20:20 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.25 |
| 10-11 20:19 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-11 20:19 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-11 20:19 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-11 20:19 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 10-11 20:19 | +20 | DOGE | DOWN | 0.65 | 0.91 | 2.32 |
| 10-11 20:19 | +15 | DOGE | DOWN | 0.65 | 0.91 | 2.32 |
| 10-11 20:19 | +10 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 20:19 | +5 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 20:19 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-11 20:19 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-11 20:19 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-11 20:19 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-11 20:18 | +10 stop | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-11 20:18 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.78 |
| 10-11 20:18 | +15 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-11 20:18 | +10 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-11 20:18 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-11 20:18 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-11 20:18 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 10-11 20:17 | +10 stop | ETH | DOWN | 0.63 | 0.44 | -2.25 |
| 10-11 20:17 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
