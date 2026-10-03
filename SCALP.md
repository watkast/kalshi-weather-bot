# Range-Scalp Bot

*Updated Sat Oct 03 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 100 | 86 | 14 (0) | 0 | $-37.56 | -5.9% |
| **+10¢** | 87 | 73 | 14 (0) | 0 | $-8.15 | -1.5% |
| **+15¢** | 68 | 53 | 15 (0) | 0 | $-14.50 | -3.4% |
| **+20¢** | 280 | 198 | 82 (1) | 0 | $-84.06 | -4.8% |
| **+10¢ (15¢ stop)** | 139 | 139 | 0 (0) | 0 | $-51.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 02:51 | +10 stop | SOL | DOWN | 0.70 | 0.54 | -1.93 |
| 10-03 02:51 | +20 | SOL | DOWN | 0.70 | 0.94 | 2.16 |
| 10-03 02:51 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 10-03 02:51 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 10-03 02:51 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 10-03 02:51 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.89 |
| 10-03 02:51 | +10 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 10-03 02:51 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-03 02:50 | +10 stop | HYPE | DOWN | 0.65 | 0.48 | -2.04 |
| 10-03 02:50 | +15 | HYPE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-03 02:50 | +10 | HYPE | DOWN | 0.66 | 0.76 | 0.76 |
| 10-03 02:50 | +5 | HYPE | DOWN | 0.66 | 0.76 | 0.76 |
| 10-03 02:48 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.86 |
| 10-03 02:48 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.86 |
| 10-03 02:47 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-03 02:47 | +10 stop | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-03 02:47 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-03 02:47 | +15 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-03 02:47 | +10 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-03 02:47 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 10-03 02:46 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-03 02:46 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.84 |
| 10-03 02:46 | +20 | HYPE | DOWN | 0.61 | 0.85 | 2.09 |
| 10-03 02:46 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.25 |
| 10-03 02:46 | +10 | HYPE | DOWN | 0.61 | 0.73 | 0.84 |
| 10-03 02:46 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.22 |
| 10-03 02:46 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-03 02:46 | +20 | BTC | DOWN | 0.60 | 0.83 | 2.03 |
| 10-03 02:46 | +15 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-03 02:46 | +10 | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-03 02:46 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-03 02:46 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-03 02:46 | +20 | DOGE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-03 02:46 | +15 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-03 02:46 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-03 02:46 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 10-03 02:46 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-03 02:46 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-03 02:46 | +15 | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 10-03 02:46 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
