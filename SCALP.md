# Range-Scalp Bot

*Updated Mon Oct 05 13:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3861 | 3324 | 537 (3) | 0 | $-1340.70 | -5.5% |
| **+10¢** | 2993 | 2375 | 618 (4) | 0 | $-1209.59 | -6.4% |
| **+15¢** | 2515 | 1865 | 650 (7) | 0 | $-1034.17 | -6.5% |
| **+20¢** | 2245 | 1567 | 678 (12) | 0 | $-865.29 | -6.1% |
| **+10¢ (15¢ stop)** | 4779 | 4778 | 1 (1) | 0 | $-1783.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 13:40 | +10 stop | BTC | DOWN | 0.70 | 0.91 | 1.83 |
| 10-05 13:40 | +5 | BNB | DOWN | 0.64 | 0.77 | 1.02 |
| 10-05 13:39 | +10 stop | BTC | UP | 0.52 | 0.37 | -1.85 |
| 10-05 13:39 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-05 13:39 | +10 stop | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-05 13:39 | +20 | BNB | DOWN | 0.62 | 0.83 | 1.85 |
| 10-05 13:39 | +15 | BNB | DOWN | 0.62 | 0.77 | 1.22 |
| 10-05 13:39 | +10 | BNB | DOWN | 0.62 | 0.77 | 1.22 |
| 10-05 13:39 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-05 13:38 | +10 stop | BTC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-05 13:38 | +20 | BTC | DOWN | 0.61 | 0.91 | 2.71 |
| 10-05 13:38 | +15 | BTC | DOWN | 0.61 | 0.79 | 1.51 |
| 10-05 13:38 | +10 | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-05 13:38 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-05 13:36 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 13:36 | +20 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-05 13:36 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 13:36 | +10 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 13:36 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-05 13:35 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.32 |
| 10-05 13:35 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.73 |
| 10-05 13:35 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.31 |
| 10-05 13:35 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.31 |
| 10-05 13:35 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.59 |
| 10-05 13:35 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-05 13:35 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 13:35 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-05 13:35 | +10 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-05 13:35 | +5 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 13:34 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-05 13:34 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-05 13:33 | +10 stop | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 10-05 13:33 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.09 |
| 10-05 13:33 | +20 | HYPE | UP | 0.67 | 0.89 | 1.93 |
| 10-05 13:33 | +15 | HYPE | UP | 0.69 | 0.89 | 1.79 |
| 10-05 13:33 | +10 | HYPE | UP | 0.70 | 0.81 | 0.80 |
| 10-05 13:33 | +5 | HYPE | UP | 0.70 | 0.77 | 0.38 |
| 10-05 13:32 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-05 13:32 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 10-05 13:32 | +15 | ZEC | DOWN | 0.65 | 0.84 | 1.64 |
