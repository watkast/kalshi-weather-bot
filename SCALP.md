# Range-Scalp Bot

*Updated Wed Oct 07 22:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6934 | 6019 | 915 (10) | 0 | $-2105.10 | -4.8% |
| **+10¢** | 5257 | 4186 | 1071 (17) | 0 | $-1986.74 | -6.0% |
| **+15¢** | 4410 | 3284 | 1126 (21) | 0 | $-1643.23 | -5.9% |
| **+20¢** | 3937 | 2763 | 1174 (28) | 0 | $-1312.43 | -5.3% |
| **+10¢ (15¢ stop)** | 8396 | 8379 | 17 (10) | 0 | $-2978.92 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 22:43 | +10 stop | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 10-07 22:43 | +20 | ETH | DOWN | 0.53 | yes | -5.48 |
| 10-07 22:43 | +15 | ETH | DOWN | 0.53 | yes | -5.48 |
| 10-07 22:43 | +5 | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 10-07 22:43 | +10 stop | HYPE | DOWN | 0.27 | 0.53 | 2.28 |
| 10-07 22:41 | +5 | HYPE | DOWN | 0.71 | yes | -7.25 |
| 10-07 22:41 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-07 22:41 | +5 | SOL | DOWN | 0.65 | 0.78 | 1.02 |
| 10-07 22:40 | +10 stop | HYPE | DOWN | 0.69 | 0.53 | -1.93 |
| 10-07 22:40 | +15 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-07 22:39 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.97 |
| 10-07 22:39 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.90 |
| 10-07 22:39 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-07 22:39 | +5 | SOL | UP | 0.51 | 0.68 | 1.36 |
| 10-07 22:38 | +10 stop | BNB | UP | 0.61 | 0.45 | -1.95 |
| 10-07 22:38 | +10 stop | ETH | UP | 0.57 | 0.38 | -2.25 |
| 10-07 22:38 | +10 | ETH | UP | 0.57 | 0.84 | 2.42 |
| 10-07 22:37 | +5 | DOGE | DOWN | 0.67 | 0.78 | 0.78 |
| 10-07 22:37 | +10 stop | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 10-07 22:37 | +15 | XRP | DOWN | 0.50 | 0.66 | 1.26 |
| 10-07 22:37 | +10 | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 10-07 22:37 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-07 22:37 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-07 22:37 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-07 22:37 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-07 22:37 | +10 stop | BNB | UP | 0.54 | 0.65 | 0.76 |
| 10-07 22:37 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-07 22:37 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 22:37 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-07 22:37 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 10-07 22:37 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-07 22:37 | +10 stop | HYPE | UP | 0.65 | 0.48 | -2.04 |
| 10-07 22:37 | +15 | BNB | UP | 0.59 | 0.77 | 1.53 |
| 10-07 22:36 | +10 stop | ETH | DOWN | 0.43 | 0.54 | 0.74 |
| 10-07 22:36 | +10 | ETH | DOWN | 0.43 | 0.54 | 0.74 |
| 10-07 22:36 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 22:36 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-07 22:35 | +10 stop | BNB | DOWN | 0.63 | 0.35 | -3.13 |
| 10-07 22:35 | +10 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-07 22:35 | +5 | BNB | DOWN | 0.63 | yes | -6.47 |
