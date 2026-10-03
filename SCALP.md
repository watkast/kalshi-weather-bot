# Range-Scalp Bot

*Updated Sat Oct 03 23:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1401 | 1216 | 185 (2) | 0 | $-437.78 | -4.9% |
| **+10¢** | 1074 | 871 | 203 (4) | 0 | $-273.27 | -4.0% |
| **+15¢** | 905 | 688 | 217 (5) | 0 | $-224.63 | -4.0% |
| **+20¢** | 798 | 562 | 236 (7) | 0 | $-261.53 | -5.2% |
| **+10¢ (15¢ stop)** | 1749 | 1748 | 1 (1) | 0 | $-720.46 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 22:57 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-03 22:57 | +10 stop | BTC | DOWN | 0.45 | 0.59 | 1.05 |
| 10-03 22:55 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-03 22:53 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.01 |
| 10-03 22:53 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 10-03 22:53 | +10 stop | DOGE | DOWN | 0.61 | 0.85 | 2.14 |
| 10-03 22:53 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-03 22:52 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-03 22:52 | +10 stop | BTC | UP | 0.62 | 0.27 | -3.81 |
| 10-03 22:52 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-03 22:52 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-03 22:52 | +10 stop | DOGE | UP | 0.48 | 0.61 | 0.95 |
| 10-03 22:52 | +10 stop | XRP | UP | 0.46 | 0.20 | -2.90 |
| 10-03 22:52 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-03 22:52 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-03 22:52 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-03 22:52 | +5 | DOGE | UP | 0.49 | 0.61 | 0.85 |
| 10-03 22:51 | +10 stop | SOL | UP | 0.69 | 0.50 | -2.23 |
| 10-03 22:51 | +10 stop | ETH | UP | 0.60 | 0.44 | -1.95 |
| 10-03 22:51 | +10 stop | HYPE | DOWN | 0.63 | 0.90 | 2.46 |
| 10-03 22:51 | +15 | HYPE | DOWN | 0.63 | 0.90 | 2.46 |
| 10-03 22:51 | +10 | HYPE | DOWN | 0.63 | 0.90 | 2.46 |
| 10-03 22:51 | +5 | HYPE | DOWN | 0.63 | 0.90 | 2.46 |
| 10-03 22:51 | +10 stop | XRP | DOWN | 0.71 | 0.50 | -2.39 |
| 10-03 22:51 | +10 | XRP | DOWN | 0.71 | 0.85 | 1.20 |
| 10-03 22:51 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.46 |
| 10-03 22:51 | +10 stop | SOL | DOWN | 0.64 | 0.37 | -3.04 |
| 10-03 22:51 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-03 22:51 | +5 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-03 22:50 | +5 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 10-03 22:50 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-03 22:50 | +10 stop | ETH | DOWN | 0.62 | 0.42 | -2.35 |
| 10-03 22:50 | +10 | ETH | DOWN | 0.62 | 0.80 | 1.51 |
| 10-03 22:50 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-03 22:50 | +10 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-03 22:50 | +5 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-03 22:50 | +10 stop | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-03 22:50 | +10 | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-03 22:50 | +5 | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-03 22:50 | +10 stop | BNB | UP | 0.70 | 0.83 | 1.00 |
