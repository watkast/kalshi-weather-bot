# Range-Scalp Bot

*Updated Thu Oct 08 11:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7458 | 6458 | 1000 (13) | 0 | $-2356.76 | -5.0% |
| **+10¢** | 5665 | 4484 | 1181 (22) | 0 | $-2314.88 | -6.5% |
| **+15¢** | 4754 | 3511 | 1243 (30) | 0 | $-1919.96 | -6.4% |
| **+20¢** | 4244 | 2955 | 1289 (37) | 0 | $-1533.73 | -5.8% |
| **+10¢ (15¢ stop)** | 9047 | 9020 | 27 (17) | 0 | $-3286.86 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 10:57 | +5 | BTC | UP | 0.55 | 0.69 | 1.07 |
| 10-08 10:56 | +10 stop | BTC | UP | 0.63 | 0.46 | -2.05 |
| 10-08 10:56 | +15 | BTC | UP | 0.63 | 0.88 | 2.25 |
| 10-08 10:56 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-08 10:53 | +10 stop | ETH | DOWN | 0.55 | 0.66 | 0.76 |
| 10-08 10:53 | +10 stop | BTC | UP | 0.66 | 0.47 | -2.24 |
| 10-08 10:53 | +10 | BTC | UP | 0.66 | 0.88 | 1.96 |
| 10-08 10:53 | +5 | BTC | UP | 0.66 | 0.75 | 0.60 |
| 10-08 10:52 | +10 stop | ETH | DOWN | 0.60 | 0.45 | -1.85 |
| 10-08 10:52 | +10 stop | SOL | DOWN | 0.67 | 0.51 | -1.94 |
| 10-08 10:52 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 10-08 10:52 | +15 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 10-08 10:52 | +10 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 10-08 10:52 | +5 | SOL | DOWN | 0.71 | 0.88 | 1.47 |
| 10-08 10:50 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-08 10:50 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-08 10:47 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 10:46 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-08 10:46 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-08 10:46 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-08 10:46 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-08 10:46 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-08 10:46 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +20 | BNB | DOWN | 0.61 | 0.84 | 2.03 |
| 10-08 10:46 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +5 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-08 10:46 | +20 | HYPE | DOWN | 0.65 | 0.92 | 2.48 |
| 10-08 10:46 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.50 |
| 10-08 10:46 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-08 10:46 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-08 10:46 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-08 10:46 | +20 | DOGE | DOWN | 0.63 | 0.90 | 2.48 |
| 10-08 10:46 | +15 | DOGE | DOWN | 0.63 | 0.90 | 2.48 |
| 10-08 10:46 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-08 10:46 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-08 10:46 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-08 10:46 | +20 | ETH | UP | 0.64 | no | -6.57 |
| 10-08 10:46 | +15 | ETH | UP | 0.64 | no | -6.57 |
