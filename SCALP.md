# Range-Scalp Bot

*Updated Sun Nov 01 11:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43581 | 37975 | 5606 (63) | 1 | $-12447.91 | -4.5% |
| **+10¢** | 32513 | 26039 | 6474 (85) | 1 | $-11155.81 | -5.5% |
| **+15¢** | 27215 | 20244 | 6971 (112) | 1 | $-10174.83 | -6.0% |
| **+20¢** | 24165 | 16862 | 7303 (146) | 2 | $-8993.70 | -5.9% |
| **+10¢ (15¢ stop)** | 53172 | 53087 | 85 (50) | 0 | $-20103.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 11:57 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-01 11:56 | +10 stop | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-01 11:56 | +20 | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-01 11:56 | +15 | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-01 11:56 | +10 | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-01 11:56 | +5 | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-01 11:55 | +10 stop | NEAR | UP | 0.41 | 0.67 | 2.27 |
| 11-01 11:55 | +20 | NEAR | UP | 0.41 | 0.67 | 2.27 |
| 11-01 11:55 | +15 | NEAR | UP | 0.41 | 0.67 | 2.27 |
| 11-01 11:55 | +10 | NEAR | UP | 0.41 | 0.67 | 2.27 |
| 11-01 11:55 | +5 | NEAR | UP | 0.41 | 0.67 | 2.27 |
| 11-01 11:54 | +10 stop | BNB | UP | 0.67 | 0.34 | -3.62 |
| 11-01 11:53 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-01 11:53 | +10 stop | SOL | UP | 0.69 | 0.88 | 1.67 |
| 11-01 11:52 | +10 stop | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-01 11:52 | +5 | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-01 11:51 | +10 stop | BTC | DOWN | 0.68 | 0.44 | -2.74 |
| 11-01 11:50 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-01 11:50 | +10 stop | SOL | DOWN | 0.63 | 0.40 | -2.64 |
| 11-01 11:49 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.73 |
| 11-01 11:49 | +15 | HYPE | UP | 0.66 | 0.81 | 1.25 |
| 11-01 11:49 | +10 | HYPE | UP | 0.66 | 0.76 | 0.73 |
| 11-01 11:49 | +5 | HYPE | UP | 0.66 | 0.74 | 0.52 |
| 11-01 11:49 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-01 11:49 | +10 stop | NEAR | UP | 0.51 | 0.63 | 0.85 |
| 11-01 11:48 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-01 11:48 | +10 stop | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-01 11:47 | +10 stop | BNB | DOWN | 0.65 | 0.46 | -2.24 |
| 11-01 11:47 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-01 11:47 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-01 11:47 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-01 11:47 | +5 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-01 11:47 | +10 stop | DOGE | DOWN | 0.52 | 0.70 | 1.47 |
| 11-01 11:47 | +10 stop | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 11:46 | +10 stop | HYPE | UP | 0.56 | 0.69 | 0.97 |
| 11-01 11:46 | +20 | HYPE | UP | 0.56 | 0.76 | 1.69 |
| 11-01 11:46 | +15 | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-01 11:46 | +10 | HYPE | UP | 0.56 | 0.69 | 0.97 |
| 11-01 11:46 | +5 | HYPE | UP | 0.56 | 0.63 | 0.35 |
| 11-01 11:46 | +10 stop | SOL | UP | 0.63 | 0.34 | -3.23 |
