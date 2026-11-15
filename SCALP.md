# Range-Scalp Bot

*Updated Sun Nov 15 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60611 | 52871 | 7740 (112) | 0 | $-16452.46 | -4.3% |
| **+10¢** | 45281 | 36207 | 9074 (150) | 0 | $-15535.37 | -5.5% |
| **+15¢** | 37931 | 28142 | 9789 (188) | 0 | $-14224.17 | -6.0% |
| **+20¢** | 33811 | 23543 | 10268 (240) | 0 | $-12517.64 | -5.9% |
| **+10¢ (15¢ stop)** | 73761 | 73610 | 151 (89) | 0 | $-27119.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 10:17 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-15 10:17 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 11-15 10:16 | +10 stop | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-15 10:16 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-15 10:16 | +15 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-15 10:16 | +10 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-15 10:16 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-15 10:16 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-15 10:16 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-15 10:16 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-15 10:16 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-15 10:16 | +5 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-15 10:16 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.84 |
| 11-15 10:16 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-15 10:16 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 11-15 10:16 | +10 | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 10:16 | +5 | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 10:16 | +10 stop | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 10:16 | +20 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 10:16 | +15 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 10:16 | +10 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 10:16 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 11-15 10:16 | +10 stop | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-15 10:16 | +20 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-15 10:16 | +15 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-15 10:16 | +10 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-15 10:16 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 11-15 10:06 | +5 | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-15 10:03 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-15 10:03 | +5 | ZEC | UP | 0.66 | 0.72 | 0.29 |
| 11-15 10:02 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 11-15 10:01 | +10 stop | ZEC | DOWN | 0.46 | 0.29 | -2.03 |
| 11-15 10:01 | +20 | ZEC | DOWN | 0.46 | yes | -4.78 |
| 11-15 10:01 | +15 | ZEC | DOWN | 0.46 | yes | -4.78 |
| 11-15 10:01 | +10 | ZEC | DOWN | 0.46 | yes | -4.78 |
| 11-15 10:01 | +5 | ZEC | DOWN | 0.47 | 0.54 | 0.34 |
| 11-15 10:01 | +10 stop | HYPE | DOWN | 0.49 | 0.24 | -2.81 |
| 11-15 10:01 | +20 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 11-15 10:01 | +15 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 11-15 10:01 | +10 | HYPE | DOWN | 0.52 | yes | -5.38 |
