# Range-Scalp Bot

*Updated Wed Oct 07 21:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6855 | 5953 | 902 (10) | 0 | $-2070.63 | -4.8% |
| **+10¢** | 5200 | 4141 | 1059 (17) | 0 | $-1956.67 | -6.0% |
| **+15¢** | 4356 | 3242 | 1114 (21) | 1 | $-1630.80 | -6.0% |
| **+20¢** | 3893 | 2732 | 1161 (28) | 2 | $-1298.33 | -5.3% |
| **+10¢ (15¢ stop)** | 8302 | 8285 | 17 (10) | 0 | $-2937.99 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 21:34 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-07 21:33 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-07 21:32 | +5 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 10-07 21:32 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 10-07 21:31 | +10 stop | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-07 21:31 | +20 | DOGE | DOWN | 0.61 | 0.87 | 2.35 |
| 10-07 21:31 | +15 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-07 21:31 | +10 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-07 21:31 | +5 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-07 21:31 | +10 stop | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-07 21:31 | +20 | ZEC | DOWN | 0.57 | 0.78 | 1.79 |
| 10-07 21:31 | +15 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 10-07 21:31 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-07 21:31 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-07 21:31 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-07 21:31 | +20 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 10-07 21:31 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 10-07 21:31 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-07 21:31 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-07 21:30 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-07 21:30 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-07 21:30 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-07 21:30 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-07 21:30 | +5 | BTC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-07 21:30 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-07 21:30 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-07 21:30 | +15 | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 10-07 21:30 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-07 21:30 | +5 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-07 21:30 | +10 stop | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 21:30 | +20 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 10-07 21:30 | +15 | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 21:30 | +10 | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 21:30 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-07 21:26 | +10 stop | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-07 21:26 | +5 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-07 21:26 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 10-07 21:26 | +20 | BTC | UP | 0.67 | no | -6.86 |
| 10-07 21:26 | +15 | BTC | UP | 0.67 | no | -6.86 |
| 10-07 21:26 | +10 | BTC | UP | 0.68 | no | -6.96 |
