# Range-Scalp Bot

*Updated Sun Nov 15 12:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60705 | 52959 | 7746 (112) | 0 | $-16442.03 | -4.3% |
| **+10¢** | 45352 | 36270 | 9082 (150) | 0 | $-15521.49 | -5.4% |
| **+15¢** | 37990 | 28193 | 9797 (188) | 0 | $-14195.14 | -6.0% |
| **+20¢** | 33862 | 23586 | 10276 (240) | 0 | $-12478.66 | -5.9% |
| **+10¢ (15¢ stop)** | 73881 | 73730 | 151 (89) | 0 | $-27173.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 11:57 | +10 stop | ZEC | DOWN | 0.57 | 0.85 | 2.51 |
| 11-15 11:57 | +20 | ZEC | DOWN | 0.57 | 0.85 | 2.51 |
| 11-15 11:57 | +15 | ZEC | DOWN | 0.57 | 0.85 | 2.51 |
| 11-15 11:57 | +10 | ZEC | DOWN | 0.57 | 0.85 | 2.51 |
| 11-15 11:57 | +5 | ZEC | DOWN | 0.57 | 0.67 | 0.64 |
| 11-15 11:51 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-15 11:51 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-15 11:50 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-15 11:50 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-15 11:49 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-15 11:49 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-15 11:49 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-15 11:49 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 11:49 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 11:49 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 11:49 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-15 11:48 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.95 |
| 11-15 11:47 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 11-15 11:47 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-15 11:47 | +10 stop | ZEC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-15 11:47 | +20 | ZEC | DOWN | 0.56 | 0.81 | 2.21 |
| 11-15 11:47 | +15 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 11:47 | +10 | ZEC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-15 11:47 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.27 |
| 11-15 11:46 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-15 11:46 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-15 11:46 | +20 | NEAR | DOWN | 0.71 | 0.93 | 2.02 |
| 11-15 11:46 | +15 | NEAR | DOWN | 0.71 | 0.90 | 1.68 |
| 11-15 11:46 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-15 11:46 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-15 11:46 | +10 stop | ETH | DOWN | 0.57 | 0.42 | -1.86 |
| 11-15 11:46 | +20 | ETH | DOWN | 0.57 | 0.79 | 1.90 |
| 11-15 11:46 | +15 | ETH | DOWN | 0.57 | 0.75 | 1.48 |
| 11-15 11:46 | +10 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 11-15 11:46 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-15 11:46 | +10 stop | BNB | DOWN | 0.58 | 0.74 | 1.28 |
| 11-15 11:46 | +20 | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 11-15 11:46 | +15 | BNB | DOWN | 0.58 | 0.74 | 1.28 |
| 11-15 11:46 | +10 | BNB | DOWN | 0.58 | 0.74 | 1.28 |
| 11-15 11:46 | +5 | BNB | DOWN | 0.58 | 0.74 | 1.28 |
