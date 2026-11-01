# Range-Scalp Bot

*Updated Sun Nov 01 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43191 | 37648 | 5543 (62) | 0 | $-12283.72 | -4.5% |
| **+10¢** | 32209 | 25803 | 6406 (84) | 0 | $-11011.47 | -5.4% |
| **+15¢** | 26950 | 20047 | 6903 (112) | 0 | $-10069.45 | -6.0% |
| **+20¢** | 23934 | 16702 | 7232 (146) | 0 | $-8897.42 | -5.9% |
| **+10¢ (15¢ stop)** | 52662 | 52579 | 83 (48) | 0 | $-19913.26 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 04:21 | +10 stop | BNB | UP | 0.67 | 0.84 | 1.49 |
| 11-01 04:21 | +20 | BNB | UP | 0.67 | 0.89 | 2.02 |
| 11-01 04:21 | +15 | BNB | UP | 0.67 | 0.84 | 1.49 |
| 11-01 04:21 | +10 | BNB | UP | 0.67 | 0.84 | 1.49 |
| 11-01 04:21 | +5 | BNB | UP | 0.67 | 0.73 | 0.35 |
| 11-01 04:18 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 11-01 04:16 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-01 04:16 | +20 | ETH | UP | 0.69 | 0.91 | 2.03 |
| 11-01 04:16 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 11-01 04:16 | +10 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-01 04:16 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-01 04:16 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-01 04:16 | +20 | NEAR | UP | 0.69 | 0.89 | 1.78 |
| 11-01 04:16 | +15 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 11-01 04:16 | +10 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-01 04:16 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 11-01 04:16 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-01 04:16 | +20 | BTC | UP | 0.69 | 0.91 | 2.00 |
| 11-01 04:16 | +15 | BTC | UP | 0.69 | 0.87 | 1.57 |
| 11-01 04:16 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-01 04:16 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-01 04:07 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 11-01 04:07 | +5 | HYPE | UP | 0.68 | 0.74 | 0.30 |
| 11-01 04:06 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-01 04:05 | +10 stop | HYPE | DOWN | 0.49 | 0.34 | -1.84 |
| 11-01 04:05 | +10 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 11-01 04:05 | +5 | HYPE | DOWN | 0.49 | 0.56 | 0.34 |
| 11-01 04:05 | +5 | DOGE | UP | 0.64 | no | -6.57 |
| 11-01 04:05 | +10 stop | HYPE | UP | 0.20 | 0.55 | 3.20 |
| 11-01 04:05 | +10 stop | DOGE | UP | 0.59 | 0.40 | -2.24 |
| 11-01 04:05 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 11-01 04:04 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 1.01 |
| 11-01 04:04 | +10 | NEAR | DOWN | 0.62 | 0.75 | 1.01 |
| 11-01 04:04 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.39 |
| 11-01 04:03 | +10 stop | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 11-01 04:02 | +10 stop | DOGE | DOWN | 0.57 | 0.29 | -3.13 |
| 11-01 04:02 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-01 04:01 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 04:01 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 04:01 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
