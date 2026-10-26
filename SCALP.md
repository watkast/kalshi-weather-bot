# Range-Scalp Bot

*Updated Mon Oct 26 02:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34151 | 29818 | 4333 (43) | 0 | $-9431.54 | -4.4% |
| **+10¢** | 25561 | 20546 | 5015 (65) | 0 | $-8298.35 | -5.2% |
| **+15¢** | 21369 | 15969 | 5400 (89) | 0 | $-7440.35 | -5.5% |
| **+20¢** | 18939 | 13284 | 5655 (111) | 0 | $-6524.68 | -5.5% |
| **+10¢ (15¢ stop)** | 41817 | 41755 | 62 (33) | 0 | $-15918.86 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 02:40 | +10 stop | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-26 02:40 | +10 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-26 02:40 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 10-26 02:37 | +10 stop | BTC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-26 02:37 | +10 | BTC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-26 02:37 | +5 | BTC | DOWN | 0.46 | 0.54 | 0.44 |
| 10-26 02:36 | +10 stop | BTC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-26 02:36 | +10 | BTC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-26 02:36 | +5 | BTC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-26 02:36 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-26 02:36 | +15 | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-26 02:36 | +10 | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-26 02:36 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-26 02:35 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-26 02:33 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 02:33 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 02:33 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-26 02:33 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 02:33 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-26 02:32 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-26 02:32 | +20 | BTC | DOWN | 0.65 | 0.96 | 2.91 |
| 10-26 02:32 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-26 02:32 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-26 02:32 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-26 02:32 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 02:32 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-26 02:32 | +15 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 10-26 02:32 | +10 | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 02:32 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 02:32 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-26 02:32 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-26 02:32 | +15 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-26 02:32 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.75 |
| 10-26 02:32 | +5 | BNB | DOWN | 0.64 | 0.75 | 0.75 |
| 10-26 02:32 | +10 stop | DOGE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-26 02:32 | +20 | DOGE | DOWN | 0.61 | 0.90 | 2.70 |
| 10-26 02:32 | +15 | DOGE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-26 02:32 | +10 | DOGE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-26 02:32 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-26 02:32 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
