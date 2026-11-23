# Range-Scalp Bot

*Updated Mon Nov 23 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69291 | 60460 | 8831 (146) | 1 | $-18656.09 | -4.3% |
| **+10¢** | 51711 | 41399 | 10312 (189) | 2 | $-17304.86 | -5.3% |
| **+15¢** | 43339 | 32223 | 11116 (244) | 2 | $-15500.93 | -5.7% |
| **+20¢** | 38597 | 26912 | 11685 (305) | 2 | $-13792.41 | -5.7% |
| **+10¢ (15¢ stop)** | 84374 | 84184 | 190 (118) | 1 | $-31032.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 00:24 | +10 stop | HYPE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-23 00:23 | +10 stop | BTC | UP | 0.53 | open |  |
| 11-23 00:23 | +10 | BTC | UP | 0.53 | open |  |
| 11-23 00:23 | +5 | BTC | UP | 0.52 | 0.60 | 0.45 |
| 11-23 00:23 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 00:23 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 00:23 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-23 00:23 | +10 stop | HYPE | UP | 0.67 | 0.45 | -2.54 |
| 11-23 00:22 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 11-23 00:22 | +20 | XRP | DOWN | 0.70 | 0.93 | 2.05 |
| 11-23 00:22 | +15 | XRP | DOWN | 0.70 | 0.87 | 1.47 |
| 11-23 00:22 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 11-23 00:22 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-23 00:22 | +10 stop | BNB | UP | 0.51 | 0.30 | -2.43 |
| 11-23 00:22 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 00:22 | +10 stop | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-23 00:22 | +10 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-23 00:22 | +5 | SOL | DOWN | 0.53 | 0.62 | 0.55 |
| 11-23 00:22 | +5 | ETH | DOWN | 0.48 | 0.56 | 0.44 |
| 11-23 00:22 | +10 stop | NEAR | UP | 0.33 | 0.54 | 1.76 |
| 11-23 00:21 | +10 stop | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-23 00:21 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-23 00:21 | +10 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-23 00:21 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.53 |
| 11-23 00:21 | +10 stop | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-23 00:21 | +20 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-23 00:21 | +15 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-23 00:21 | +10 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-23 00:21 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-23 00:21 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.34 |
| 11-23 00:21 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 11-23 00:21 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 00:21 | +10 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 00:21 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 11-23 00:21 | +10 stop | HYPE | DOWN | 0.49 | 0.33 | -1.94 |
| 11-23 00:21 | +20 | HYPE | DOWN | 0.49 | 0.71 | 1.87 |
| 11-23 00:21 | +15 | HYPE | DOWN | 0.49 | 0.67 | 1.46 |
| 11-23 00:21 | +10 | HYPE | DOWN | 0.50 | 0.67 | 1.40 |
| 11-23 00:21 | +5 | HYPE | DOWN | 0.50 | 0.55 | 0.18 |
| 11-23 00:21 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
